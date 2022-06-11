import re
from typing import Tuple, Optional

from numpy import mat
from app.segments.abstract_segment import AbstractSegment

class Generic(AbstractSegment):
    arguments = []

    def __init__(self, segment: list):
        self.arguments = []

        for value in segment[1:]:
            self.arguments.append(value)

    @staticmethod
    def identifier(identifier: str) -> Tuple[str, Optional[int]]:
        regex = r"(\D+)(\d*)"
        matches = re.search(regex, identifier, re.IGNORECASE)

        if matches.group(2):
            return matches.group(1), int(matches.group(2))

        return str(matches.group(1)), None

    def to_serializable(self):
        return self.arguments

if __name__ == '__main__':
    pass
