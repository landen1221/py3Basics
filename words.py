def print_upper_words(lst, starts_with):
    """Prints a list of words with all letters uppercased, only if the word starts with the given letters"""
    for i in lst:
        for j in starts_with:
            if i[0] == j:
                print(i.upper())

word_list = ["hello", "hey", "yo", "goodbye", "yes"]
print_upper_words(word_list, ['h', 'y'])
