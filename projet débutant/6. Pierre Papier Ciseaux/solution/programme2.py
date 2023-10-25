from random import choice

# déclaration des constantes
GAME_CHOICES = ["pierre", "papier", "ciseaux"]
DISPLAY_CHOICES = """
Ton choix 👉 {player_choice}
Mon choix 👉 {random_choice}
"""
WHY = {
    "papier_pierre": "Le papier enveloppe la pierre ❗",
    "ciseaux_papier": "Les ciseaux coupent le papier ❗",
    "ciseaux_pierre": "La pierre casse les ciseaux ❗"
}

# bla-bla-bla
print("\n💥Bienvenue dans le Jeu : Pierre, Papier, Ciseaux💥")
print("""Tu as le choix parmi ces 3 propositions :
la pierre, le papier ou les ciseaux
Tu dois écrire un seul mot en 🤜MINUSCULE🤛
""")

# début du jeu
running = True
while running:

    random_choice = choice(GAME_CHOICES)
    print("=-="*20+"\nJ'ai fait mon choix.\nA ton tour ...\n")

    # première fois que j'utilise l'opérateur walrus et c'est la première fois que j'en vois l'utilité
    while (player_choice := input("Ton choix ❓\n👉 ")) not in GAME_CHOICES:
        print(f"Choix incorrect.\nEntre un autre choix ou vérifie la syntaxe et recommence.")

    print(DISPLAY_CHOICES.format(player_choice=player_choice, random_choice=random_choice))

    if player_choice == random_choice:
        print("Egalité: Nous devons recommencer.\nPrêt ❓")
        # inutile de faire un "else", ça évite un niveau d'indentation supplémentaire, donc un "continue" suffit
        continue

    list_player_win = [
        player_choice == "pierre" and random_choice == "ciseaux",
        player_choice == "ciseaux" and random_choice == "papier",
        player_choice == "papier" and random_choice == "pierre"
    ]    # ci-dessous, je ne voulais pas faire deux choses :
    # - une structure conditionnelle à rallonge (les 3 conditions dans la liste ci-dessus sur la même ligne)
    # - une suite de "if" et "elif" avec à chaque fois "player_win = True"
    # donc j'ai opté pour une liste de test conditionnelle et une somme de cette liste
    player_win = False
    if sum(list_player_win):
        player_win = True

    result = "BRAVO 💯 Tu as gagné 💪" if player_win else "DOMMAGE ❗ Tu as perdu 👎"
    # j'ai opté pour un dictionnaire pour retourner les raisons de la victoire ou de la défaite
    # j'utilise comme clé les 2 réponses données triées par ordre alphabétique et séparé par "_"
    why = f"{min(player_choice, random_choice)}_{max(player_choice, random_choice)}"
    print(result, WHY[why])

    print("Le jeu est terminé.\n" + "=-="*20 + "\n")

    # deuxième fois que j'utilise walrus 😛
    while (answer := input("Veux-tu recommancer une partie ❓ Y/n ")) not in ["Y", "n"]:
        print("Mauvaise réponse, recommence ...")

    if answer == "n":
        running = False
        print("Merci 🤝\nA bientôt")
    else:
        print("COOL 💚\n")