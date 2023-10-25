from random import randint

BDD = {
    "element": ["papier", "pierre", "ciseaux"],
    "gagnant": ["10", "21", "02"],
    "phrase": [ "Le papier enveloppe la pierre", "Les ciseaux coupent le papier", "La pierre casse les ciseaux"]
}

while True:
    joueur = input("pierre, papier ou ciseaux: ")
    if (joueur in BDD["element"]):
        choix, joueur = randint(0, 2), BDD["element"].index(joueur)

        if choix != joueur: break
        print("Égalité, recommencez...")

    else: print("Faute de frappe !")

print(f'Vous avez {"gagné" if f"{choix}{joueur}" in BDD["gagnant"] else "perdu"} ! {BDD["phrase"][choix + joueur - 1]} !')