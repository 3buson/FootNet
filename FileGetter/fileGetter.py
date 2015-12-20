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
        print "Getting HTML for club %s, league %s, season %s" % (clubName, league, season)

        url      = baseURL + `clubId`
        filename = baseDirname + league + '/' + season + '/' + clubName + '_' + `clubId`

        if(season != '15'):
            url = baseURL + `clubId` + '?saison_id=20' + season

        urlgrabber.urlgrab(url, filename)

for season in [2015, 2014, 2013, 2012, 2011, 2010]:
    fetchHTMLFiles(constants.clubDictESP, constants.leagues['spain'],   constants.seasons[season])
    fetchHTMLFiles(constants.clubDictENG, constants.leagues['england'], constants.seasons[season])
    fetchHTMLFiles(constants.clubDictGER, constants.leagues['germany'], constants.seasons[season])
    fetchHTMLFiles(constants.clubDictITA, constants.leagues['italy'],   constants.seasons[season])
    fetchHTMLFiles(constants.clubDictFRA, constants.leagues['france'],  constants.seasons[season])