__author__ = 'Matevz Lenic'

from pyquery import PyQuery as pq
import urlgrabber
import time
import sys
import re
import os

sys.path.insert(0, '../')
import constants
import utils

from Club import Club
from Player import Player
from Season import Season
from ClubSeason import ClubSeason
from PlayerClubSeason import PlayerClubSeason


def parseAllPlayerClubSeasonDetails(connection, seasonId='all'):
    cursor = connection.cursor()

    if(seasonId != 'all'):
        cursor.execute("SELECT pcs.idP, pcs.idS FROM playerclubseason pcs WHERE pcs.idS = ?", seasonId)
    else:
        cursor.execute("SELECT pcs.idP, pcs.idS FROM playerclubseason pcs")

    playersSeasons = cursor.fetchall()

    print "Entries to process: %d" % len(playersSeasons)

    for playerSeason in playersSeasons:
        parsePlayerClubSeasonDetails(connection, playerSeason[0], playerSeason[1])


def parsePlayerClubSeasonDetails(connection, playerId, seasonId):
    pcs     = PlayerClubSeason()
    pcs.idP = playerId
    pcs.idS = seasonId

    url        = 'http://www.transfermarkt.co.uk/randomString/leistungsdaten/spieler/' + `playerId` + '/saison/20' + `seasonId` + '/plus/1'
    playerHTML = urlgrabber.urlopen(url, retries=10)
    document   = pq(playerHTML.read())

    playerHTML.close()

    if(len(document(".items")) < 1):
        print "Player details not available"
        return

    print "Parsing player club season details for player %d, season %d..." % (playerId, seasonId)

    fieldIdx = 0

    fields = len(document(document(document('tfoot')[0]).children()[0]).children())

    for field in document(document(document('tfoot')[0]).children()[0]).children().items():
        # Goalkeeper
        if(fields == 13):
            # Apps
            if(fieldIdx == 2):
                apps = field.html()

                if(apps == '-'):
                    apps = 0

                pcs.apps = int(apps)

            # Goals
            if(fieldIdx == 3):
                goals = field.html()

                if(goals == '-'):
                    goals = 0

                pcs.goals = int(goals)

            # Own goals
            if(fieldIdx == 4):
                ownGoals = field.html()

                if(ownGoals == '-'):
                    ownGoals = 0

                pcs.ownGoals = int(ownGoals)

            # On subs
            if(fieldIdx == 5):
                onSubs = field.html()

                if(onSubs == '-'):
                    onSubs = 0

                pcs.onSubs = int(onSubs)

            # Off subs
            if(fieldIdx  == 6):
                offSubs = field.html()

                if(offSubs  == '-'):
                    offSubs  = 0

                pcs.offSubs = int(offSubs)

            # Yellow cards
            if(fieldIdx == 7):
                yellowCards = field.html()

                if(yellowCards == '-'):
                    yellowCards = 0

                pcs.yellowCards = int(yellowCards)

            # Red cards
            if(fieldIdx == 9):
                redCards = field.html()

                if(redCards == '-'):
                    redCards = 0

                pcs.redCards = int(redCards)

            # Conceded goals
            if(fieldIdx == 10):
                concededGoals = field.html()

                if(concededGoals == '-'):
                    concededGoals = 0

                pcs.concededGoals = int(concededGoals)

            # Clean sheets
            if(fieldIdx == 11):
                cleanSheets = field.html()

                if(cleanSheets == '-'):
                    cleanSheets = 0

                pcs.cleanSheets = int(cleanSheets)

            # Minutes played
            if(fieldIdx == 12):
                minutesPlayed = field.html()

                if(minutesPlayed == '-'):
                    minutesPlayed = '0\''

                pcs.minutesPlayed = int(minutesPlayed.replace('.','')[:-1])

            fieldIdx += 1

        # Not a goalkeeper
        elif(fields == 14):
            # Apps
            if(fieldIdx == 2):
                apps = field.html()

                if(apps == '-'):
                    apps = 0

                pcs.apps = int(apps)

            # Goals
            if(fieldIdx == 3):
                goals = field.html()

                if(goals == '-'):
                    goals = 0

                pcs.goals = int(goals)

            # Assists
            if(fieldIdx == 4):
                assists = field.html()

                if(assists == '-'):
                    assists = 0

                pcs.assists = int(assists)

            # Own goals
            if(fieldIdx == 5):
                ownGoals = field.html()

                if(ownGoals == '-'):
                    ownGoals = 0

                pcs.ownGoals = int(ownGoals)

            # On subs
            if(fieldIdx == 6):
                onSubs = field.html()

                if(onSubs == '-'):
                    onSubs = 0

                pcs.onSubs = int(onSubs)

            # Off subs
            if(fieldIdx  == 7):
                offSubs = field.html()

                if(offSubs  == '-'):
                    offSubs  = 0

                pcs.offSubs = int(offSubs)

            # Yellow cards
            if(fieldIdx == 8):
                yellowCards = field.html()

                if(yellowCards == '-'):
                    yellowCards = 0

                pcs.yellowCards = int(yellowCards)

            # Red cards
            if(fieldIdx == 10):
                redCards = field.html()

                if(redCards == '-'):
                    redCards = 0

                pcs.redCards = int(redCards)

            # Penalty goals
            if(fieldIdx == 11):
                penaltyGoals = field.html()

                if(penaltyGoals == '-'):
                    penaltyGoals = 0

                pcs.penaltyGoals = int(penaltyGoals)

            # Minutes per goal
            if(fieldIdx == 12):
                minutesPerGoal = field.html()

                if(minutesPerGoal == '-'):
                    minutesPerGoal = '0\''

                pcs.minutesPerGoal = int(minutesPerGoal.replace('.','')[:-1])

            # Minutes played
            if(fieldIdx == 13):
                minutesPlayed = field.html()

                if(minutesPlayed == '-'):
                    minutesPlayed = '0\''

                pcs.minutesPlayed = int(minutesPlayed.replace('.','')[:-1])

            fieldIdx += 1

    print "Updating player club season..."

    # print pcs.apps
    # print pcs.goals
    # print pcs.assists
    # print pcs.ownGoals
    # print pcs.yellowCards
    # print pcs.redCards
    # print pcs.onSubs
    # print pcs.offSubs
    # print pcs.penaltyGoals
    # print pcs.concededGoals
    # print pcs.cleanSheets
    # print pcs.minutesPerGoal
    # print pcs.minutesPlayed

    pcs.dbUpdate(connection)

    return

