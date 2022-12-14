from distance_calculations import conllu_to_counter, calculate_distance_pairwise, calculate_distance_all
from mds_cluster import create_dendogram
import pandas as pd
import matplotlib.pyplot as plt

files = {
    'Language1': 'data/file1.conllu',
    'Language2': 'data/file2.conllu',
    'Language3': 'data/file3.conllu'
}

lang = dict()

for language, file in files.items():
    lang[language] = conllu_to_counter(file)


df = calculate_distance_all(lang)
# df = calculate_distance_pairwise(lang)


df.info()

# do mds with df

create_dendogram(df)


