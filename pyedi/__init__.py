from typing import Optional
from pyedi.segments.utilities import split_segment
from pyedi.segments.interchange import Interchange as InterchangeSegment
from pyedi.segments.transaction_set import TransactionSet as TransactionSetSegment
from pyedi.segments.abstract_segment import AbstractSegment
from pyedi.utilities import ReversibleIterator
from pyedi.settings import Settings


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

        return collection

    def build(self, segment: list, segments: ReversibleIterator) -> Optional[AbstractSegment]:
        identifier = segment[0]

        if identifier == InterchangeSegment.identification:
            interchange = InterchangeSegment(
                segment, segments, self.settings)

            return interchange.to_serializable()

        if identifier == TransactionSetSegment.identification:
            transaction_set = TransactionSetSegment(
                segment, segments, self.settings)

            return transaction_set.to_serializable()


def parse_str(content: str, settings: Settings) -> list:
    return Edi(settings).parse(content)


def parse_file(path: str, settings: Settings) -> list:
    transaction_sets = []

    with open(path) as f:
        content = f.read()
        transaction_sets.append(parse_str(content, settings))

    return transaction_sets
