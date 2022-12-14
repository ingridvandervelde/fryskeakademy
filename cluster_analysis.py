from distance_calculations import *
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


def mds(distances: pd.DataFrame):
    # do calculations
    dendogram = 'filled dendogram'
    return dendogram
