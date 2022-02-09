#!/usr/bin/env python

# This is the entry file. Example usage (on unix systems):

# ./index.py path/to/my/directory --phrases All the words and "phrases that I like"

import argparse

from counting import get_common_words
from printer import print_stats
from rich.console import Console

# Run this if not being imported. Accepts input from the command line and calls helper.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Glean interesting statistics from text files in a given directory. Displays by default the most common words at least 7 characters long."
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
        help="phrases to search for in the text if the most common are not desired",
    )
    args = parser.parse_args()

    # When using rich we cannot print normally, so create our rich console here so we
    # can print if we need to.
    console = Console()
    phrases = args.phrases
    # Provide default queries if none are provided.
    if phrases is None:
        phrases = get_common_words(args.source)
        console.print(
            "Printing most common long words. To specify particular words or phrases use the --phrase flag."
        )

    print_stats(console, phrases, args.source)
