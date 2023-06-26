#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv(r"26_listcmprhnsn+natoalpha\NATO-alphabet\nato_phonetic_alphabet.csv")
letter_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# //Alternative but more complex
# data_dict = pandas.read_csv(r"26_listcmprhnsn+natoalpha\NATO-alphabet\nato_phonetic_alphabet.csv").to_dict()
# letter_dict = {letter:code for (index_l, letter) in data_dict["letter"].items() for (index_c, code) in data_dict["code"].items() if index_l == index_c} 

user_input = input("Enter the name: ")

letter_list = [letter_dict[f"{letter.upper()}"] for letter in user_input]
print(letter_list)