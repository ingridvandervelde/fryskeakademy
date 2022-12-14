from distance_calculations import conllu_to_counter, calculate_distance_pairwise, calculate_distance_all
from mds_cluster import create_dendogram
import pandas as pd
import matplotlib.pyplot as plt

files = [
    'data/file1.conllu',
    'data/file2.conllu'
]

counter_1 = conllu_to_counter(files[0])
counter_2 = conllu_to_counter(files[1])

lang = {
    'Language1': counter_1,
    'Language2': counter_2
}

df = calculate_distance_all(lang)



df.info()

# do mds with df

create_dendogram(df)


