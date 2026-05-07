"""
Exercise 6 — Git Stash

This script is intentionally incomplete. You'll add a new function stub
mid-way through, then stash your work to handle an urgent fix elsewhere.
See EXERCISES.md for full instructions.
"""


def load_data(filepath: str) -> list:
    """Load records from a CSV file."""
    records = []
    with open(filepath, "r") as f:
        for line in f:
            records.append(line.strip().split(","))
    return records


def filter_records(records: list, key: str) -> list:
    """Return only records where the first column matches key."""
    return [r for r in records if r[0] == key]


# TODO: Add a new function below this line as part of the exercise.
# It doesn't need to work — just add a stub like:
#
#   def summarize(records):
#       pass
