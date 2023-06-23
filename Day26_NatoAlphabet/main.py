from typing import List

import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv("nato_phonetic_alphabet.csv")

# this works the same as the list comprehension
# data_dict = df.set_index('letter')['code'].to_dict()

# .items() for list and .iterrows() for csv
# '_' used when a variable is not going to be used or reference in a loop. Acts as placeholder

data_dict = {row.letter: row.code for _, row in df.iterrows()}


# print(data_dict)
# print(dataWithPandas)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word:").upper()

nato_list = [data_dict[letter] for letter in word]

print(nato_list)