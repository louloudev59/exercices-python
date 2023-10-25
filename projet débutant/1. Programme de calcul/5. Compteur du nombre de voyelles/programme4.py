def nb_voyelles(phrase: str) -> int:
    return sum(phrase.lower().count(voyelle) for voyelle in "aeiou")