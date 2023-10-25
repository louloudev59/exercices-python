# Voici un exemple de code répondant à la consigne
def nb_voyelles(phrase: str) -> int:
    
    return sum(True for char in phrase if char in "aeiou")