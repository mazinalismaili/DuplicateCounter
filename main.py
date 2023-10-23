import string
text = 'This is a sample text that we want to check if any word is duplicated or not. text, word, duplicated, test, test.' # text to check
dict = {} # storing the words with count of each word

#initializing the punctuation remover (avoid word with punct like: "text,") 
translator = str.maketrans('', '', string.punctuation)

#split the text and remove punctuations
new_text = text.translate(translator).split()

#loop through the text and count each word
for word in new_text:
    if word in dict:
        dict[word] +=1
    else:
        dict[word] = 1

print(dict)
