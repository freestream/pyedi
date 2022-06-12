from calendar import TUESDAY
from pyedi.utilities import ReversibleIterator
from pyedi.segments.utilities import split_segment
from pyedi.segments.transaction_set import TransactionSet as TransactionSetSegment
from pyedi.segments.abstract_segment import AbstractSegment
from pyedi.settings import Settings

class GroupEnvelope(AbstractSegment):
    identification = 'GS'
    terminator = 'GE'

    arguments = []
    items: dict

    def __init__(self, segment: list, segments: ReversibleIterator, settings: Settings):
        self.items = {}
        self.arguments = []

        for value in segment[1:]:
            self.arguments.append(value)

        while True:
            try:
                segment = segments.__next__()
            except StopIteration:
                break

            segment = split_segment(segment, settings.element_separator)
            identifier = segment[0]

            if identifier == self.identification:
                segments.__prev__()
                break

            if identifier == self.terminator:
                if settings.stop_on_assert_error is True:
                    assert len(self.items) == int(segment[1]), f"{self.identification} segment was expected to have {segment[1]} items, got: {len(self.items)}"

                segments.__prev__()
                break

            if identifier == TransactionSetSegment.identification:
                transaction_set = TransactionSetSegment(
                    segment, segments, settings)

                if identifier not in self.items:
                    self.items[identifier] = []

                self.items[identifier].append(
                    transaction_set.to_serializable())

    def to_serializable(self):
        return {
            'arguments': self.arguments,
            'items': self.items,
        }


if __name__ == '__main__':
    pass
