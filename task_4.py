sentence = input()

words = sentence.split()

unique_words = []

punctuation = '.,!?;:"\'()[]{}'

for word in words:
    while word and word[0] in punctuation:
        word = word[1:]
    
    while word and word[-1] in punctuation:
        word = word[:-1]
    
    if word:
        unique_words.append(word)

for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)