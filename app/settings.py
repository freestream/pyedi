class Settings():
    element_separator: str
    segment_terminator: str
    sub_element_separator: str
    stop_on_assert_error: bool

    def __init__(
        self,
        element_separator: str = '*',
        segment_terminator: str = '~',
        sub_element_separator: str = '>',
        stop_on_assert_error: bool = True
    ):
        self.element_separator = element_separator
        self.segment_terminator = segment_terminator
        self.sub_element_separator = sub_element_separator
        self.stop_on_assert_error = stop_on_assert_error
