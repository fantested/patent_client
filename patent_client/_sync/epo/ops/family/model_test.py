# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *        Source File: patent_client/_async/epo/ops/family/model_test.py        *
# ********************************************************************************

import json
from pathlib import Path

import pytest

from .model import Family
from patent_client.util.test import compare_dicts

fixtures = Path(__file__).parent / "fixtures"


def test_model():
    result = Family.objects.get("EP1000000A1")
    expected_file = fixtures / "family_model_output.json"
    # expected_file.write_text(result.model_dump_json(indent=2))
    expected = json.loads(expected_file.read_text())
    compare_dicts(json.loads(result.model_dump_json()), expected)
