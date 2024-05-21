import pytest
import tempfile
import os


@pytest.fixture
def input_data():
    return {
        "config": {
            "section1": {"key1": "value1", "key2": "value2"},
            "section2": {"key3": "value3", "key4": "value4"},
        }
    }


@pytest.fixture
def temp_files():
    input_file = tempfile.NamedTemporaryFile(delete=False)
    output_file = tempfile.NamedTemporaryFile(delete=False)
    yield input_file, output_file
    os.remove(input_file.name)
    os.remove(output_file.name)
