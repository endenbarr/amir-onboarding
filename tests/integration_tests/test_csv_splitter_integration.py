from main import create_files
from tests.mock_data import CHUNKS
import pytest
import os


@pytest.fixture
def clean_csv_files():
    yield
    for chunk_number in range(1, len(CHUNKS) + 1):
        os.remove(f"out_{chunk_number}.csv")


@pytest.mark.usefixtures("clean_csv_files")
def test_create_files():
    create_files(chunks=CHUNKS, output_file_name="out")
    assert os.path.exists("out_1.csv")
    assert os.path.exists("out_2.csv")

    with open("out_1.csv", "r") as output_file_1:
        assert output_file_1.read() == "".join(CHUNKS[0])
    with open("out_2.csv", "r") as output_file_2:
        assert output_file_2.read() == "".join(CHUNKS[1])
