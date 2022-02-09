#!/usr/bin/env python

# This is the entry file. Example usage (on unix systems):

# ./index.py path/to/my/directory --phrases All the words and "phrases that I like"

import argparse

from printer import print_stats

# Run this if not being imported. Accepts input from the command line and calls helper.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Glean interesting statistics from text files in a given directory."
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
