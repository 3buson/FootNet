__author__ = 'matic'

import os
import urlgrabber
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
        print "Getting HTML for club %s" % clubName

        url      = baseURL + `clubId`
        filename = baseDirname + league + '/' + season + '/' + clubName + '_' + `clubId`

        if(season != '15'):
            url = baseURL + `clubId` + '?saison_id=20' + season

        urlgrabber.urlgrab(url, filename)

fetchHTMLFiles(constants.clubDictESP, constants.leagues['spain'])
fetchHTMLFiles(constants.clubDictESP, constants.leagues['spain'], constants.seasons[2014])