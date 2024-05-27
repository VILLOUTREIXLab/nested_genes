#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:24:12 2024

@author: mateo
"""

import pandas as pd

df7=pd.read_table('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S7.txt')
df7.to_pickle('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S7.pkl')
df8=pd.read_table('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S8.txt')
df8.to_pickle('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S8.pkl')
