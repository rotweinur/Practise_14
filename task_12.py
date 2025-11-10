def count_holes_letters(word):
    holes_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    count = 0
    for char in word:
        if char in holes_letters:
            count += 1
    return count

def main():
    text = input()
    
    holes_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    holes_count = 0
    no_holes_count = 0
    
    for char in text:
        if char.isalpha(): 
            if char in holes_letters:
                holes_count += 1
            else:
                no_holes_count += 1
    
    print(holes_count, no_holes_count)
    
    words = text.split()
    result_words = []
    
    for word in words:
        if count_holes_letters(word) >= 2:
            result_words.append(word)
    
    print(result_words)

if __name__ == "__main__":
    main()