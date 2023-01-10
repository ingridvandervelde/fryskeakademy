from sklearn.manifold import MDS
import pandas as pd
import matplotlib.pyplot as plt


def create_mds(distances: pd.DataFrame, ax: plt.Axes):
    mds = MDS(random_state=0)
    scaled_df = mds.fit_transform(distances)

    # create scatterplot
    ax.scatter(scaled_df[:, 0], scaled_df[:, 1])

    # add axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # add lables to each point
    for i, txt in enumerate(distances.index):
        ax.annotate(txt, (scaled_df[:, 0][i], scaled_df[:, 1][i]))

    return scaled_df

# Obsoleted
# files = {
#     'Afrikaans': '../data/af_afribooms-ud-train.conllu',
#     'Danish': '../data/da_ddt-ud-train.conllu',
#     'German': '../data/de_gsd-ud-train.conllu',
#     'English': '../data/en_ewt-ud-train.conllu',
#     'Faroese': '../data/fo_oft-ud-test.conllu',
#     'Frisian': '../data/fy-frysk-ud-all.conllu',
#     'Icelandic': '../data/is_modern-ud-train.conllu',
#     'Gronings': '../data/nds-gronings-ud-all.conllu',
#     'Dutch': '../data/nl_alpino-ud-train.conllu',
#     'Norwegian': '../data/no_bokmaal-ud-train.conllu',
#     'Swedish': '../data/sv_talbanken-ud-train.conllu'
# }
#
# lang = dict()
#
# for language, file in files.items():
#     lang[language] = conllu_to_counter(file)
# df = calculate_distance_all(lang)
# dfp = calculate_distance_pairwise(lang)
#
#
# #perform multi-dimensional scaling
# mds = MDS(random_state=0)
# scaled_df = mds.fit_transform(df)
#
# #calculations for explained variance
# list1 = [0.49640871, 0.66261855, 0.7659065, 0.83728937, 0.88780632, 0.93446863,
#  0.95885534, 0.97855612, 0.99303231, 1, 1] #This is from the pca analysis not sure if this is the one to use though
#
# def distance(x1,y1,x2,y2):
#     dist = ((x1-x2)**2 + (y1-y2)**2)**.5
#     return(dist)
# list2 = []
# for i in range(13):
#     if i == 10:
#         break
#     list2.append(distance(scaled_df[i,0], scaled_df[i,1], scaled_df[i+1,0], scaled_df[i+1,1]))
#
#
# def variance(a,b):
#     var = (a - b)**2
#     return(var)
# list3 = []
# for i in range(11):
#     if i == 10:
#         break
#     list3.append(variance(list1[i],list2[i]))
#
# explained_variance = str(sum(list3))
#
#
#
# #create scatterplot
# plt.scatter(scaled_df[:,0], scaled_df[:,1])
#
# #add axis labels
# plt.xlabel(explained_variance +'% of the variance explained' )
# plt.ylabel('')
#
# #add lables to each point
# for i, txt in enumerate(df.index):
#     plt.annotate(txt, (scaled_df[:,0][i]+.03, scaled_df[:,1][i]))
#
# #display scatterplot
# plt.show()