from pyedi.utilities import ReversibleIterator
from pyedi.segments.utilities import split_segment
from pyedi.segments.generic import Generic as GenericSegment
from pyedi.segments.address import Address as AddressSegment
from pyedi.segments.product import Product as ProductSegment
from pyedi.segments.abstract_segment import AbstractSegment
from pyedi.settings import Settings


class TransactionSet(AbstractSegment):
    identification = 'ST'
    terminator = 'SE'

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

            if identifier in [self.identification, self.terminator]:
                segments.__prev__()
                break

            if AddressSegment.test(identifier):
                item = AddressSegment(
                    segment, segments, settings)
                identifier = item.qualifier()

                self.items[identifier] = item.to_serializable()
            elif identifier == ProductSegment.identification:
                item = ProductSegment(
                    segment, segments, settings)

                if identifier not in self.items:
                    self.items[identifier] = []

                self.items[identifier] = [
                    *self.items[identifier], *item.to_serializable()]
            elif len(identifier):
                item = GenericSegment(segment)
                identifier, index = item.identifier(identifier)

                if identifier not in self.items:
                    self.items[identifier] = {}

                if index is None:
                    index = 0

                    while index in self.items[identifier]:
                        index = index + 1

                self.items[identifier][index] = item.to_serializable()

    def to_serializable(self):
        return {
            'arguments': self.arguments,
            'items': self.items,
        }


if __name__ == '__main__':
    pass
