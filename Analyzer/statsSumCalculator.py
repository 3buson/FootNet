__author__ = 'matic'

import sys

sys.path.insert(0, '../')
import utils

def main():
    connection = utils.connectToDB()

    print "[Stats sum calculator]  Calculating clubs sums and updating clubs table..."
    utils.calculateClubsSums(connection)
    print "[Stats sum calculator]  Clubs table updated."

    print "[Stats sum calculator]  Calculating players career sums and updating players table..."
    utils.calculatePlayersCareerSums(connection)
    print "[Stats sum calculator]  Players table updated."

if __name__ == "__main__":
    main()