from typing import Final
'''
Solution au projet Usine de voiture.

Ce que vous allez voir est une des solutions possibles pour résoudre cet exercice.
'''


#Création de notre dictionnaire des couleurs (plusieurs possibilité pour régler ce problème)
couleurs = {
    'noir': 90,
    'rouge': 91,
    'vert': 92,
    'jaune': 93,
    'bleue': 94,
    'rose': 95,
    'cyan': 96,
}


#Création de la class Usine
class Usine:   #les parenthèses ne sont pas obligatoire quand la class n'est pas définie comme une class enfant.

    def __init__(self, modele: str, puissance: int, poid: float, couleur: str = 'noir'):  #fonction essentielle d'une class pour initialiser des variables qui hériteront des paramètres renseignés
        """
        *Mais pourquoi on ne choisirait pas un nom de variable plus facile à écrire pour aller plus vite ?*

        C'est une très bonne question que nous avons la. Choisir avec partimonie le nom de ses fonctions permet de
        retrouver plus facilement à quoi les servent, mais rien ne vous empêche de les nommées comme vous le voulez.
        Par ailleurs, si votre code est destiné à être réutilisé par un autre developer ou par vous dans plusieurs années,
        vous serez bien content d'avoir mis des noms explicites pour vous retrouver plus facilement x)
        """
        self.__modele : Final[str] = modele
        self.__puissance: Final[int] = puissance
        self.__poid: Final[float] = poid
        self.__couleur: Final[int] = self.convertir_couleur(couleur) #on appelle une fonction pour définir la variable

    def convertir_couleur(self, couleur: str) -> int:

        couleur = couleur.lower() #La fonction lower() permet de transformer tous les caractères majuscules en minuscules pour ne pas avoir de problème sur la casse

        if couleur in couleurs.keys():
            return couleurs[couleur]

        raise ValueError(f"La couleur {couleur} n'est pas disponible !") #renvoi une erreur si la couleur n'est pas disponnible


    def montrer_ressources(self) -> None:

        print(
            f"Vos caractéristiques de voiture :\n"
            f"Modèle : {self.__modele}\n"
            f"Puissance en chevaux : {self.__puissance}\n"
            f"Poid : {self.__poid} kg\n"
            f"Couleur : " +
            f"\033[{self.__couleur}m" +
            f"{self.__couleur}" +
            "\033[0m"
        )

    # On définit les propriétés
    @property
    def poid_(self) -> float:
        return self.__poid

    @property
    def puissance_(self) -> int:
        return self.__puissance

    @property
    def modele_(self) -> str:
        return self.__modele

    @property
    def couleur_(self) -> int:
        return self.__couleur


'''
Utilisation de cette class :

Imaginons que nous voulons 3 voitures différentes voulant sortir de l'usine
'''


voiture_1 = Usine(modele='Renaud', puissance=120, poid=1200) #première voiture définit sans couleur
voiture_2 = Usine(modele='Peugeot', puissance=90, poid=1050, couleur='vert')
voiture_3 = Usine(modele='Tesla', puissance=230, poid=1800, couleur='Cyan')

'''
Afficher les informations des 3 voitures :
'''

for voiture in (voiture_1, voiture_2, voiture_3): #on boucle sur les 3 voitures pour récupérer l'objet "Usine"

    print(f"Informations pour la voiture {voiture.modele_} :\n") #On utiliser la propriété "modele_" pour afficher uniquement le nom du modèle actuel de voiture
    voiture.montrer_ressources() #On montre toutes les ressources à partir d'un appel de fonction
    print("--------------------------------------------")








