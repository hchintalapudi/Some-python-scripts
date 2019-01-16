#!/usr/bin/python

#importing required packages

import pandas as pd
import numpy as np

#open the two given files as pandas dataframes
platform_data = pd.read_csv("GPL6947-13512.txt", sep = "\t")
expression_data = pd.read_csv("GSE47438.csv", sep = ",")

#renaming first column in expression data as it is common for both datasets
expression_data.columns = ['ID' if x=='Row.names' else x for x in expression_data.columns]

#merge two datasets on the common column probe id
merged = pd.merge(expression_data, platform_data[['ID', 'ILMN_Gene']], on= 'ID')

# rearranging columns as required
merged_cols = merged.columns.tolist()
merged_cols = merged_cols[-1:] + merged_cols[:-1]
merged = merged[merged_cols]

#compute sum of all rows to filter gene symbols based on maximum value of sum
merged['sum'] = merged.sum(axis=1)

#filtering gene symbols 
filtered = merged[merged.groupby(['ILMN_Gene'])['sum'].transform(max) == merged['sum']]    

#delete unwanted sum column
del filtered['sum']

#output the resullt to .csv file
filtered.to_csv('output.csv', sep = ",")  
