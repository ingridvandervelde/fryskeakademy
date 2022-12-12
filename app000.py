# pip install scikit-learn i.p.v. sklearn
# shiny run --reload ~/Data/onderwijs/DataWise/_code/app.py

from shiny import *
import numpy as np
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

choices = {
  "Afrikaans": "Afrikaans", "Danish": "Danish", "Dutch": "Dutch", 
  "English": "English", "Faroese": "Faroese", "Frisian": "Frisian", 
  "German": "German", 
  "Icelandic": "Icelandic", "Gronings": "Gronings"
}

app_ui = ui.page_fluid(
  ui.input_select("x1", "Choose language 1", choices),
  ui.input_select("x2", "Choose language 2", choices),
  ui.output_text_verbatim("txt"),
  ui.output_plot("dendrogram"),
  ui.output_plot("multidimensional_clustering")
)

def server(input, output, session):
  @output
  @render.text
  def txt():
    return f"You chose languages {input.x1()} and {input.x2()}"
  
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

app = App(app_ui, server)
