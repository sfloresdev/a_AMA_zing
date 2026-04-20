
import os
from typing import Tuple


class MazeConfig:
    def __init__(self, filepath: str):
        self.filepath: str = filepath
        self.width: int = 0
        self.height: int = 0
        self.entry: Tuple[int, int] = (-1, -1)
        self.exit: Tuple[int, int] = (-1, -1)
        self.outputfile: str = ""
        self.perfect: bool = False

        self._parse()
        self._validate()

    def _assign_value(self, key: str, value: str, line_num: int) -> None:
        try:
            if key == 'WIDTH':
                self.width = int(value)
            elif key == 'HEIGHT':
                self.height = int(value)
            elif key == 'ENTRY':
                x, y = map(int, value.split(','))
                self.entry = (x, y)
            elif key == 'EXIT':
                x, y = map(int, value.split(','))
                self.exit = (x, y)
            elif key == 'OUTPUT_FILE':
                self.outputfile = value
            elif key == 'PERFECT':
                self.perfect = bool(value)
            else:
                pass
        except ValueError:
            raise ValueError(f"Error: Type of line {line_num} for {key} key")

    def _parse(self) -> None:
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(
                f"Error: Missing config file '{self.filepath}'")

        with open(self.filepath, 'r') as file:
            for num, line in enumerate(file, 1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if '=' not in line:
                    raise ValueError(
                        f"Syntax error in line {num}. Missing '='")

                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                self._assign_value(key, value, num)

    def _validate(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Error: WIDTH and HEIGHT must be (> 0)")
        if self.entry == (-1, 1) or self.exit == (-1, -1):
            raise ValueError("Error: ENTRY and EXIT coordinates are missing")
        if not self.outputfile:
            raise ValueError("Error: Missing file specificator")
        if self.entry == self.exit:
            raise ValueError("Error: Both entry and exit can't be equal")
