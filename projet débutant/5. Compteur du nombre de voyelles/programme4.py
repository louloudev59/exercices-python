# Voici un exemple de code répondant à la consigne

def nb_voyelles(phrase: str) -> int:
    return sum(phrase.lower().count(voyelle) for voyelle in "aeiou")