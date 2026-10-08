# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the average of the ratio death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.

import pandas as pd

df= pd.read_csv("covid.csv")

print(df.head())

df=df[df['Confirmed']>0].copy()

df['ratio']=df['Deaths']/df['Confirmed']


theshold=[500, 1000, 5000]

for i in theshold:
    subset = df[df['Active']>i]
    print(f"\n Country with more {i} than:")
    print(subset['Country'].tolist())
    print(f"average of the ratio death/confirmed among those:  {subset['ratio'].mean(): 4f}" )