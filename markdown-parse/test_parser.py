import pytest
from parse import Parser


def test_parse_simple_bold():
    text = "**bold**not bold"
    key = "**"
    replace = ["<b>", "</b>"]

    bold_parser = Parser(key, replace)
    result = bold_parser.parse(text)
    assert result == "<b>bold</b>not bold"
