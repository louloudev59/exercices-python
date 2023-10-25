def nb_voyelles(phrase):
    VOWELS = ["a", "e", "i", "o", "u"]
    i = 0
    for letter in phrase:
        if letter in VOWELS:
            i += 1
    return i