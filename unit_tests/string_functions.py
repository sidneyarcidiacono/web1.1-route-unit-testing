"""Functions to manipulate strings."""


def greet_by_name(name):
    """Return a greeting to the given person."""
    try:
        greeting = "Hello, " + name + "!"
        return greeting
    except (ValueError):
        return "Invalid input"


def reverse(str):
    """Reverses the characters in a string."""
    return str[::-1]


def reverse_words(str):
    """Reverses the letters in each word of a string."""
    words = str.split()
    new_words = reverse(words[0])
    for word in words[1:]:
        new_words += " " + reverse(word)
    return new_words


def sarcastic(str):
    """ReTuRn tHe SaRcAsTiC vErSiOn Of A sTrInG."""
    new_string = ""
    capitalize = True
    for letter in str:
        if letter.isalpha():
            new_string += letter.upper() if capitalize else letter.lower()
            capitalize = not capitalize
        else:
            new_string += letter
    return new_string


def find_longest_word(sentence):
    """Return the longest word in a sentence."""
    try:
        words_list = sentence.split()
        print(words_list)
        longest_word = words_list[0]
        for word in words_list:
            if len(word) > len(longest_word):
                longest_word = word
        return word
    except (IndexError):
        return "Invalid input"


def return_list(items):
    """Take in items and return items as a list."""
    items_list = []
    if items:
        split_items = items.split(" ")
        for thing in split_items:
            items_list.append(thing)
        return items_list
    else:
        return "Please supply some items"
