# Voici un exemple de code répondant à la consigne
def nb_voyelles(mot: str):
    
    # Prise en compte des voyelles existantes dans une liste
    voyelles = ['a','e','o','u','i','y']
    # Compteur de voyelles initialisé à 0 par défaut
    counter = 0
    # On compte le nombre de fois où chaque voyelle apparaît dans le mot grâce à la méthode count
    for v in voyelles:
        counter += mot.count(v)
    return counter

if __name__ == "__main__":
    print(nb_voyelles("bonjour, comment allez-vous ?"))
    print(nb_voyelles("je vais à paris"))
    print(nb_voyelles("docstring"))
    print(nb_voyelles(""))