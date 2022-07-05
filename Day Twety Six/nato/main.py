import pandas as pd 

nato = pd.read_csv('alphabtes.csv')
nato_list = {row.letter:row.code for(index,row) in nato.iterrows()}
word = input("Enter a word: ").upper()
result = [nato_list[letter] for  letter in word]
print(result)