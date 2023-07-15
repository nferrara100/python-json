# create HTML parser from given markdown text. text may be given like ~~something~~
# that will be converted to <del>something</del>

import re
from collections import deque
from dataclasses import dataclass
from typing import List

# @dataclass
# class Match:
#     key: str
#     end: int


class Parser:
    def __init__(self, key: str, replace: str) -> None:
        self.key = re.escape(key)
        self.regex = re.compile(self.key + ".+" + self.key)
        self.replace = replace

    def parse(self, text: str) -> List[str]:
        re.
        return text
