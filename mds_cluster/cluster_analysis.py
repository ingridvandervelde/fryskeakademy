import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform
def create_dendogram(distances: pd.DataFrame, ax: plt.Axes):
    # do calculations
    #X = np.random.rand(15, 12)
    labels = list(distances.columns.values)
    distances = squareform(distances)
    # labels = [
    #     'Afrikaans',
    #     'Danish',
    #     'German',
    #     'English',
    #     'Faroese',
    #     'Frisian',
    #     'Icelandic',
    #     'Gronings',
    #     'Dutch',
    #     'Norwegian',
    #     'Swedish']

    dnd = hierarchy.dendrogram(hierarchy.linkage(distances, 'average'),
                              above_threshold_color="blue",
                              color_threshold=0.3,
                              orientation='right',
                              labels=labels)
    ax.set_title('Dendrogram of syntactic distances between languages')
    ax.set_ylabel('Languages')
    ax.set_xlabel('Distances')
    #plt.show()

    return (dnd)
