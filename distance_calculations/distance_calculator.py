from collections import Counter
from itertools import combinations
from numpy import corrcoef
import pandas as pd


def calculate_distance_all(languages_counters: dict[str: Counter]) -> pd.DataFrame:
    trigrams: set[str] = set()
    distances: pd.DataFrame

    # for every language in our analysis, get the unique pos-trigrams
    for language_counter in languages_counters.values():
        trigrams.update(sorted(language_counter))

    # create the empty dataframe with the amount of languages as rows and the amount of pos-trigrams as columns
    df = pd.DataFrame(index=languages_counters.keys(), columns=sorted(trigrams))
    df = df.astype('float64')

    # iterate over all languages given
    for language_label, language_counter in languages_counters.items():
        # get the total number of trigrams in the given counter
        trigram_total: int = sum(language_counter.values())
        # set the frequencies for the language
        df.loc[language_label] = {k: v / trigram_total for k, v in language_counter.items()}

    # fill NaN so that frequencies of unknown trigrams are 0
    df = df.fillna(0)

    # 1 minus the pearson correlation
    distances = 1 - df.T.corr()
    return distances


def calculate_distance_pairwise(languages_counters: dict[str: Counter]) -> pd.DataFrame:
    # get all languages and init empty dataframe
    languages: [str] = list(languages_counters.keys())
    distances = pd.DataFrame(index=languages, columns=languages)
    distances.astype('float64')

    # get all possible combinations for pairwise comparison and iterate over them
    lang_combis = combinations(languages, 2)
    for lang_a, lang_b in lang_combis:
        # get the inventory of pos-trigrams for the two languages
        trigrams: set[str] = set(languages_counters[lang_a] + languages_counters[lang_b])

        # create an empty dataframe with the indexes and columns
        df = pd.DataFrame(index=[lang_a, lang_b], columns=sorted(trigrams))
        df = df.astype('float64')

        # get the total number of trigrams in the given counter
        len_a: int = sum(languages_counters[lang_a].values())
        len_b: int = sum(languages_counters[lang_b].values())

        # set the frequencies for the languages
        df.loc[lang_a] = {k: v / len_a for k, v in languages_counters[lang_a].items()}
        df.loc[lang_b] = {k: v / len_b for k, v in languages_counters[lang_b].items()}

        # fill NaN so that frequencies of unknown trigrams are 0
        df = df.fillna(0)

        correlation: float = df.T.corr()[lang_a][lang_b]

        # 1 minus the pearson correlation
        distances[lang_a][lang_b] = 1 - correlation
        distances[lang_b][lang_a] = 1 - correlation

    # set same language distance to 0
    distances = distances.fillna(0)
    return distances
