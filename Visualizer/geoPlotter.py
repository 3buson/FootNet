__author__ = 'matic'

import csv
import sys
import traceback
from BeautifulSoup import BeautifulSoup

sys.path.insert(0, '../')
import utils


def main():
    seasonsInput = raw_input('Please enter desired seasons separated by comma (all for all of them): ')
    leaguesInput = raw_input('Please enter IDs of desired leagues separated by comma (all for all of them): ')
    weightByApps = raw_input('Do you want to weight metric sums by sum of appearances? (Y/N): ')

    if(seasonsInput == 'all'):
        seasons       = seasonsInput
        seasonsString = seasonsInput
    else:
        seasons       = seasonsInput.split(',')
        seasons       = [int(season) for season in seasons]
        seasonsString = ','.join(map(str, seasons))

    if(leaguesInput == 'all'):
        leagues       = leaguesInput
        leaguesString = leaguesInput
    else:
        leagues       = leaguesInput.split(',')
        leagues       = [int(league) for league in leagues]
        leaguesString = ','.join(map(str, leagues))

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

        if(metric != 'apps' and weightByApps):
            weightByAppsString = '/SUM(pcs.apps)'
        else:
            weightByAppsString = ''

        if(seasons != 'all'):
            if(leagues != 'all'):
                cursor.execute("SELECT c.nameCountry, SUM(pcs.apps), SUM(pcs.%s)%s FROM playerclubseason pcs JOIN player p USING (idP) JOIN countries c USING (idC) JOIN club cl USING (idClub) WHERE pcs.idS IN (%s) AND cl.idL IN (%s) GROUP BY idC ORDER BY SUM(pcs.%s) DESC" %
                                (metric, weightByAppsString, metric, seasonsString, leaguesString))
            else:
                cursor.execute("SELECT c.nameCountry, SUM(pcs.apps), SUM(pcs.%s)%s FROM playerclubseason pcs JOIN player p USING (idP) JOIN countries c USING (idC) WHERE pcs.idS IN (%s) GROUP BY idC ORDER BY SUM(pcs.%s) DESC" %
                                (metric, weightByAppsString, metric, seasonsString))
        elif(leagues != 'all'):
            cursor.execute("SELECT c.nameCountry, SUM(pcs.apps), SUM(pcs.%s)%s FROM playerclubseason pcs JOIN player p USING (idP) JOIN countries c USING (idC) JOIN club cl USING (idClub) WHERE cl.idL IN (%s) GROUP BY idC ORDER BY SUM(pcs.%s) DESC" %
                           (metric, weightByAppsString, metric, leaguesString))
        else:
            cursor.execute("SELECT c.nameCountry, SUM(pcs.apps), SUM(pcs.%s)%s FROM playerclubseason pcs JOIN player p USING (idP) JOIN countries c USING (idC) GROUP BY idC ORDER BY SUM(pcs.%s) DESC" %
                           (metric, weightByAppsString, metric))

        stats = cursor.fetchall()

        # rearange stats into a dictionary
        statsByCountry = dict()

        for stat in stats:
            value = stat[2]

            if(weightByApps):
                abosluteValue = stat[1]

            if(not value):
                if(weightByApps or abosluteValue < 300):
                    statsByCountry[stat[0].lower()] = 0.0
                else:
                    statsByCountry[stat[0].lower()] = 0
            else:
                if(weightByApps):
                    statsByCountry[stat[0].lower()] = float(value)
                else:
                    statsByCountry[stat[0].lower()] = int(value)

        maxValue = int(stats[4][1])

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

                except:
                    continue

                # set the color we are going to use and then update the style
                color = colors[color_class]

                p['style'] = path_style + color

        # now go through all of the groups and update the style
        for g in gs:
            try:
                value = statsByCountry[countries[g['id']]]

                if(weightByApps):
                    if(value < avgValue):
                        color_class = int(round(value / float(avgValue) * 10))
                    else:
                        color_class  = int(round(value / float(maxValue) * 5))
                        color_class += 9
                        color_class  = min(14, color_class)
                else:
                    color_class = int(round(value / float(maxValue) * 14))

            except:
                continue


            # set the color we are going to use and then update the style
            color = colors[color_class]

            g['style'] = path_style + color
            # loop through all the paths within this group and update all of their styles too
            for t in g.findAll('path', recursive=True):
                t['style'] = path_style + color


        # write everything to svg file
        if(weightByApps):
            filename = metric + 'ByCountry_leagues_' + leaguesString + '_seasons_' + seasonsString + '_weighted.svg'
        else:
            filename = metric + 'ByCountry_leagues_' + leaguesString + '_seasons_' + seasonsString + '.svg'

        f = open('Visualizations/' + filename, "w")

        # it's really important that "viewBox" is correctly capitalized and BeautifulSoup kills the capitalization in my tests
        f.write(str(soup).replace('viewbox', 'viewBox', 1))
        f.close()

        print "[Vizualizer GeoPlotter]  Image for metric %s generated" % metric

if __name__ == "__main__":
    main()