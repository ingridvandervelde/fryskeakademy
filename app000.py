# Tutorial : https://shiny.rstudio.com/py/docs/get-started.html
# Reference: https://shiny.rstudio.com/py/api/

# pip install scikit-learn i.p.v. sklearn
# shiny run --reload ~/Data/onderwijs/DataWise/_code/app.py

from shiny import *
from shiny.types import FileInfo

import numpy as np
import pandas as pd

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

import pandas as pd
from sklearn.manifold import MDS

from distance_calculations import conllu_to_counter
from collections import Counter

from shiny.types import ImgData

### User Interace 

choices = {
    "Afrikaans": "Afrikaans", "Danish": "Danish", "Dutch": "Dutch",
    "English": "English", "Faroese": "Faroese", "Frisian": "Frisian",
    "German": "German",
    "Icelandic": "Icelandic", "Gronings": "Gronings"
}

app_ui = ui.page_fluid(
    # https://shiny.rstudio.com/py/api/reference/shiny.ui.input_file.html
    ui.navset_tab_card(
        ui.nav("Homepage", "info", ui.output_image("image1")),
        ui.nav("Upload CoNLL-U files",
               (ui.input_file("files", "Upload CoNLL-U files", accept=[".conllu"], multiple=True),
                #ui.input_text("x1", "Type language corresponding to the CoNLL-U file", placeholder="Enter language"),
                ui.output_ui("text_box"),
                ui.input_action_button("x1", "Calculate"),
                ui.output_plot("dendrogram1"),
                ui.output_plot("multidimensional_clustering1")
                )
               ),
        ui.nav("Choose from a set of languages",
               (ui.input_checkbox_group("x2", "Choose languages", choices),
                ui.input_action_button("x2", "Calculate", class_="btn-success"),
                ui.output_plot("dendrogram2"),
                ui.output_plot("multidimensional_clustering2")
                )
               ),
    ),
    # ui.output_plot("dendrogram"),
    # ui.output_plot("multidimensional_clustering")
)


### Server

def server(input, output, session):
    # create data structure containing conllu files

    @reactive.Effect
    @reactive.event(input.files)
    def allfiles():
        dict_languages = dict()

        files: list[FileInfo] = input.files()

        for file in files:
            path = file['datapath']
            filename = file['name']

            dict_languages[filename] = conllu_to_counter(path)
        
        return dict_languages
        
        
    @output
    @render.ui
    @reactive.event(input.files)
    def text_box():
      
        file_list = list()
        files: list[FileInfo] = input.files()
      
        for file in files:
            file_list.append(file)
            return ui.input_text("n", "Type language corresponding to the CoNLL-U file", placeholder="Enter language")
            
      
    
    # def ask_language(dict_languages: dict[str, Counter]):
    #     languages_counters: dict[str: Counter]
    # 
    #     filenames = dict_languages.keys()
    # 
    #     filename_to_language = {
    #         'file1_dutch.conllu': 'Dutch'
    #     }
    #     
    #     
    #     
    #     languages_counters = {filename_to_language[k]: v for k, v in dict_languages.items()}
    #     
    #     
    #     # {'file1_dutch.conllu': Counter()} -> {'Dutch': Counter()}
    #     # ', '.join(filenames)
    #     #
    #     # input textbox
    # 
    #     # user_input = "Dutch,English,Frisian"
    #     # language_names = user_input.split(',')
    # 
    #     return languages_counters


    # respond on 'allfiles', and calculate distances between conllu files

    # respond on 'distance matrix' and show dendrogram and multidimensional scaling plot
    
  
    
    @output
    @render.plot
    @reactive.event(input.x1)
  
    def dendrogram1():
        X = np.random.rand(15, 12)
        fig = plt.figure()

        # see: https://shiny.rstudio.com/py/docs/ui-page-layouts.html
        # and  https://www.askpython.com/python/examples/dendrograms-in-python
        dn = hierarchy.dendrogram(hierarchy.linkage(X, 'ward'),
                                  above_threshold_color="blue",
                                  color_threshold=0,
                                  orientation='right')  # or: 'average'
        return (fig)
      
    @output
    @render.plot
    @reactive.event(input.x2)
  
    def dendrogram2():
        X = np.random.rand(15, 12)
        fig = plt.figure()

        # see: https://shiny.rstudio.com/py/docs/ui-page-layouts.html
        # and  https://www.askpython.com/python/examples/dendrograms-in-python
        dn = hierarchy.dendrogram(hierarchy.linkage(X, 'ward'),
                                  above_threshold_color="blue",
                                  color_threshold=0,
                                  orientation='right')  # or: 'average'
        return (fig)
    
    
    @output
    @render.plot
    @reactive.event(input.x1)
   
    def multidimensional_clustering1():

        # see: https://www.statology.org/multidimensional-scaling-in-python/

        # create DataFrane
        df = pd.DataFrame({'player': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                           'points': [4, 4, 6, 7, 8, 14, 16, 19, 25, 25, 28],
                           'assists': [3, 2, 2, 5, 4, 8, 7, 6, 8, 10, 11],
                           'blocks': [7, 3, 6, 7, 5, 8, 8, 4, 2, 2, 1],
                           'rebounds': [4, 5, 5, 6, 5, 8, 10, 4, 3, 2, 2]})

        # set player column as index column
        df = df.set_index('player')

        # perform multi-dimensional scaling
        mds = MDS(random_state=0)
        scaled_df = mds.fit_transform(df)

        # create scatterplot
        fig = plt.scatter(scaled_df[:, 0], scaled_df[:, 1])

        # add axis labels
        plt.xlabel('Coordinate 1')
        plt.ylabel('Coordinate 2')

        # add lables to each point
        for i, txt in enumerate(df.index):
            plt.annotate(txt, (scaled_df[:, 0][i] + .3, scaled_df[:, 1][i]))

        # display scatterplot
        return (fig)
      
      
      
    @output
    @render.plot
    @reactive.event(input.x2)
   
    def multidimensional_clustering2():

        # see: https://www.statology.org/multidimensional-scaling-in-python/

        # create DataFrane
        df = pd.DataFrame({'player': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                           'points': [4, 4, 6, 7, 8, 14, 16, 19, 25, 25, 28],
                           'assists': [3, 2, 2, 5, 4, 8, 7, 6, 8, 10, 11],
                           'blocks': [7, 3, 6, 7, 5, 8, 8, 4, 2, 2, 1],
                           'rebounds': [4, 5, 5, 6, 5, 8, 10, 4, 3, 2, 2]})

        # set player column as index column
        df = df.set_index('player')

        # perform multi-dimensional scaling
        mds = MDS(random_state=0)
        scaled_df = mds.fit_transform(df)

        # create scatterplot
        fig = plt.scatter(scaled_df[:, 0], scaled_df[:, 1])

        # add axis labels
        plt.xlabel('Coordinate 1')
        plt.ylabel('Coordinate 2')

        # add lables to each point
        for i, txt in enumerate(df.index):
            plt.annotate(txt, (scaled_df[:, 0][i] + .3, scaled_df[:, 1][i]))

        # display scatterplot
        return (fig)
    
    @output
    @render.image
    def image1(): 
        from pathlib import Path
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "data\Fryke_akademy.jpeg.jpeg"), "width": "300px"}
        return img
        
      
    # @output
    # @render.image
    # def image2(): 
    #     from pathlib import Path
    #     dir = Path(__file__).resolve().parent
    #     img: ImgData = {"src": str(dir / """), "width": "150px"}
    #     return img

app = App(app_ui, server)

# test
