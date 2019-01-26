#!/usr/bin/env python

from __future__ import print_function
import sys
import fileinput

def raffle(number_of_winners, entries):
    return []

if __name__ == '__main__':
    try:
        number_of_winners = int(sys.argv[1])
        entry_files = sys.argv[2:]
    except (IndexError, ValueError) as e:
        print("""
USAGE: raffle.py number_of_winners [entries_file...]

    number_of_winners (required):
        The number of unique winners for the raffle
    entries_file (optional, repeated):
        Text file(s) with one raffle entry per line
        If none given, entries will be read from standard input
        Or you can specificy stdin explicitly with `-`
                 
        """, file=sys.stderr)
        sys.exit(1)
    
    entries = [line.strip() for line in fileinput.input(files=entry_files)]

    print("Selecting", number_of_winners, "winners from", entries, "...", file=sys.stderr)
    winners = raffle(number_of_winners, entries)
    print("\n".join(winners))
