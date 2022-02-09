#!/usr/bin/env python

import argparse

from calculate import get_stats
from tabulate import tabulate


def get_all_stats(queries, source):
    results = [
        [
            "Word or Phrase (Total Occurrences):",
            "Documents:",
            "Sentences containing the word:",
        ],
        ["-", "-", "-"],
    ]
    for query in queries:
        stats = get_stats(query, source)
        num_examples = len(stats["examples"])
        shown_examples = 3
        if num_examples < 3:
            shown_examples = num_examples
        examples = "\n\n".join(stats["examples"][:shown_examples])
        results.append(
            [f"{query}({stats['count']})", ", ".join(stats["in_documents"]), examples]
        )
        results.append(["-", "-", "-"])
    print(
        tabulate(
            results,
            headers="firstrow",
            tablefmt="plain",
        )
    )


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
        "--words",
        "-w",
        type=str,
        nargs="+",
        required=True,
        help="the comma separated words to analyse in the text",
    )
    args = parser.parse_args()

    get_all_stats(args.words, args.source)
