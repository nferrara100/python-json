#!/usr/bin/env python

import argparse

from calculate import get_all_stats

parser = argparse.ArgumentParser(description="Glean interesting statistics from text.")
parser.add_argument(
    "source",
    type=str,
    nargs="*",
    default="data/",
    help="the relative name of the directory to examine",
)
parser.add_argument(
    "--words",
    "-w",
    type=str,
    nargs="+",
    required=True,
    help="the comma separated words to analyse in the next",
)
args = parser.parse_args()

get_all_stats(args.words, args.source)
