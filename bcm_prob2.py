#!/usr/bin/python

#import pandas
import pandas as pd

#open and read the 2 bed files
test1 = pd.read_csv("test1.bed", sep="\t")
test2 = pd.read_csv("test2.bed", sep="\t")

#create an empty dataframe
df = pd.DataFrame()

# iterating over rows of 1st file
for row in test1.itertuples():
    
    x=[]

    #check the data of 1st file against 2nd file to see if the mappings are in both chromosomes and if the mappings are longer than 1000 basepairs apart 
    x = test2[(row[1] == test2.chrm) & (abs(row[2] - test2.start) < 1000) & (abs(row[3] - test2.end) < 1000) & (row[4] == test2.num)]
   
    #get attributes row and index
    n = getattr(row, 'index')
   
     #if x is empty, continue the loop or append the data which passes the criteria to the dataframe
    if (x.empty):
        continue 
    df = df.append(x,n)
#print the reads which pass    
print (df)

