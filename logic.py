# I got some help from AI on a few parts, but I changed the code and learned how it works.
#https://www.geeksforgeeks.org/python/exporting-variable-to-csv-file-in-python/

import csv

VOTES_FILE = "votes.csv"
voters: dict[str, str] = {} #store all votes

def load_votes() -> None:
    """Load old votes from the CSV file if it exists."""
    try:
        with open(VOTES_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)

            for row in reader:
                if len(row) == 2:
                    voter_id = row[0]
                    candidate = row[1]
                    voters[voter_id] = candidate
    except FileNotFoundError:
        pass


def save_votes() -> None:
    """Save all votes to a CSV file."""
    with open(VOTES_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "candidate"])
        #write each voter and candidate they chose
        for voter_id, candidate in voters.items():
            writer.writerow([voter_id, candidate])


def add_vote(voter_id: str, candidate: str) -> bool:
    """
    Try to add a vote. Return True if added, False if id already voted.
    """
    #check if this id already voted
    if voter_id in voters:
        return False
    #save the vote
    voters[voter_id] = candidate
    save_votes()
    return True





# load saved data when program starts(AI helped this part.)
load_votes()
