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
"""mark_security tests."""
import unittest

import flask
import webtest
from datastore import data_types
from handlers.testcase_detail import mark_security
from libs import form
from tests.test_libs import helpers as test_helpers
from tests.test_libs import test_utils


@test_utils.with_cloud_emulators("datastore")
class HandlerTest(unittest.TestCase):
  """Test Handler."""

  def setUp(self):
    test_helpers.patch(
        self,
        [
            "libs.auth.get_current_user",
            "libs.auth.is_current_user_admin",
            "handlers.testcase_detail.show.get_testcase_detail",
        ],
    )
    flaskapp = flask.Flask("testflask")
    flaskapp.add_url_rule("/", view_func=mark_security.Handler.as_view("/"))
    self.app = webtest.TestApp(flaskapp)

    self.testcase = data_types.Testcase()
    self.testcase.put()
    self.mock.is_current_user_admin.return_value = True
    self.mock.get_testcase_detail.return_value = {"testcase": "yes"}
    self.mock.get_current_user().email = "test@user.com"

  def test_succeed(self):
    """Mark a testcase as security-related."""
    self.testcase.security_flag = False
    self.testcase.put()

    resp = self.app.post_json(
        "/",
        {
            "testcaseId": self.testcase.key.id(),
            "csrf_token": form.generate_csrf_token(),
        },
    )

    self.assertEqual(200, resp.status_int)
    self.assertEqual("yes", resp.json["testcase"])

    testcase = self.testcase.key.get()
    self.assertTrue(testcase.security_flag)
