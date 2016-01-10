__author__ = 'matic'

import sys
sys.path.insert(0, '../')
import utils

def main():
    connection = utils.connectToDB()

    utils.calculateClubsSums(connection)

if __name__ == "__main__":
    main()