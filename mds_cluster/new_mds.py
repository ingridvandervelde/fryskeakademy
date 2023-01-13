from distance_calculations import conllu_to_counter, calculate_distance_all, calculate_distance_pairwise
from sklearn.manifold import MDS
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns
from collections import Counter
from itertools import combinations
from numpy import corrcoef

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

#create scatterplot
pca = PCA(n_components=2)
pca.fit_transform(df)

pcs = pca.fit_transform(df)
plt.scatter(pcs[:, 0], pcs[:,1])

#calculate ecplained variance
var = round(sum(list(pca.explained_variance_ratio_))*100, 2)
print('\n Total Variance Explained:', var)

#add axis labels
x_axis = str(var)
plt.xlabel('\n Total Variance Explained: '+ x_axis +' %')
plt.ylabel('')

#Assign labels
for i, txt in enumerate(df.index):
    plt.annotate(txt, (pcs[:,0][i]+.01, pcs[:,1][i]))

plt.show()