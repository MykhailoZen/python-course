import pytest


@pytest.fixture
def input_data():
    return {
        "config": {
            "section1": {"key1": "value1", "key2": "value2"},
            "section2": {"key3": "value3", "key4": "value4"},
        }
    }


def test_input_data(input_data):
    assert "config" in input_data
    assert "section1" in input_data["config"]
    assert input_data["config"]["section1"]["key1"] == "value1"
    assert input_data["config"]["section2"]["key3"] == "value3"
