# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Display word lengths
print("Word Lengths:")
for word in words:
    print("{0}: {1}".format(word, len(word)))
