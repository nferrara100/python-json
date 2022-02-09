from calculate import get_query_stats
from tabulate import tabulate


# Formats stats as required for display.
def get_formatted_stats(stats, query):
    # Never show more than three examples if there are more.
    num_examples = len(stats["examples"])
    shown_examples = 3
    if num_examples < 3:
        shown_examples = num_examples
    examples = "\n\n".join(stats["examples"][:shown_examples])
    # return as list instead of dict.
    return [f"{query}({stats['count']})", ", ".join(stats["locations"]), examples]


# Returns two dimensional lists representing the grid of our desired output.
def get_stat_grid(queries, source):
    # Start with headers.
    results = [
        [
            "Word or Phrase\n(Total Occurrences):",
            "Documents:",
            "Sentences containing the word:",
        ],
        ["-", "-", "-"],
    ]

    # Do this for every word of phrase searched and create its own row.
    for query in queries:
        # Do the calculations
        stats = get_query_stats(query, source)
        formatted_stats = get_formatted_stats(stats, query)
        results.append(formatted_stats)
        results.append(["-", "-", "-"])
    return results


# Gets output from helper and prints to standard out.
def print_stats(queries, source):
    stat_grid = get_stat_grid(queries, source)
    output = tabulate(
        stat_grid,
        tablefmt="plain",
    )
    print(output)