def parseFile(connection, filename, league, season):
    document    = pq(filename=filename)
    pcsList     = list()
    playersList = list()

    # check if club squad table is present
    if(len(document(".items")) < 1 or len(document(".empty")) > 0):
        print "Club squad not available"
        return

    clubId          = filename.split("_",2)[1]
    clubValue       = 0
    playersInserted = 0

    club          = Club()
    club.idClub   = clubId
    club.idL      = constants.leagueIds[league]
    club.nameClub = document(".spielername-profil").html().strip()

    # parse club ranking
    if(season != constants.currentSeason):
        htmlString = open(filename).read().replace('\t', '')
        match = re.search(r"(.*)Platz", htmlString)
        if(not match):
            standing = 1
        else:
            standing = match.group(1)[:-2]
    else:
        standing = 0

    # parse players table
    for i in document(document(document(".items")[0]).children()[1]).children().items():
        player = Player()
        pcs    = PlayerClubSeason()
        idx    = 0

        playerExists = False

        playerId     = pq(i.children()[1])(".spielprofil_tooltip").attr('id')
        playerNumber = pq(i.children()[0]).children().html()

        # check if player does not have a number
        if playerNumber != '-' and playerNumber:
            player.playingNumber = int(playerNumber)
        else:
            playerNumber = '-1'

        # check if player is already in the DB
        if(utils.checkIfPlayerExists(connection, playerId)):
            playerExists = True

        pcs.idS          = int(season)
        pcs.idP          = int(playerId)
        pcs.idClub       = club.idClub
        pcs.playerNumber = int(playerNumber)

        if(not playerExists):
            for j in range(0,len(i.children())):
                column = i.children()[j]

                if (str(pq(i.children()[2]).attr('class')) == "hide"):
                    prevClubPresent = False
                else:
                    prevClubPresent = True

                # Playing Position
                if idx == 0:
                    position = pq(column).attr('title')

                    if(position == 'Torwart' or position == 'Goalkeeper'):
                        player.playingPosition = 'GK'
                    elif(position == 'Abwehr' or position == 'Defence'):
                        player.playingPosition = 'DEF'
                    elif(position == 'Mittelfeld' or position == 'Midfield'):
                        player.playingPosition = 'MID'
                    elif(position == 'Sturm' or position == 'Striker'):
                        player.playingPosition = 'ATT'
                    else:
                        player.playingPosition = 'UNK'

                    idx += 1
                    continue

                # Player Name and ID
                if idx == 1:
                    nameElement = pq(column)(".spielprofil_tooltip")
                    names       = nameElement.attr('title').split(" ")

                    player.idP       = int(playerId)
                    player.firstName = names[0]
                    if len(names) > 1:
                        player.lastName = " ".join(names[1:len(names)])

                    idx += 1
                    continue

                # Birth date (only if not current season)
                if idx == 2:
                    if(prevClubPresent) and not playerExists:
                        date = pq(column).html().split(" ")
                        if(len(date) > 2):
                            player.birthDate = int(date[2])
                        else:
                            player.birthDate = -1

                        idx += 1
                        continue
                    else:
                        idx += 1
                        continue

                # Player nationality / birth date
                if idx == 3:
                    if(not playerExists):
                        if(prevClubPresent):
                            flagElement = pq(pq(column).html())

                            # check for multiple nationality
                            if len(flagElement.children()) > 0:
                                nationality = flagElement.children().attr('title')
                            else:
                                nationality = flagElement.attr('title')

                            player.nationality = nationality
                        else:
                            date = pq(column).html().split(" ")
                            if(len(date) > 2):
                                player.birthDate = int(date[2])
                            else:
                                player.birthDate = 0

                    idx += 1
                    continue

                # Player nationality (only if current season)
                if (idx == 4):
                    if(not prevClubPresent and not playerExists):
                        flagElement = pq(pq(column).html())

                        # check for multiple nationality
                        if len(flagElement.children()) > 0:
                            nationality = flagElement.children().attr('title')
                        else:
                            nationality = flagElement.attr('title')

                        player.nationality = nationality

                    idx += 1
                    continue

                # Player market value
                if (idx == 5):
                    priceString = "0"
                    multiplier  = 1

                    for character in pq(column).html().split("<")[0]:
                        if(character.isdigit() or character == '.' or character == ','):
                            priceString += character
                        elif(character == 'm'):
                            multiplier = 1000000
                        elif(character == 'k'):
                            multiplier = 1000

                    price = float(priceString) * multiplier

                    clubValue += price

                    if(price == 0):
                        price = -1

                    pcs.playerValue = price

            # player.to_string()
            playersList.append(player)
            pcsList.append(pcs)

            playersInserted += 1

        else:
            # parse only player market value
            priceString = "0"
            multiplier  = 1

            for character in pq(i.children()[5]).html().split("<")[0]:
                if(character.isdigit() or character == '.' or character == ','):
                    priceString += character
                elif(character == 'm'):
                    multiplier = 1000000
                elif(character == 'k'):
                    multiplier = 1000

            price = float(priceString) * multiplier

            clubValue += price

            if(price == 0):
                price = -1

            pcs.playerValue = price

            pcsList.append(pcs)

        # cleanup
        del pcs
        del player

    if(clubValue == 0):
        clubValue = -1

    cs         = ClubSeason()
    cs.idClub  = clubId
    cs.idS     = int(season)
    cs.ranking = int(standing)
    cs.value   = clubValue

    # inserting
    club.dbInsert(connection)
    cs.dbInsert(connection)

    for player in playersList:
        player.dbInsert(connection)

    for pcs in pcsList:
        pcs.dbInsert(connection)

    # cleanup
    del cs
    del club
    del playersList
    del pcsList

    print "Inserted %d new player(s)" % playersInserted

