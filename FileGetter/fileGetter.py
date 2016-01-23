__author__ = 'matic'

import os
import sys
import time
import urlgrabber

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
        print "[File Getter]  Getting HTML for club: %s\tleague: %s\tseason: 20%s" % \
              (clubName, league, season)

        url      = baseURL + `clubId`
        filename = baseDirname + league + '/' + season + '/' + clubName + '_' + `clubId`

        if(season != '15'):
            url = baseURL + `clubId` + '?saison_id=20' + season

        # because of different season schedule seasons are shifted for one number in MLS...
        if(league == 'MajorLeagueSoccer'):
            url = baseURL + `clubId` + '?saison_id=' + `(int('20' + season) - 1)`

        try:
            urlgrabber.urlgrab(url, filename, retries=5)
        except Exception, e:
            time.sleep(60)
            urlgrabber.urlgrab(url, filename, retries=5)

            print "Exception occurred!", e
            print "URL: ", url

            pass

def main():
    for season in constants.seasons.keys():
        for country in constants.leagues.keys():
            league = constants.leagues[country]
            fetchHTMLFiles(constants.clubs[league], league, constants.seasons[season])

            print "\n[File Getter]  Fetched all HTML files for league %s\n" % league

        print "\n[File Getter]  Fetched all HTML files for all leagues for season %s\n" % \
              season

if __name__ == "__main__":
    main()