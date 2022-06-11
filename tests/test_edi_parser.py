import os
from app import parse_file
from app.settings import Settings

current_path = os.path.dirname(os.path.abspath(__file__))


def test_parse_file3():
    parse_file(current_path + '/files/file3.txt', Settings())
