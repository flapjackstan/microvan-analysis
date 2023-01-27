#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:53:26 2023

@author: camargo
"""

#%%
import pandas as pd
from pathlib import Path

from sklearn.decomposition import PCA

#%% reading data

DATA_PATH = Path('./data/')
MICROVAN = 'Microvan_data_CSV.csv'
DATA_DICTIONARY = 'data_dictionary.csv'

microvan = pd.read_csv(DATA_PATH.joinpath(MICROVAN))
data_dictionary = pd.read_csv(DATA_PATH.joinpath(DATA_DICTIONARY))

#%%

COLS = microvan.columns.tolist()
DEMOGRAPHICS = ['age', 'income', 'miles', 'numkids', 'female', 'educ', 'recycle']
FEATURES = [item for item in COLS if item not in DEMOGRAPHICS]

#%%

pca = PCA(n_components=len(FEATURES), random_state=2023)

# train model with data
pca.fit(microvan[FEATURES])

# fit model on data
pca_32 = pca.transform(microvan[FEATURES])

#plot

#%%


pca.components_
pca.explained_variance_ratio_
#%%

pca = PCA(n_components=4, random_state=2023)
pca.fit(microvan[FEATURES])
pca_4 = pca.transform(microvan[FEATURES])

pca_df = pd.DataFrame(pca_4, columns=['1', '2', '3', '4'])
