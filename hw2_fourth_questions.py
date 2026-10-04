##############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the average of the ratio death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

import pandas as pd

df = pd.read_csv("covid.csv")

print(df.head())

threshold = [500, 1000, 5000]

for number in threshold:

    print(f'The countries which have more than {number} active cases.')

    filtered_df = df[df['Active'] > number].copy()

    print(filtered_df['Country'])

    filtered_df['Ratio'] = filtered_df['Deaths'] / filtered_df['Confirmed']

    print(f"Average Deaths/Confirmed cases: {filtered_df['Ratio'].mean()}")
