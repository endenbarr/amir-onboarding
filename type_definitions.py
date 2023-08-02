from typing import Generator
from argparse import Namespace

ChunkType = list[str]
StringGeneratorType = Generator[str, None, None]


class ArgsNamespace(Namespace):
    input_file: str
    output_file: str
    row_limit: int
