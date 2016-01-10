__author__ = 'matic'

import csv
import sys
import traceback
from BeautifulSoup import BeautifulSoup

sys.path.insert(0, '../')
import utils


def main():
    # Read country abbreviations from csv
    countries = dict()
    reader    = csv.reader(open('countrymapping.csv'), delimiter=",")

    for row in reader:
        try:
            countries[row[1]] = row[0].lower()
        except Exception, e:
            print "[Vizualizer GeoPlotter]  Exception occured!", e
            traceback.print_exc()

            pass

    connection = utils.connectToDB()
    cursor     = connection.cursor()

    for metric in ['apps', 'goals', 'assists', 'ownGoals', 'yellowCards', 'redCards', 'onSubs', 'offSubs', 'penaltyGoals', 'concededGoals', 'cleanSheets']:
        print "[Vizualizer GeoPlotter]  Generating image for metric %s..." % metric

        cursor.execute("SELECT c.nameCountry, SUM(pcs.%s) FROM playerclubseason pcs JOIN player p USING (idP) JOIN countries c USING (idC) GROUP BY idC ORDER BY SUM(pcs.%s) DESC" %
                       (metric, metric))

        stats = cursor.fetchall()

        # rearange stats into a dictionary
        statsByCountry = dict()

        for stat in stats:
            value = stat[1]

            if(not value):
                statsByCountry[stat[0].lower()] = 0
            else:
                statsByCountry[stat[0].lower()] = int(value)

        maxValue = int(stats[4][1])

        sum = 0
        num = 0
        for statByCountry in statsByCountry.values():
            if(statByCountry > 0):
                sum += statByCountry
                num += 1

        avgValue = sum / float(num)


        # Load the SVG map
        svg = open('countries.svg', 'r').read()

        # Load into Beautiful Soup
        soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview','path'])

        colors = ["#a9caea", "#9dbede", "#92b2d3", "#87a6c8", "#7b9abc", "#708eb1", "#6582a6", "#5a769b", "#4e6a8f", "#435e84", "#385279", "#2c466d", "#213a62", "#19325D", "#0b234c"] # blue

        # Find counties with multiple polygons
        gs = soup.contents[2].findAll('g',recursive=False)
        # Find countries without multiple polygons
        paths = soup.contents[2].findAll('path',recursive=False)

        # define what each path style should be as a base (with color fill added at the end)
        path_style = "fill-opacity:1;stroke:#ffffff;stroke-width:0.99986994;stroke-miterlimit:3.97446823;stroke-dasharray:none;stroke-opacity:1;fill:"

        # replace the style with the color fill you want
        for p in paths:
             if 'land' in p['class']:
                try:
                    value = statsByCountry[countries[p['id']]]
                    if(value < avgValue):
                        color_class = int(round(value / float(avgValue) * 10))
                    else:
                        color_class  = int(round(value / float(maxValue) * 5))
                        color_class += 9
                        color_class  = min(14, color_class)
                except:
                    continue

                # set the color we are going to use and then update the style
                color = colors[color_class]

                p['style'] = path_style + color

        # now go through all of the groups and update the style
        for g in gs:
                try:
                    value = statsByCountry[countries[g['id']]]
                    if(value < avgValue):
                        color_class = int(round(value / float(avgValue) * 10))
                    else:
                        color_class  = int(round(value / float(maxValue) * 5))
                        color_class += 9
                        color_class  = min(14, color_class)
                except:
                    continue


                # set the color we are going to use and then update the style
                color = colors[color_class]

                g['style'] = path_style + color
                # loop through all the paths within this group and update all of their styles too
                for t in g.findAll('path',recursive=True):
                    t['style'] = path_style + color


        # write everything to svg file
        filename = metric + 'ByCountry.svg'
        f = open('Visualizations/' + filename, "w")
        # it's really important that "viewBox" is correctly capitalized and BeautifulSoup kills the capitalization in my tests
        f.write(str(soup).replace('viewbox','viewBox',1))

        print "[Vizualizer GeoPlotter]  Image for metric %s generated" % metric

if __name__ == "__main__":
    main()