# similarity ratio between two words
# implementing get_close_matches from the standard library difflib
# getting the user response forn the match

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        resp=input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        if resp == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif resp == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it"
      
word = input("Enter word: ")

print(translate(word))

