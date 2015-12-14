__author__ = 'matic'

import os
import urllib

dirname = 'html/'
baseURL = 'http://www.transfermarkt.co.uk/jumplist/startseite/verein/'

clubDictESP = dict()

clubDictESP['RMA']  = 418   # real madrid
clubDictESP['FCB']  = 131   # barcelona
clubDictESP['ATM']  = 13    # atletico madrid
clubDictESP['VCF']  = 1049  # valencia
clubDictESP['SEV']  = 368   # sevilla
clubDictESP['ATH']  = 621   # athletic bilbao  
clubDictESP['VIL']  = 1050  # villareal
clubDictESP['RSC']  = 681   # real sociedad
clubDictESP['CVCF'] = 418   # celta vigo
clubDictESP['ESP']  = 714   # espanyol
clubDictESP['GRCF'] = 16795 # granada
clubDictESP['DLC']  = 897   # deportivo la coruna
clubDictESP['MCF']  = 1084  # malaga
clubDictESP['RBCF'] = 150   # betis
clubDictESP['GECF'] = 3709  # getafe
clubDictESP['LCF']  = 3368  # levante
clubDictESP['RVCF'] = 367   # rayo vallecano
clubDictESP['SGCF'] = 2448  # sporting gijon
clubDictESP['ECF']  = 1533  # eibar
clubDictESP['LPCF'] = 472   # las palmas

# create HTML directory
dir = os.path.dirname(dirname)
if not os.path.exists(dir):
    os.makedirs(dir)

for clubName, clubId in clubDictESP.iteritems():
    print "Getting HTML for club %s" % clubName

    url      = baseURL + `clubId`
    filename = dirname + clubName + '_' + `clubId`

    f = open(filename,'wb')
    f.write(urllib.urlopen(url).read())
    f.close()