import os
import re

from files import get_file_paths


# Get stats for this one file and this one query.
def stats_for_file(file, query):
    # Escape to avoid regex collisions
    escaped_query_string = re.escape(query)
    # Search for the query string. It must start and end with a word separator. For
    # example: Search for `me`: Me, myself, and I (match); Something (not a match).
    pattern = r"(?<=\b)(" + escaped_query_string + r")(?=\b)"
    regex = re.compile(pattern, flags=re.IGNORECASE)
    with open(file) as f:
        # Read all lines into memory to make it easier to search. Does not work for very
        # large files.
        lines = f.read()
        results = regex.findall(lines)
        matches = len(results)
        examples = []
        # Don't bother searching for example sentences if there are no matches.
        if matches > 0:
            # Split into sentences via periods, question marks, and exclamation marks.
            # This does not cover all edge cases.
            sentences = re.split("[.?!]", lines)
            # Search every sentence for matching queries and append the sentence to the
            # examples list if a match.
            for sentence in sentences:
                if regex.search(sentence):
                    formatted_sentence = " ".join(sentence.split()) + "."
                    formatted_sentence = regex.sub(
                        r"[bold red]\1[/bold red]", formatted_sentence
                    )
                    examples.append(formatted_sentence)
        return {"matches": matches, "examples": examples}


# Start calculation for word or phrase here. Find all relevant files and then call
# call helper for each. Then return data from the helper in a useful format.
def get_query_stats(query, source=None):
    count = 0
    examples = []
    locations = []
    files = get_file_paths(source)

    for file in files:
        # Perform calculations on this file for this query.
        stats = stats_for_file(file, query)
        if stats["matches"] > 0:
            # Increase the occurrence count by the number of matches found in the file.
            count += stats["matches"]
            # Unite the examples list from this file with all existing examples.
            examples += stats["examples"]
            # Gets the filename without its directory.
            filename = file.split(os.sep)[-1:][0]
            # Record this file as being a match.
            locations.append(filename)

    return {"count": count, "locations": locations, "examples": examples}
