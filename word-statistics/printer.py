from calculate import get_query_stats
from rich.table import Table


# Formats stats as required for display.
def get_formatted_stats(stats, query):
    # Never show more than three examples if there are more.
    num_examples = len(stats["examples"])
    shown_examples = 3
    if num_examples < 3:
        shown_examples = num_examples
    examples = "\n\n".join(stats["examples"][:shown_examples])
    # return as list instead of dict.
    return (
        f"[bold red]{query}[/bold red] ({stats['count']})",
        ", ".join(stats["locations"]),
        examples,
    )


# Gets output from helper and prints to standard out.
def print_stats(console, queries, source):
    table = Table(show_header=True, show_lines=True, header_style="bold green")
    table.add_column("Word or Phrase\n(Total Occurrences)", max_width=30)
    table.add_column("Documents", max_width=15)
    table.add_column("Sentences containing the word or phrase", justify="right")
    # Do this for every word of phrase searched and create its own row.
    for query in queries:
        # Do the calculations
        stats = get_query_stats(query, source)
        formatted_stats = get_formatted_stats(stats, query)
        table.add_row(*formatted_stats)
    console.print(table)
