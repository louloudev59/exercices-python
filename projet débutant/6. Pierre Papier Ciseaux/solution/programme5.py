# Voici un exemple de code répondant à la consigne
from random import choice


propositions = ['pierre', 'papier', 'ciseaux']
victoires = {'pierre':'papier', 'papier':'ciseaux', 'ciseaux':'pierre'}
defaites = {'pierre':'ciseaux', 'papier':'pierre', 'ciseaux':'papier'}

phrases_victoire = {'pierre':'La pierre écrase les ciseaux !', 'papier':'Le papier enveloppe la pierre !', 'ciseaux':'Les ciseaux coupent le papier !'}


def tour_joueur():
    choix = input('Que choisissez vous ? | pierre/papier/ciseaux | ')
    while choix not in propositions:
        choix = input('Veuillez choisir une option valide ! | pierre/papier/ciseaux | ')
    return choix

def tour_ennemi():
    return choice(propositions)

while True:
    choix_ennemi = tour_ennemi()
    choix_joueur = tour_joueur()
    print(f'Votre adversaire a choisi : {choix_ennemi}')
    if victoires[choix_ennemi] == choix_joueur:
        print('Bravo, vous avez gagné ! ' + phrases_victoire[choix_joueur])
        break
    elif defaites[choix_ennemi] == choix_joueur:
        print('Dommage, vous avez perdu ! ' + phrases_victoire[choix_ennemi])
        break
    else:
        print(f'Hmmm... {choix_joueur} contre {choix_ennemi} est une égalité, il faut rejouer !')