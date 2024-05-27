#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

"""
To translate file from txt to pkl for faster loading
txt file of table s7 and s8 can be found at https://www.science.org/doi/10.1126/science.aax1971#supplementary-materials
from the article https://pubmed.ncbi.nlm.nih.gov/31488706/
"""

df7=pd.read_table('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S7.txt')
df7.to_pickle('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S7.pkl')
df8=pd.read_table('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S8.txt')
df8.to_pickle('Biomart_and_Packer_data/NIHMS1604359-supplement-Table_S8.pkl')
