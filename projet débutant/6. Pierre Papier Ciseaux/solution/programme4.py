import random

points_joueur = 0
points_python = 0

def points():
    print("vous avez: ", points_joueur, "points et Python a : ", points_python, ("points"))
    
def checkStrContainsUpper(joueur):
    for x in joueur:
        if x == x.upper():
            return True
    return False


while True:
    joueur = input("Choissir entre pierre, papier ou ciseaux / quitter :  ")

    if checkStrContainsUpper(joueur) == True :
        print("Veuillez ne pas mettre de majuscules")
        break


    if joueur == "quitter":
        break 

    randomchoice = random.randint(1, 3)

    if randomchoice == 1 :
        Python = "pierre"

    elif randomchoice == 2:
        Python = "papier"

    else:
        Python ="ciseaux"

    if joueur == "pierre":
        print("Pierre /", Python)

    elif joueur == "ciseaux":
        print("Ciseaux /", Python)

    else:
        print("Papier /", Python)
    if Python == joueur:
        print("Match nul")
        points() 

    elif Python == "pierre" and joueur == "ciseaux":
        print("Vous avez perdu ! La pierre casse les ciseaux")
        points_python = points_python + 1
        points() 
    
    elif Python == "papier" and joueur == "ciseaux":
        print("Vous avez gagné! Les ciseaux coupent le papier")
        points_joueur = points_joueur + 1
        points() 

    elif Python == "ciseaux" and joueur == "pierre":
        print("Vous avez gagné ! La pierre casse les ciseaux ")
        points_joueur = points_joueur + 1
        points() 

    elif Python == "pierre" and joueur == "papier":
        print("Vous avez gagné! Le papier envellope la pierre")
        points_joueur = points_joueur + 1
        points() 

    elif Python == "ciseaux" and joueur == "papier":
        print("Vous avez perdu ! Les ciseaux coupent le papier")
        points_python = points_python + 1
        points()
    elif Python == "papier" and joueur =="pierre":
        print("Vous avez perdu! Le papier envellope la pierre")
        points_python = points_python + 1
        points() 

    if points_joueur == 3:
        print("Vous avez gagné la partie !")
        points()
        break 

    if points_python == 3:
        print("Vous avez perdu!")
        break 