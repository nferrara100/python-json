#!/usr/bin/env python

# This is the entry file. Example usage (on unix systems):

# ./index.py path/to/my/directory --phrases All the words and "phrases that I like"

import argparse

from calculate import get_stats
from tabulate import tabulate


# Returns two dimensional lists representing the grid of our desired output.
def get_all_stats(queries, source):
    # Start with headers.
    results = [
        [
            "Word or Phrase (Total Occurrences):",
            "Documents:",
            "Sentences containing the word:",
        ],
        ["-", "-", "-"],
    ]

    # Do this for every word of phrase searched and create its own row.
    for query in queries:
        # Do the calculations
        stats = get_stats(query, source)
        # Never show more than three examples if there are more.
        num_examples = len(stats["examples"])
        shown_examples = 3
        if num_examples < 3:
            shown_examples = num_examples
        examples = "\n\n".join(stats["examples"][:shown_examples])
        # Add to output.
        results.append(
            [f"{query}({stats['count']})", ", ".join(stats["locations"]), examples]
        )
        # Add something to separate lines.
        results.append(["-", "-", "-"])
    return results


# Gets output from helper and prints to standard out.
def print_stats(queries, source):
    stats = get_all_stats(queries, source)
    output = tabulate(
        stats,
        tablefmt="plain",
    )
    print(output)


# Run this if not being imported. Accepts input from the command line and calls helper.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Glean interesting statistics from text."
    )
    parser.add_argument(
        "source",
        type=str,
        nargs="*",
        help="the relative name of the directory to examine",
    )
    parser.add_argument(
        "--phrases",
        "-p",
        type=str,
        nargs="+",
        required=True,
        help="the phrases to search for in the text",
    )
    args = parser.parse_args()

    print_stats(args.phrases, args.source)
