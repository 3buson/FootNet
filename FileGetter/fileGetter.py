__author__ = 'matic'

import os
import urlgrabber

import sys
sys.path.insert(0, '../')
import constants


baseDirname = 'html/'
baseURL     = 'http://www.transfermarkt.co.uk/jumplist/startseite/verein/'

def fetchHTMLFiles(clubDict, league, season='15'):
    # create HTML directory
    dir = os.path.dirname(baseDirname)
    if not os.path.exists(dir):
        os.makedirs(dir)

    # create league directory inside HTML directory
    dir = os.path.dirname(baseDirname + league + '/')
    if not os.path.exists(dir):
        os.makedirs(dir)

    # create season directory inside league directory
    dir = os.path.dirname(baseDirname + league + '/' + season + '/')
    if not os.path.exists(dir):
        os.makedirs(dir)

    for clubName, clubId in clubDict.iteritems():
        print "Getting HTML for club: %s\tleague: %s\tseason: 20%s" % (clubName, league, season)

        url      = baseURL + `clubId`
        filename = baseDirname + league + '/' + season + '/' + clubName + '_' + `clubId`

        if(season != '15'):
            url = baseURL + `clubId` + '?saison_id=20' + season

        urlgrabber.urlgrab(url, filename)

def main():
    for season in constants.seasons.keys():
        for country in constants.leagues.keys():
            league = constants.leagues[country]
            fetchHTMLFiles(constants.clubs[league], league, constants.seasons[season])

            print "\nFetched all HTML files for league %s" % league

        print "\nFetched all HTML files for all leagues for season 20%s" % season

if __name__ == "__main__":
    main()