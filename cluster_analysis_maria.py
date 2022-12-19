from distance_calculations import conllu_to_counter, calculate_distance_all, calculate_distance_pairwise
from mds_cluster import create_dendogram
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

files = {
    'Afrikaans': 'data/af_afribooms-ud-train.conllu',
    'Danish': 'data/da_ddt-ud-train.conllu',
    'German': 'data/de_gsd-ud-train.conllu',
    'English': 'data/en_ewt-ud-train.conllu',
    'Faroese': 'data/fo_oft-ud-test.conllu',
    'Frisian': 'data/fy-frysk-ud-all.conllu',
    'Icelandic': 'data/is_modern-ud-train.conllu',
    'Gronings': 'data/nds-gronings-ud-all.conllu',
    'Dutch': 'data/nl_alpino-ud-train.conllu',
    'Norwegian': 'data/no_bokmaal-ud-train.conllu',
    'Swedish': 'data/sv_talbanken-ud-train.conllu'
}

lang = dict()

for language, file in files.items():
    lang[language] = conllu_to_counter(file)
df = calculate_distance_all(lang)
dfp = calculate_distance_pairwise(lang)
# do mds with df
dnd = create_dendogram(df)

plt.show()
