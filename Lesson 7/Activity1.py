Text = input("Enter a piece of text:")
Word = input("Enter a word to search in the text:")

if Word in Text:
    print("The word is in the given text.")
else:
    print("The word is not in the given text.")    