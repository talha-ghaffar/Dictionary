import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    
    if word in data:
        meaning = data[word]
        return meaning
    elif len(get_close_matches(word, data.keys()))>0:
        word1 = get_close_matches(word, data.keys())[0]
        ans = input("Do you mean %s instead? If yes press Y if no press N" %word1)
        ans = ans.lower()
        if ans == "y":
            meaning = data[word1]
            return meaning
        elif ans == "n":
            return ("such word dont exist")
        else:
            return ("sorry wrong input")
    else:
        return ("such word dont exist")


word = input("Please enter the word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
