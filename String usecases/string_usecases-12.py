# 12.you are developing a program to detect and correct spelling mistakes in text document. Implement a pyhton function to  suggest corrections for misspelled words in a given text string.
from textblob import TextBlob
def correct_spelling(text):
    blob=TextBlob(text)
    corrected_text=blob.correct()
    return str(corrected_text)


text="I havv a speling mistak in thiss sentense"
print(correct_spelling(text))