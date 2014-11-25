from collections import OrderedDict
import numpy as np
import pandas as pd

from bokeh.charts import Histogram

# we build some distributions and load them into a dict
mu, sigma = 0, 0.5
normal = np.random.normal(mu, sigma, 1000)
lognormal = np.random.lognormal(mu, sigma, 1000)
distributions = OrderedDict(normal=normal, lognormal=lognormal)

# then we create a pandas df from the dict
df = pd.DataFrame(distributions)
distributions = df.to_dict()

for k, v in distributions.items():
    distributions[k] = v.values()

# any of the following commented are valid Bar inputs
#df = distributions.values()
#df = tuple(distributions.values())
#df = tuple([tuple(x) for x in distributions.values()])
#df = np.array(distributions.values())
#df = distributions.values()[0]

hist = Histogram(df, bins=50, filename="histograms.html")
hist.title("Histograms").ylabel("frequency").legend(True)
hist.width(400).height(350).show()