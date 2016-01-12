from twisted.python.constants import _Constant

__author__ = 'matic'

import csv
import sys
import traceback
from BeautifulSoup import BeautifulSoup

sys.path.insert(0, '../')
import constants
import utils


def main():
    seasonsInput = raw_input('Please enter desired seasons separated by comma (all for all of them): ')
    leaguesInput = raw_input('Please enter IDs of desired leagues separated by comma (all for all of them): ')
    weightByApps = raw_input('Do you want to weight metric sums by sum of appearances? (Y/N): ')

    if(seasonsInput == 'all'):
        seasons              = seasonsInput
        seasonsString        = constants.allSeasonsString
        seasonsStringCompact = seasonsInput
    else:
        seasons              = seasonsInput.split(',')
        seasons              = [int(season) for season in seasons]
        seasonsString        = ','.join(map(str, seasons))
        seasonsStringCompact = seasonsString

    if(leaguesInput == 'all'):
        leagues              = leaguesInput
        leaguesString        = constants.allLeaguesString
        leaguesStringCompact = leaguesInput
    else:
        leagues              = leaguesInput.split(',')
        leagues              = [int(league) for league in leagues]
        leaguesString        = ','.join(map(str, leagues))
        leaguesStringCompact = leaguesString

    if(weightByApps == 'N'):
        weightByApps = False
    else:
        weightByApps = True


    # read country abbreviations from csv
    countries = dict()
    reader    = csv.reader(open('countrymapping.csv'), delimiter=",")

    for row in reader:
        try:
            countries[row[1]] = row[0].lower()
        except Exception, e:
            print "[Vizualizer GeoPlotter]  Exception occurred!", e
            traceback.print_exc()

            pass

    connection = utils.connectToDB()
    cursor     = connection.cursor()

    # loop through metrics, fetch the data, and color the map
    for metric in ['apps', 'goals', 'assists', 'ownGoals', 'yellowCards', 'redCards', 'onSubs', 'offSubs', 'penaltyGoals', 'concededGoals', 'cleanSheets']:
        print "[Vizualizer GeoPlotter]  Generating image for metric %s..." % metric

        gkMetric = (metric == 'concededGoals' or metric == 'cleanSheets')

        if((metric != 'apps' and not gkMetric) and weightByApps):
            weightByAppsString = '/SUM(pcs.apps)'
        else:
            weightByAppsString = ''

        if(gkMetric):
            cursor.execute("SELECT c.nameCountry, SUM(pcs.apps) FROM playerclubseason pcs JOIN player p USING (idP) JOIN countries c USING (idC) JOIN club cl USING (idClub) WHERE p.playingPosition = 'GK' AND pcs.idS IN (%s) AND cl.idL IN (%s) GROUP BY idC" %
                                            (seasonsString, leaguesString))

            goalKeeperAppsArray = cursor.fetchall()

        cursor.execute("SELECT c.nameCountry, SUM(pcs.apps), SUM(pcs.%s)%s FROM playerclubseason pcs JOIN player p USING (idP) JOIN countries c USING (idC) JOIN club cl USING (idClub) WHERE pcs.idS IN (%s) AND cl.idL IN (%s) GROUP BY idC ORDER BY SUM(pcs.%s) DESC" %
                        (metric, weightByAppsString, seasonsString, leaguesString, metric))

        stats = cursor.fetchall()

        # rearange stats into a dictionary
        goalKeeperAppsByCountry = dict()
        statsByCountry          = dict()
        maxValue                = 0

        if(gkMetric):
            for goalKeeperApps in goalKeeperAppsArray:
                value = goalKeeperApps[1]

                if(not value):
                    value = 0
                else:
                    value = int(value)

                goalKeeperAppsByCountry[goalKeeperApps[0]] = value

        for stat in stats:
            value   = stat[2]
            country = stat[0]

            if(weightByApps and metric != 'apps'):
                absoluteValue = stat[1]

            if(not value):
                if(weightByApps):
                    value = 0.0
                else:
                    value = 0
            else:
                if(weightByApps and metric != 'apps'):
                    # ignore countries with less than 300 apperances (if enough leagues and seasons are selected)
                    if(absoluteValue < 400 and (len(seasonsString) > 6 or seasonsString == 'all') and (len(leaguesString) > 6 or seasonsString == 'all')):
                         value = 0.0
                    else:
                        if(gkMetric):
                            value = float(value) / float(goalKeeperAppsByCountry[country])
                        else:
                            value = float(value)
                else:
                    value = int(value)

            if(value > maxValue):
                maxValue = value

            statsByCountry[stat[0].lower()] = value

        sum = 0
        num = 0
        for statByCountry in statsByCountry.values():
            if(statByCountry > 0):
                sum += statByCountry
                num += 1

        if(num != 0):
            avgValue = sum / float(num)
        else:
            avgValue = 0


        # load the SVG map and load it into Beautiful Soup
        svg  = open('countries.svg', 'r').read()
        soup = BeautifulSoup(svg, selfClosingTags=['defs', 'sodipodi:namedview', 'path'])

        # blue shades
        colors = ["#a9caea", "#9dbede", "#92b2d3", "#87a6c8", "#7b9abc", "#708eb1", "#6582a6", "#5a769b", "#4e6a8f", "#435e84", "#385279", "#2c466d", "#213a62", "#19325D", "#0b234c"]

        # find counties with and without multiple polygons
        gs    = soup.contents[2].findAll('g',    recursive=False)
        paths = soup.contents[2].findAll('path', recursive=False)

        # define what each path style should be as a base (with color fill added at the end)
        path_style = "fill-opacity:1;stroke:#ffffff;stroke-width:0.99986994;stroke-miterlimit:3.97446823;stroke-dasharray:none;stroke-opacity:1;fill:"

        # replace the style with the color fill you want
        for p in paths:
            if 'land' in p['class']:
                try:
                    value = statsByCountry[countries[p['id']]]

                    if(not weightByApps):
                        if(value < avgValue):
                            color_class = int(round(value / float(avgValue) * 10))
                        else:
                            color_class  = int(round(value / float(maxValue) * 5))
                            color_class += 9
                            color_class  = min(14, color_class)
                    else:
                        color_class = int(round(value / float(maxValue) * 14))
                        color_class = min(14, color_class)

                except:
                    continue

                # set the color we are going to use and then update the style
                color = colors[color_class]

                p['style'] = path_style + color

        # now go through all of the groups and update the style
        for g in gs:
            try:
                value = statsByCountry[countries[g['id']]]

                if(weightByApps and metric != 'apps'):
                    if(value < avgValue):
                        color_class = int(round(value / float(avgValue) * 10))
                    else:
                        color_class  = int(round(value / float(maxValue) * 5))
                        color_class += 9
                        color_class  = min(14, color_class)
                else:
                    color_class = int(round(value / float(maxValue) * 14))
                    color_class = min(14, color_class)

            except:
                continue


            # set the color we are going to use and then update the style
            color = colors[color_class]

            g['style'] = path_style + color
            # loop through all the paths within this group and update all of their styles too
            for t in g.findAll('path', recursive=True):
                t['style'] = path_style + color


        # write everything to svg file
        if(weightByApps and metric != 'apps'):
            filename = metric + 'ByCountry_leagues_' + leaguesStringCompact + '_seasons_' + seasonsStringCompact + '_weighted.svg'
        else:
            filename = metric + 'ByCountry_leagues_' + leaguesStringCompact + '_seasons_' + seasonsStringCompact + '.svg'

        f = open('Visualizations/' + filename, "w")

        # it's really important that "viewBox" is correctly capitalized and BeautifulSoup kills the capitalization in my tests
        f.write(str(soup).replace('viewbox', 'viewBox', 1))
        f.close()

        print "[Vizualizer GeoPlotter]  Image for metric %s generated" % metric

if __name__ == "__main__":
    main()