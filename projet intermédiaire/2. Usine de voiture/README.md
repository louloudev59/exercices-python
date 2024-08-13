# Usine de voiture

## Introduction
Bienvenue dans ce projet où vous allez fabriquer une "usine de voiture" en s'aidant d'une class. Il s'agit d'un niveau intermédiaire qui peut être réalisé par des débutants si la notion de class est acquise.

## Instructions
Suivez les étapes ci-dessous pour réaliser ce projet :

1. **Class usine** : créer une class `Usine` prenant en paramètre les informations suivantes :
    - Le modèle (en `str`)
    - La couleur (en `str` et par défaut vaut `noir`)
    - La puissance (en `int` qui représentera les chevaux)
    - Le poid (en `float` en kg)

2. **Conversion du format `str` de la couleur** : à parti du texte fournit par l'utilisateur à l'initialisation de la class, convertir le texte en un nombre de 90 à 96 à partir des séquences d'échappement ANSI.

3. **Afficher individuellement les caractéristiques** : à partir de propriétés, créer 4 propriétés servant à afficher dans la console la propriété demandé. (pour la couleur, il faut un affichage en couleur dans la console)

4. **Afficher les caractéristiques** : à partir d'une fonction, afficher l'intégralité des caractéristiques de la voiture.

5. **Essayer le code** : Faites 3 configurations de voiture ayant des caractéristiques différentes et affichez les comme dans l'exemple ci-dessous

## Exemple
<img src="Exemple/Capture d'écran 2024-08-13 151016.png" alt="Exemple rendu">

## Indices
Pour afficher un text en couleur dans la console, vous pouvez utiliser le format suivant :
`\033[...m`

Vous devez remplacer les `...` par un nombre pour afficher une couleur. (Vous pouvez vous amuser à remplacer ce nombre par un nombre random pour voir le résultat)
Si vous renseignez `0`, les modifications reprendrons leur état par défaut.

Ex : 
```python Exemple\Couleur.py```

Ce fichier "README.md" sert de guide pour les utilisateurs qui souhaitent participer à votre projet en créant ce programme d'usine de voiture. Vous pouvez le personnaliser davantage en fonction de vos besoins.