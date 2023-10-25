def nb_voyelles(phrase):
    phrase.lower()
    if len(phrase) == 0:
        return 0
    else:
        return phrase.count('a') + phrase.count('e') + phrase.count('i') + phrase.count('o') + phrase.count('u')

print(nb_voyelles(""))