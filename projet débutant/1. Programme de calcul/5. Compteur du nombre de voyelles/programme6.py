def nb_voyelles(phrase: str) -> int:

    """Fonction permettant de compter le nombre de voyelles au sein d'une chaîne de caractères.

    Args:
        phrase (str):

        La chaîne de caractère peut contenir des majuscules et/ou des minuscules.
        Avec la fonction "lower" utilisée dans la structure conditionnelle, les majuscules ne seront pas comptées.
        En conséquence, une chaîne de caractères ne comportant que des majuscules sera considérée comme étant vide.

    Returns:
        int:

        Le chiffre 0 est retourné si une chaîne de caractères vide est passée comme argument lors de l'appel de la fonction.
        Le nombre de voyelles contenu dans l'argument est retourné si ce dernier comporte au moins un caractère.

    """
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"

    nb = (phrase.count(a) + phrase.count(e) + phrase.count(i) + phrase.count(o) + phrase.count(u))

    if phrase.lower() == "":
        return 0
    else:
        return nb