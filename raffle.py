#!/usr/bin/env python
import random

# ------------------
#  Raffle algorithm
# ------------------

def raffle(number_of_winners, entries):   
    secure_random = random.SystemRandom() # uses os.urandom()

    winners = set() # hold unique values only
    hat = list(entries)

    while len(winners) < number_of_winners:
        hat_size = len(hat)
        if hat_size == 0:
            raise ValueError("Not enough unique entries for {} winners".format(number_of_winners))

        random_index = secure_random.randrange(hat_size)
        drawn_entry = hat.pop(random_index) # get and remove random_index
        winners.add(drawn_entry)

    return winners


# ------------------------
#  Command-line interface
# ------------------------

USAGE="""USAGE: raffle.py number_of_winners [entries_file...]

    number_of_winners (required):
        The number of unique winners for the raffle
    entries_file (optional, repeated):
        Text file(s) with one raffle entry per line
        If none given, entries will be read from standard input (`-`)
                 
"""

if __name__ == '__main__':
    import sys
    import fileinput

    try:
        number_of_winners = int(sys.argv[1])
        entry_files = sys.argv[2:]
    except (IndexError, ValueError) as e:
        sys.stderr.write(USAGE)
        sys.exit(1)

    entries = [line.strip() for line in fileinput.input(files=entry_files)]

    sys.stderr.write("Selecting {} winners from {}...\n".format(number_of_winners, entries))
    winners = raffle(number_of_winners, entries)
    print("\n".join(winners))
