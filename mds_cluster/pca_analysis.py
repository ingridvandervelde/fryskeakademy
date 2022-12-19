from collections import Counter
from itertools import combinations
from numpy import corrcoef
import pandas as pd
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from distance_calculations import conllu_to_counter

files = {
    'Afrikaans': '../data/af_afribooms-ud-train.conllu',
    'Danish': '../data/da_ddt-ud-train.conllu',
    #'German': 'data/de_gsd-ud-train.conllu',
    'German':'../data/de_hdt-ud-test.conllu',
    #'English': 'data/en_gum-ud-train.conllu',
    #'English': 'data/en_atis-ud-train.conllu',
    'English': '../data/en_ewt-ud-train.conllu',
    'Faroese': '../data/fo_farpahc-ud-train.conllu',
    #'Faroese': 'data/fo_oft-ud-test.conllu',
    'Frisian': '../data/fy-frysk-ud-all.conllu',
    'Icelandic': '../data/is_icepahc-ud-train.conllu',
    #'Icelandic': 'data/is_modern-ud-dev.conllu',
    'Gronings': '../data/nds-gronings-ud-all.conllu',
    #'Dutch': 'data/nl_lassysmall-ud-train.conllu',
    'Dutch': '../data/nl_alpino-ud-train.conllu',
    'Norwegian': '../data/no_bokmaal-ud-train.conllu',
    'Swedish': '../data/sv_talbanken-ud-train.conllu'
}

lang = dict()

for language, file in files.items():
    lang[language] = conllu_to_counter(file)

def calculate_distance_all_print(languages_counters: dict[str: Counter]) -> pd.DataFrame:
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

    ##############################################

    print(df)
    pca = PCA(n_components=11)
    pca.fit_transform(df)
    print('pca')
    print(pca)
    print(pca.explained_variance_ratio_.cumsum())

    pcs = pca.fit_transform(df)
    print('pcs')
    print(pcs)
    pc1_values = pcs[:, 0]
    pc2_values = pcs[:, 1]
    sns.scatterplot(x=pc1_values, y=pc2_values)
    plt.show()

    ##############################################

    # 1 minus the pearson correlation
    distances = 1 - df.T.corr()
    return distances
calculate_distance_all_print(lang)