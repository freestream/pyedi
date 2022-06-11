import re
from app.utilities import ReversibleIterator
from app.segments.utilities import split_segment
from app.segments.abstract_segment import AbstractSegment
from app.settings import Settings

class Address(AbstractSegment):
    qualifier_name = ''
    items = []

    def __init__(self, segment: list, segments: ReversibleIterator, settings: Settings):
        self.items = []

        regex = r"^N(\d+)$"
        identifier = segment[0]

        matches = re.search(regex, identifier, re.IGNORECASE)
        sqs = int(matches.group(1))

        self.qualifier_name = segment[1]
        self.items.append(segment[2:])

        while True:
            try:
                segment = segments.__next__()

                if segment is None:
                    break

                segment = split_segment(
                    segment, settings.element_separator)

                identifier = segment[0]

                matches = re.search(
                    regex, identifier, re.IGNORECASE)

                if not matches:
                    segments.__prev__()
                    break

                sub_sqs = int(matches.group(1))

                if (sub_sqs > sqs):
                    self.items.append(segment[1:])
                else:
                    segments.__prev__()
                    break

            except StopIteration:
                break

    def qualifier(self) -> str:
        return self.qualifier_name

    def to_serializable(self):
        return self.items

    @staticmethod
    def test(identifier: str) -> bool:
        regex = r"^N(\d+)$"

        matches = re.search(regex, identifier, re.IGNORECASE)

        if matches is None:
            return False

        return bool(matches)

    def __repr__(self):
        return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
    pass
