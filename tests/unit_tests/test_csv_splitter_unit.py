import math
from main import validate_file_length, is_input_valid, get_file_chunks
import pytest
import os
from tests.mock_data import CSV_DATA, TITLE, CSV_DATA_LINE_COUNT
from typing import Callable
from type_definitions import StringGeneratorType


def create_temp_file_fixture(file_extension: str) -> Callable[[], StringGeneratorType]:
    @pytest.fixture
    def temp_file() -> StringGeneratorType:
        file_name = f"test.{file_extension}"
        with open(file_name, "w") as test_file:
            test_file.write(CSV_DATA)
        yield file_name
        os.remove(file_name)

    return temp_file


temp_csv_file = create_temp_file_fixture(file_extension="csv")
temp_txt_file = create_temp_file_fixture(file_extension="txt")

valid_row_limits = 3
invalid_row_limits = 8


def test_validate_file_length_success(temp_csv_file):
    assert validate_file_length(input_file_path=temp_csv_file, row_limit=valid_row_limits) is True


def test_validate_file_length_should_fail_row_limit_too_high(temp_csv_file):
    assert validate_file_length(input_file_path=temp_csv_file, row_limit=invalid_row_limits) is False


def test_is_input_valid_success(temp_csv_file):
    assert is_input_valid(input_file_path=temp_csv_file, row_limit=valid_row_limits) is True


def test_is_input_valid_should_fail_file_not_exist():
    assert is_input_valid(input_file_path="non_existent_file.csv", row_limit=valid_row_limits) is False


def test_is_input_valid_should_fail_not_csv(temp_txt_file):
    assert is_input_valid(input_file_path=temp_txt_file, row_limit=valid_row_limits) is False


def test_get_file_chunks(temp_csv_file):
    row_limits = 4
    row_limits_no_header = row_limits - 1
    unrounded_expected_chunks_count = (CSV_DATA_LINE_COUNT - 1) / row_limits_no_header
    chunks = get_file_chunks(input_file_path=temp_csv_file, row_limit=row_limits)
    assert len(chunks) == math.ceil(unrounded_expected_chunks_count)
    assert len(chunks[0]) == len(chunks[1]) == row_limits
    assert len(chunks[2]) == CSV_DATA_LINE_COUNT - (math.floor(unrounded_expected_chunks_count) * row_limits_no_header)
    assert all([chunk[0] == TITLE for chunk in chunks])
    assert chunks[0][3] == "DataA3,DataB3,78,Value3\n"
    assert chunks[1][2] == "DataA5,DataB5,60,Value5\n"
    assert chunks[2][1] == "DataA7,DataB7,24,Value7\n"
