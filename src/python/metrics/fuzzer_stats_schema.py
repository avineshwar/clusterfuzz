# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Fuzzer stats schema."""

_COMMON_COLUMNS = [
    {
        "mode": "NULLABLE",
        "name": "kind",
        "type": "STRING"
    },
    {
        "mode": "NULLABLE",
        "name": "timestamp",
        "type": "FLOAT"
    },
    {
        "mode": "REPEATED",
        "name": "command",
        "type": "STRING"
    },
    {
        "mode": "NULLABLE",
        "name": "build_revision",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "fuzzer",
        "type": "STRING"
    },
    {
        "mode": "NULLABLE",
        "name": "job",
        "type": "string"
    },
    {
        "mode": "NULLABLE",
        "name": "source",
        "type": "STRING"
    },
]

_AFL_SCHEMA = [
    {
        "mode": "NULLABLE",
        "name": "strategy_fast_cal_random",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "dict_used",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "new_units_generated",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "crash_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "manual_dict_size",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "timeout_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "stability",
        "type": "FLOAT"
    },
    {
        "mode": "NULLABLE",
        "name": "corpus_crash_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "startup_crash_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "timeout_limit",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_subset",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "bad_instrumentation",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "average_exec_per_sec",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_fast_cal_manual",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "corpus_size",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "new_units_added",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "log_lines_unwanted",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "actual_duration",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "expected_duration",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "oom_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "log_lines_ignored",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_mutations",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "read_units",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "max_len",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "log_lines_from_engine",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_recommended_dict",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "exception_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "slow_unit_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_value_profile",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "recommended_dict_size",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "leak_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_mutations_radamsa",
        "type": "INTEGER",
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_mutations_ml_rnn",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_selection_method",
        "type": "STRING"
    },
] + _COMMON_COLUMNS

_LIBFUZZER_SCHEMA = [
    {
        "mode": "NULLABLE",
        "name": "max_len",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "log_lines_ignored",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "feature_coverage",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "average_exec_per_sec",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "crash_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "expected_duration",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "leak_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_subset",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_dataflow_tracing",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "number_of_executed_units",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "slow_unit_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_mutations_radamsa",
        "type": "INTEGER",
    },
    {
        "mode": "NULLABLE",
        "name": "log_lines_from_engine",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "merge_edge_coverage",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_random_max_len",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "peak_rss_mb",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "corpus_crash_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "startup_crash_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "edge_coverage",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "new_units_generated",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "initial_feature_coverage",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "manual_dict_size",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_fork",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "bad_instrumentation",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "initial_edge_coverage",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "timeout_limit",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "dict_used",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "fuzzing_time_percent",
        "type": "FLOAT"
    },
    {
        "name": "new_features",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "log_lines_unwanted",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "slowest_unit_time_sec",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "edges_total",
        "type": "INTEGER"
    },
    {
        "name": "new_edges",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "timeout_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_mutations_ml_rnn",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_entropic",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "slow_units_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "oom_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_selection_method",
        "type": "STRING"
    },
    {
        "mode": "NULLABLE",
        "name": "recommended_dict_size",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "actual_duration",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_value_profile",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_recommended_dict",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "corpus_size",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "new_units_added",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_mutator_plugin",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_mutator_plugin_radamsa",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_peach_grammar_mutation",
        "type": "STRING"
    },
    {
        "mode": "NULLABLE",
        "name": "corpus_rss_mb",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "merge_new_files",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "merge_new_features",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_handle_unstable",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_weighted_mutations",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "strategy_corpus_mutations",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "read_units",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "seed_corpus_rss",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "exception_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "edge_coverage_count",
        "type": "INTEGER"
    },
] + _COMMON_COLUMNS

_HONGGFUZZ_SCHEMA = [
    {
        "mode": "NULLABLE",
        "name": "timeout_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "branch_coverage_percent",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "guard_nb",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "crashes_count",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "new_units_added",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "slowest_unit_ms",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "peak_rss_mb",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "iterations",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "time",
        "type": "INTEGER"
    },
    {
        "mode": "NULLABLE",
        "name": "speed",
        "type": "INTEGER"
    },
] + _COMMON_COLUMNS

_SCHEMA = {
    "afl": _AFL_SCHEMA,
    "honggfuzz": _HONGGFUZZ_SCHEMA,
    "libFuzzer": _LIBFUZZER_SCHEMA,
}


def get(engine_name):
  """Get the schema for an engine name."""
  schema = _SCHEMA.get(engine_name)
  if not schema:
    return None

  return {"fields": schema}
