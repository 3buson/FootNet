__author__ = 'matic'

import sys
sys.path.insert(0, '../')
import utils

def main():
    connection = utils.connectToDB()

    utils.calculatePlayersCareerSums(connection)

if __name__ == "__main__":
    main()