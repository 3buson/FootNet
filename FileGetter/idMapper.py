__author__ = 'matic'

import sys
import time
import urlgrabber
from pyquery import PyQuery as pq

sys.path.insert(0, '../')
import constants

leaguesDict  = constants.leagueURLIds
outputString = ''
baseURL      = 'http://www.transfermarkt.co.uk/liga-1/startseite/wettbewerb/'

for league, leagueURL in leaguesDict.items():
    url = baseURL + leagueURL

    try:
        leagueHTML = urlgrabber.urlopen(url, retries=10)
    except Exception, e:
        time.sleep(10)
        leagueHTML = urlgrabber.urlopen(url, retries=10)

    outputString += 'clubDict' + league + '       = dict()\n'

    document = pq(leagueHTML.read())

    leagueHTML.close()

    print "[ID Mappper]  Mapping IDs for league %s..." % (league)

    # parse clubs table
    for i in document(document(document(".items")[0]).children()[2]).children().items():
        clubName = pq(i.children()[2]).children().attr('title')
        clubURL  = pq(i.children()[2]).children().attr('href')

        clubNameNoSpace = clubName.replace(" ", "").upper()
        startClubURLIdx = clubURL.index('/verein/') + len('/verein/')
        endClubURLIdx   = clubURL.index('/saison_id/', startClubURLIdx)
        clubId          = clubURL[startClubURLIdx:endClubURLIdx]

        outputString += 'clubDict' + league + '[\'' + clubNameNoSpace[0:4] + '\'] = ' + clubId + ' # ' + clubName + '\n'

    outputString += '\n\n'

print "[ID Mappper]  Finished mapping IDs for all leagues\n\n"

print outputString