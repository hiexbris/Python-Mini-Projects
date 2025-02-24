import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
word = input('Give something')
word = word.upper()

diary = {row.letter: row.code for (index, row) in data.iterrows()}

output = [diary[letter] for letter in word]
print(output)
