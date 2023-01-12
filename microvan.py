#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:53:26 2023

@author: camargo
"""

#%%
import pandas as pd
from pathlib import Path

#%% reading data

DATA_PATH = Path('./data/')
MICROVAN = 'Microvan_data_CSV.csv'
DATA_DICTIONARY = 'data_dictionary.csv'

microvan = pd.read_csv(DATA_PATH.joinpath(MICROVAN))
data_dictionary = pd.read_csv(DATA_PATH.joinpath(DATA_DICTIONARY))

#%%