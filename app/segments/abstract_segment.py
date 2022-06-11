class AbstractSegment():
    def __repr__(self):
        return '\n'.join(str(item) for item in self.__dict__.items())

    def default(self, o):
        return o.__dict__

    def to_serializable(self):
        pass

if __name__ == '__main__':
    pass
