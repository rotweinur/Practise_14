from collections import Counter

text = []
while True:
    line = input()
    if line == "":
        break
    text.append(line)

full_text = " ".join(text).lower()

punctuation = '.,!?;:"\'()[]{}'
cleaned_text = ""
for char in full_text:
    if char not in punctuation:
        cleaned_text += char

words = cleaned_text.split()

word_count = Counter(words)

seen_order = []
for word in words:
    if word not in seen_order:
        seen_order.append(word)


sorted_words = sorted(seen_order, key=lambda x: word_count[x], reverse=True)

for word in sorted_words:
    print(word)