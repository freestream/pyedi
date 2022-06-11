import re
from app.utilities import ReversibleIterator
from app.segments.utilities import split_segment
from app.segments.abstract_segment import AbstractSegment
from app.settings import Settings

class Product(AbstractSegment):
    identification = 'PO1'
    items = []

    def __init__(self, segment: list, segments: ReversibleIterator, settings: Settings):
        self.items = []

        regex = r"^PO(\d+)$"

        item = {0: segment[1:]}

        while True:
            try:
                segment = segments.__next__()

                if segment is None:
                    break

                segment = split_segment(
                    segment, settings.element_separator)

                identifier = segment[0]

                if 'PID' == identifier:
                    item['desc'] = segment[1:]
                elif self.identification == identifier:
                    self.items.append(item)
                    item = {0: segment[1:]}
                else:
                    matches = re.search(
                        regex, identifier, re.IGNORECASE)

                    if not matches:
                        self.items.append(item)
                        segments.__prev__()
                        break

                    index = int(matches.group(1))
                    item[index] = segment[1:]

            except StopIteration:
                self.items.append(item)
                break

    def to_serializable(self):
        return self.items


if __name__ == '__main__':
    pass
