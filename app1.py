# returning json data as a dict and defining the function translate
# accepting input word as argument for the translate function

import json

data = json.load(open("data.json"))

def translate(w):
    return data[w]

word = input("Enter word: ")

print(translate(word))

