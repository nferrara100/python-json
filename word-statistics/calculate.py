import os
import re


# Get stats for this one file and this one query.
def stats_for_file(file, query):
    # Accepts a single word (escaped). It must be preceded by whitespace and can not be
    # followed by another letter, but can be followed by punctuation. For example:
    # Search for `me`: Me, myself, and I (match); Something (not a match).
    pattern = f"(?<=\s){re.escape(query)}(?![a-z])"
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
                    examples.append(" ".join(sentence.split()) + ".")
        return {"matches": matches, "examples": examples}


# Start calculation for word or phrase here. Find all relevant files and then call
# call helper for each. Then return data from the helper in a useful format.
def get_query_stats(query, source=None):
    # If no source is provided locate the example data relative to this file.
    if source is None or len(source) == 0:
        script_dir = os.path.dirname(__file__)
        source = [os.path.join(script_dir, "example_data/")]
    count = 0
    examples = []
    locations = []

    # Find all the files in the source folder.
    # Loop through source if there are multiple source directories.
    for dir in source:
        abs_dir_path = os.path.abspath(dir)
        try:
            for filename in os.listdir(abs_dir_path):
                # Don't examine files that are not text files so all data is the same.
                if filename[4:] != ".txt":
                    continue
                abs_filename = os.path.join(abs_dir_path, filename)

                # Perform calculations on this file for this query.
                stats = stats_for_file(abs_filename, query)
                if stats["matches"] > 0:
                    # Increase the occurrence count by the number of matches found in the file.
                    count += stats["matches"]
                    # Unite the examples list from this file with all existing examples.
                    examples += stats["examples"]
                    # Record this file as being a match.
                    locations.append(filename)
        # Return a pretty error when a file is not found. Continue looking for other
        # files.
        except FileNotFoundError:
            print(f"Error: {dir} does not exist.")
    return {"count": count, "locations": locations, "examples": examples}
