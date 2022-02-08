import os
import re


def number_of_in(word, file):
    pattern = f"\s{re.escape(word)}[^a-z]"
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, file)
    with open(abs_file_path) as f:
        lines = f.read()
        results = re.findall(pattern, lines, flags=re.IGNORECASE)
        return len(results)


def number_of(word):
    count = 0
    for i in range(1, 6):
        count += number_of_in(word, f"data/doc{i}.txt")
    return count
