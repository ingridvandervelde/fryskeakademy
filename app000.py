# Tutorial : https://shiny.rstudio.com/py/docs/get-started.html
# Reference: https://shiny.rstudio.com/py/api/

# pip install scikit-learn i.p.v. sklearn
# shiny run --reload ~/Data/onderwijs/DataWise/_code/app.py

from shiny import *
from shiny.types import FileInfo

import numpy as np
import pandas as pd

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

import pandas as pd
from sklearn.manifold import MDS

### User Interace 

app_ui = ui.page_fluid(
# https://shiny.rstudio.com/py/api/reference/shiny.ui.input_file.html
  ui.input_file("files", "Upload CoNLL-U files", accept=[".conllu"], multiple=True),

  ui.output_plot("dendrogram"),
  ui.output_plot("multidimensional_clustering")
)

### Server

def server(input, output, session):

# create data structure containing conllu files

  @reactive.Effect
  @reactive.event(input.files)
  def allfiles():
    listFiles = list()
    
    for x in range(0,4):
       f: list[FileInfo] = input.files()
       df = pd.read_csv(f[0]["datapath"])
       listFiles.append(df)
    return(listFiles)

# respond on 'allfiles', and calculate distances between conllu files

# respond on 'distance matrix' and show dendrogram and multidimensional scaling plot

  @output
  @render.plot
  def dendrogram():
    X = np.random.rand(15, 12)
    fig = plt.figure()

  # see: https://shiny.rstudio.com/py/docs/ui-page-layouts.html
  # and  https://www.askpython.com/python/examples/dendrograms-in-python
    dn = hierarchy.dendrogram(hierarchy.linkage(X, 'ward'), 
                              above_threshold_color="blue", 
                              color_threshold=0,
                              orientation='right') # or: 'average'
    return(fig)



  @output
  @render.plot
  def multidimensional_clustering():
    
  # see: https://www.statology.org/multidimensional-scaling-in-python/
    
  # create DataFrane
    df = pd.DataFrame({'player': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                       'points': [4, 4, 6, 7, 8, 14, 16, 19, 25, 25, 28],
                       'assists': [3, 2, 2, 5, 4, 8, 7, 6, 8, 10, 11],
                       'blocks': [7, 3, 6, 7, 5, 8, 8, 4, 2, 2, 1],
                       'rebounds': [4, 5, 5, 6, 5, 8, 10, 4, 3, 2, 2]})

  # set player column as index column
    df = df.set_index('player')

  # perform multi-dimensional scaling
    mds = MDS(random_state=0)
    scaled_df = mds.fit_transform(df)
    
  # create scatterplot
    fig = plt.scatter(scaled_df[:,0], scaled_df[:,1])

  # add axis labels
    plt.xlabel('Coordinate 1')
    plt.ylabel('Coordinate 2')

  # add lables to each point
    for i, txt in enumerate(df.index):
      plt.annotate(txt, (scaled_df[:,0][i]+.3, scaled_df[:,1][i]))

  # display scatterplot
    return(fig)

app = App(app_ui, server)
