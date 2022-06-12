from typing import List, Optional


def split_segment(segment: str, elementTerminator: str) -> List[str]:
	segment = segment.split(elementTerminator)
	stripped = [s.strip() for s in segment]
	return stripped


def find_identifier(segment: str, elementTerminator: str) -> str:
	segment = split_segment(segment, elementTerminator)
	return segment[0]


def get_element(segment: List[str], index: int, default=None) -> Optional[str]:
	element = default
	if index < len(segment):
		element = segment[index]

	return element

