# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""App Engine helpers."""

from __future__ import print_function

from distutils import spawn
import os
import shutil
import sys

from local.butler import common
from local.butler import constants

SRC_DIR_PY = os.path.join("src", "appengine")
SRC_DIR_GO = os.path.join("src", "go", "server")


def _is_go_yaml(file_path):
    """Whether or not this is a go yaml path."""
    return os.path.basename(file_path).startswith("go-")


def _get_target_directory(yaml_path):
    """Get target directory to copy appengine yaml to."""
    return SRC_DIR_GO if _is_go_yaml(yaml_path) else SRC_DIR_PY


def _add_env_vars_if_needed(yaml_path, additional_env_vars):
    """Add environment variables to yaml file if necessary."""
    # Defer imports since our python paths have to be set up first.
    import yaml
    from src.python.config import local_config

    env_values = local_config.ProjectConfig().get("env")
    if additional_env_vars:
        env_values.update(additional_env_vars)

    if not env_values:
        return

    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict) or "service" not in data:
        # Not a service.
        return

    if "runtime" in data and data["runtime"].startswith("go"):
        # Remove HELP_FORMAT as multi-line environment variable values are not
        # allowed in Go flex deployment.
        env_values.pop("HELP_FORMAT", None)

    data.setdefault("env_variables", {}).update(env_values)
    with open(yaml_path, "w") as f:
        yaml.safe_dump(data, f)


def copy_yamls_and_preprocess(paths, additional_env_vars=None):
    """Copy paths to appengine source directories since they reference sources
    and otherwise, deployment fails."""
    rebased_paths = []
    for path in paths:
        target_directory = _get_target_directory(path)
        target_filename = os.path.basename(path)
        rebased_path = os.path.join(target_directory, target_filename)

        # Remove target in case it's a symlink, since shutil.copy follows symlinks.
        if os.path.exists(rebased_path):
            os.remove(rebased_path)
        shutil.copy(path, rebased_path)
        os.chmod(rebased_path, 0o600)

        _add_env_vars_if_needed(rebased_path, additional_env_vars)
        rebased_paths.append(rebased_path)

    return rebased_paths


def find_sdk_path():
    """Find the App Engine SDK path."""
    if common.get_platform() == "windows":
        _, gcloud_path = common.execute("where gcloud.cmd", print_output=False)
    else:
        gcloud_path = spawn.find_executable("gcloud")

    if not gcloud_path:
        print("Please install the Google Cloud SDK and set up PATH to point to it.")
        sys.exit(1)

    cloud_sdk_path = os.path.dirname(os.path.dirname(os.path.realpath(gcloud_path)))
    appengine_sdk_path = os.path.join(cloud_sdk_path, "platform", "google_appengine")
    if not os.path.exists(appengine_sdk_path):
        print("App Engine SDK not found. Please run local/install_deps.bash")
        sys.exit(1)

    return appengine_sdk_path


def filter_yaml_paths(yaml_paths, deploy_go):
    """Filter yaml paths."""
    if deploy_go:
        return yaml_paths

    return [yaml_path for yaml_path in yaml_paths if not _is_go_yaml(yaml_path)]


def symlink_dirs():
    """Symlink folders for use on appengine."""
    symlink_config_dir()

    common.symlink(
        src=os.path.join("src", "protos"), target=os.path.join(SRC_DIR_PY, "protos")
    )
    common.symlink(
        src=os.path.join("src", "python"), target=os.path.join(SRC_DIR_PY, "python")
    )
    # While importing third party modules, we may call pkg_resources.
    # pkg_resources normalizes paths by calling os.path.realpath on them, which is
    # incompatible with the App Engine sandbox since the resulting path will no
    # longer be under appengine/.
    common.copy_dir(
        src=os.path.join("src", "third_party"),
        target=os.path.join(SRC_DIR_PY, "third_party"),
    )

    # Remove existing local_gcs symlink (if any). This is important, as otherwise
    # we will try deploying the directory in production. This is only needed for
    # local development in run_server.
    local_gcs_symlink_path = os.path.join(SRC_DIR_PY, "local_gcs")
    common.remove_symlink(local_gcs_symlink_path)

    _, output = common.execute("bazel run //local:create_gopath", cwd="src")
    os.environ["GOPATH"] = output.splitlines()[-1]


def build_templates():
    """Build template files used in appengine."""
    common.execute("python polymer_bundler.py", cwd="local")


def symlink_config_dir():
    """Symlink config directory in appengine directory."""
    config_dir = os.getenv("CONFIG_DIR_OVERRIDE", constants.TEST_CONFIG_DIR)
    common.symlink(src=config_dir, target=os.path.join(SRC_DIR_PY, "config"))
    common.symlink(src=config_dir, target=os.path.join(SRC_DIR_GO, "config"))


def region_from_location(location):
    """Convert an app engine location ID to a region."""
    if not location[-1].isdigit():
        # e.g. us-central -> us-central1
        location += "1"

    return location


def region(project):
    """Get the App Engine region."""
    return_code, location = common.execute(
        "gcloud app describe --project={project} "
        '--format="value(locationId)"'.format(project=project)
    )
    if return_code:
        raise RuntimeError("Could not get App Engine region")

    return region_from_location(location.strip())