connection  = utils.connectToDB()

# --- PARSE ALL FILES IN A DIRECTORY --- #
rootDirectory = "../FileGetter/html/"

for dirname1, dirnames1, filenames1 in os.walk(rootDirectory):

    # loop through leagues
    for leagueDirectory in dirnames1:
        currentDirectory1 = os.path.join(dirname1, leagueDirectory)
        for dirname2, dirnames2, filenames2 in os.walk(currentDirectory1):

            # loop through seasons
            for seasonDirectory in dirnames2:
                currentDirectory2 = os.path.join(currentDirectory1, seasonDirectory)

                # loop through clubs
                for filename in os.listdir(currentDirectory2):
                    print "Parsing file %s, legue: %s, season: %s..." %\
                          (filename, leagueDirectory, seasonDirectory)

                    startTime = time.time()
                    parseFile(connection, currentDirectory2 + '/' + filename, leagueDirectory, seasonDirectory)
                    endTime = time.time()

                    print "Parsed file %s, legue: %s, season: %s | Time spent %f s" %\
                          (filename, leagueDirectory, seasonDirectory, (endTime - startTime))

                print "\nParsed season %s, league: %s\n" % (seasonDirectory, leagueDirectory)

        print "\nParsed all seasons for league %s\n" % leagueDirectory

# --- PARSE ONE FILE ONLY --- #
# filename = "../FileGetter/html/LaLiga/15/VCF_1049"
# parseFile(filename, 'LaLiga', '15')


# --- PARSE AND UPDATE PLAYER CLUB SEASON DETAILS --- #
parseAllPlayerClubSeasonDetails(connection)