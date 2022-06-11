from app.settings import Settings
from app.utilities import ReversibleIterator
from app.segments.utilities import split_segment
from app.segments.group_envelope import GroupEnvelope as GroupEnvelopeSegment
from app.segments.abstract_segment import AbstractSegment
from app.settings import Settings

class Interchange(AbstractSegment):
    identification = 'ISA'
    terminator = 'ESA'

    arguments = []
    items: dict

    def __init__(self, segment: list, segments: ReversibleIterator, settings: Settings):
        self.items = {}
        self.arguments = []

        for value in segment[1:]:
            self.arguments.append(value)

        print(settings)

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
                assert len(self.items) == int(segment[1]), f"{self.identification} segment was expected to have {segment[1]} items, got: {len(self.items)}"

                segments.__prev__()
                break

            if identifier == GroupEnvelopeSegment.identification:
                group_envelope = GroupEnvelopeSegment(
                    segment, segments, settings)

                if identifier not in self.items:
                    self.items[identifier] = []

                self.items[identifier].append(group_envelope.to_serializable())

    def to_serializable(self):
        return {
            'arguments': self.arguments,
            'items': self.items,
        }

if __name__ == '__main__':
    pass
