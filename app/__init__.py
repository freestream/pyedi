import json
from typing import Optional
from app.segments.utilities import split_segment
from app.segments.interchange import Interchange as InterchangeSegment
from app.segments.abstract_segment import AbstractSegment
from app.utilities import ReversibleIterator
from app.settings import Settings


class Edi:
    settings: Settings

    def __init__(
        self,
        settings: Settings,
    ):
        self.settings = settings

    def parse(self, content: str) -> dict:
        segments = content.strip().split(self.settings.segment_terminator)
        segments = [segment.strip() for segment in segments]
        segments = ReversibleIterator(iter(segments))

        collection = {}

        while True:
            try:
                segment = segments.__next__()
            except StopIteration:
                break

            segment = split_segment(segment, self.settings.element_separator)
            identifier = segment[0]

            if identifier not in collection:
                collection[identifier] = []

            collection[identifier].append(self.build(segment, segments))

            break

        print(json.dumps(collection))

    def build(self, segment: list, segments: ReversibleIterator) -> Optional[AbstractSegment]:
        identifier = segment[0]

        if identifier == InterchangeSegment.identification:
            interchange = InterchangeSegment(
                segment, segments, self.settings)
            return interchange.to_serializable()


def parse_file(path: str, settings: Settings) -> list:
    transaction_sets = []

    with open(path) as f:
        content = f.read()
        transaction_sets.append(Edi(settings).parse(content))

    return transaction_sets
