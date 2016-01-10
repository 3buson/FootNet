__author__ = 'Matevz Lenic'

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

map = Basemap(projection='ortho',
              lat_0=0, lon_0=0)

#Fill the globe with a blue color
map.drawmapboundary(fill_color='aqua')
#Fill the continents with the land color
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()
plt.savefig('test.png')