from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill')
m.drawcoastlines()
m.fillcontinents()

plt.title('My first map')
plt.show()
