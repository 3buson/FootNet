# README #

### What is it all about? ###
Footnet is a collection od tools that is capable of scraping the data about football players and clubs from a popular webpage transfermarkt. It has been intended as as scraping, analyzing and visualizing tool for football data.
It is capable of getting the info about all the players and clubs from selected leagues and for selected seasons (intended only for 2000+ years, with minor changes it could be made completely general).

Since transfermarkt does not have an API, FileGetter will take care of locally storing all the needed club HTMLs and FileParser will parse them and insert the data into database (default 'footballnetwork', initial setup SQL provided). FileParser has a function for parsing details of all the stored players including all the statistics available at transfermarkt (apps, goals, assists, ...).

Analyzer uses networkx to build a player and club network and is able to export the network into an edge list and use a version of PageRank to identify 'the best' players and springboard clubs.
As an experiment a value predictor is also available, predicting values of given players (by player ID) by checking values of this players' teammates and also taking some other data about the player into account.

Visualizer is capable of player market value through time visualizations (valuePlotter). It will accept player IDs (IDs are the same as on transfermarkt) or club id (also same as on transfermarkt), selected seasons and filename as an input and output the graph into a 'filename'.png file. Apart from that, visualizer (geoPlotter) can also output aggregated data by specific metric (goals, apps, assists, ...) by country and draw it as different shades on a SVG world map.

### Dependencies ###

* [NetworkX](https://pypi.python.org/pypi/networkx/1.10) - for Analyzer
* [Snap](https://snap.stanford.edu/snappy/) - for some basic network analyses (not required)
* [urlgrabber](https://pypi.python.org/pypi/urlgrabber/3.9.1) - for FileGetter and FileParser
* [pyquery](https://pypi.python.org/pypi/pyquery) - for FileParser
* [Matplotlib](https://pypi.python.org/pypi/matplotlib/1.5.1) - For Visualizer (valuePlotter)
* [BeautifulSoup](https://pypi.python.org/pypi/BeautifulSoup/3.2.1) - For Visualizer (geoPlotter)

### TODO ###
* Inserting into the database can be optimized a lot (disable FK ckecking, autocommits, bulk inserts, ...)
* SQL injection is possible at the moment (when accepting input as comma separated values/ids), this needs to be fixed
* Club ranking is not parsing properly because of a wired way this is displayed on transfermarkt
* ...