import argparse
import os.path
from typing import Type
import logging
from type_definitions import ChunkType, ArgsNamespace

ERR_MSG = "Error message: Invalid input. Make sure the input file is a valid csv file."


def get_args() -> Type[ArgsNamespace]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=str, required=True)
    parser.add_argument("-o", "--output_file", type=str, required=True)
    parser.add_argument("-r", "--row_limit", type=int, required=True)
    return parser.parse_args(namespace=ArgsNamespace)


def validate_file_length(input_file_path: str, row_limit: int) -> bool:
    num_of_lines = 0
    with open(input_file_path, "r") as csv_file:
        for line in csv_file:
            num_of_lines += 1
    return num_of_lines > row_limit


def is_input_valid(input_file_path: str, row_limit: int) -> bool:
    is_valid_file = os.path.isfile(input_file_path) and os.path.exists(input_file_path)
    if not is_valid_file:
        return False
    is_csv = input_file_path.lower().endswith(".csv")
    if not is_csv:
        return False
    if row_limit < 1:
        return False

    return validate_file_length(input_file_path=input_file_path, row_limit=row_limit)


def get_file_chunks(input_file_path: str, row_limit: int) -> list[ChunkType]:
    chunks = []
    with open(input_file_path, "r") as csv_file:
        header = csv_file.readline()
        current_chunk = [header]
        for line in csv_file.readlines():
            current_chunk.append(line)
            if len(current_chunk) == row_limit:
                chunks.append(current_chunk)
                current_chunk = [header]

    if len(current_chunk) > 1:
        chunks.append(current_chunk)
    return chunks


def create_files(chunks: list[ChunkType], output_file_name: str) -> None:
    for i, chunk in enumerate(chunks):
        output_name_with_suffix = f"{output_file_name}_{i + 1}.csv"
        with open(output_name_with_suffix, "w") as output_file:
            output_file.writelines(chunk)
            logging.info(
                f'Output file number {i + 1} was created with the name "{output_name_with_suffix}" and it has {len(chunk)}'
                f' lines.'
            )


def main() -> None:
    args = get_args()

    if not is_input_valid(input_file_path=args.input_file, row_limit=args.row_limit):
        logging.error(ERR_MSG)
        exit()

    chunks = get_file_chunks(input_file_path=args.input_file, row_limit=args.row_limit)
    create_files(chunks=chunks, output_file_name=args.output_file)


if __name__ == "__main__":
    main()