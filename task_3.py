sentence = input()

words = sentence.split()

cleaned_words = []

punctuation = '.,!?;:"\'()[]{}'

for word in words:
    while word and word[0] in punctuation:
        word = word[1:]
    
    while word and word[-1] in punctuation:
        word = word[:-1]
    
    if word:
        cleaned_words.append(word)

print(cleaned_words)