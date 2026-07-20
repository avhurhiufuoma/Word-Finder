#Word Finder
try:
    while True:
        word = input("input the word you want to find: ")
        text = input("input the word you want it to be found from: ")
        if word.isalpha() and text.isalpha() and len(word) > 0 and len(text) > 0:
            break
        else:
            raise ValueError
    start = 0
    found = True

    for char in word:
        pos = text.find(char, start)
        if pos < 0:
            found = False
            break
        start = pos + 1

    if found:
        print("Yes, word found in the right order.")
    else:
        print("Word not found.")
except ValueError:
    print("Input alphabets only.")
