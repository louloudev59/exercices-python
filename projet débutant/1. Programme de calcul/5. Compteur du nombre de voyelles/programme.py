# Voici un exemple de code répondant à la consigne

def nb_voyelles(phrase: str)->int:
    return sum(phrase.count(el) for el in "aeiou")
