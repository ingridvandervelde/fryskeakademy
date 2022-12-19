import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform
def create_dendogram(distances: pd.DataFrame):
    # do calculations
    #X = np.random.rand(15, 12)
    fig = plt.figure()
    distances = squareform(distances)
    labels = [
        'Afrikaans',
        'Danish',
        'German',
        'English',
        'Faroese',
        'Frisian',
        'Icelandic',
        'Gronings',
        'Dutch',
        'Norwegian',
        'Swedish']

    dnd = hierarchy.dendrogram(hierarchy.linkage(distances, 'average'),
                              above_threshold_color="blue",
                              color_threshold=0.3,
                              orientation='right',
                              labels=labels)
    #plt.title('Dendrogram')
    #plt.xlabel('Customers')
    #plt.ylabel('Euclidean distances')
    #plt.show()

    return (dnd)