import random

# Choix
CHOICES = ["pierre", "papier", "ciseaux"]

# Boucle de jeu
while True:
    # Choix aléatoire de l'ordi
    random_choice = random.choice(CHOICES)
    # Demander à l'utilisateur
    choice = input("pierre, papier ou ciseaux ? ==> ")
    while choice not in CHOICES:
        print("choix non valide")
        choice = input("pierre, papier ou ciseaux ? ==> ")
    # Résolution
    if random_choice == "pierre" and choice == "papier":
        print("Vous avez gagné ! le papier enveloppe la pierre")
        break
    elif random_choice == "papier" and choice == "ciseaux":
        print("Vous avez gagné ! Les ciseaux coupent le papier")
        break
    elif random_choice == "ciseaux" and choice == "pierre":
        print("Gagné ! La pierre éclate les ciseaux")
    elif random_choice == choice:
        print("Egalité ! Recommencez...")
    else:
        print(f"Vous avez perdu ! {random_choice} gagne sur {choice}")
        break