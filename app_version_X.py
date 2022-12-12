from shiny import App, render, ui

import plotly.figure_factory as ff
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import pandas as pd
from sklearn.cluster import KMeans
from scipy.spatial import ConvexHull

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
  ui.output_plot("dendogram"),
  ui.output_plot("multidimensional_clustering"),
)

def server(input, output, session):
  @output
  @render.text
  def txt():
    return f"You chose languages {input.x1()} and {input.x2()}"
  @output
  @render.plot
  def dendogram():
    np.random.seed(1)
    X = np.random.rand(15, 12)
    fig = ff.create_dendrogram(X)
    fig.update_layout(width=800, height=500)
    return fig.show()
  @output
  @render.plot
  def multidimensional_clustering():
    df = pd.read_csv(r'C:\Users\vande\OneDrive\Documenten\School\Jaar 3\Minor\Collaborative data project\Pokemon.csv')
    # k means
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['cluster'] = kmeans.fit_predict(df[['Attack', 'Defense']])
    # get centroids
    centroids = kmeans.cluster_centers_
    cen_x = [i[0] for i in centroids] 
    cen_y = [i[1] for i in centroids]
    ## add to df
    df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2]})
    df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2]})
    # define and map colors
    colors = ['#DF2020', '#81DF20', '#2095DF']
    df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})
    fig, ax = plt.subplots(1, figsize=(8,8))
    plt.scatter(df.Attack, df.Defense, c=df.c, alpha = 0.6, s=10)
    plt.scatter(cen_x, cen_y, marker='^', c=colors, s=70)
    
    for i in df.cluster.unique():
    # get the convex hull
      points = df[df.cluster == i][['Attack', 'Defense']].values
      hull = ConvexHull(points)
      x_hull = np.append(points[hull.vertices,0],
                       points[hull.vertices,0][0])
      y_hull = np.append(points[hull.vertices,1],
                       points[hull.vertices,1][0])
    
      # interpolate
      dist = np.sqrt((x_hull[:-1] - x_hull[1:])**2 + (y_hull[:-1] - y_hull[1:])**2)
      dist_along = np.concatenate(([0], dist.cumsum()))
      spline, u = interpolate.splprep([x_hull, y_hull], 
                                    u=dist_along, s=0, per=1)
      interp_d = np.linspace(dist_along[0], dist_along[-1], 50)
      interp_x, interp_y = interpolate.splev(interp_d, spline)
      # plot shape
      plt.fill(interp_x, interp_y, '--', c=colors[i], alpha=0.2)
    
    plt.xlim(0,200)
    plt.ylim(0,200)
    return plt.show()

app = App(app_ui, server)
