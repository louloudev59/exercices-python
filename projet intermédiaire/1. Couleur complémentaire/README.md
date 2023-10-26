# Couleur Complémentaire

## Introduction
Bienvenue dans ce projet amusant où vous allez travailler avec les couleurs pour trouver la couleur complémentaire d'une couleur donnée. Il s'agit d'un défi de niveau intermédiaire qui peut être réalisé par des débutants en s'aidant de bibliothèques.

## Instructions
Suivez les étapes ci-dessous pour réaliser ce projet :

1. **Conversion de Couleur**: Créez une fonction `get_color_types(color: str) -> dict` qui convertit le format RVB hexadécimal d'une couleur en plusieurs formats, y compris RVB décimal et TSL (Teinte, Saturation, Luminosité). Le dictionnaire résultant devra contenir les éléments suivants :
   - `hex`: Valeur hexadécimale de la couleur passée en paramètre.
   - `rvb`: Liste des valeurs RVB de la couleur en décimal.
   - `tsl_norm`: Tuple contenant les valeurs TSL (Teinte en degrés 360°, Saturation en %, Luminosité en %).
   - `tsl`: Tuple contenant les valeurs TSL au format [0-1] (float).

2. **Affichage des Résultats**: Affichez le contenu du dictionnaire retourné par la fonction `get_color_types` dans la console.

3. **Couleur Complémentaire**: Créez une fonction `get_complementary(color: str) -> str` pour trouver la couleur complémentaire de la couleur passée en paramètre, et retournez cette couleur au format hexadécimal.

## Conditions
- Les valeurs hexadécimales sont précédées de "#" et les lettres sont en minuscules.
- L'affichage des résultats se fait via la console.

## Exemples
Voici quelques exemples de résultats possibles :

- `get_color_types("#19021e")` retourne **{'hex': '#19021e', 'rvb': [25, 2, 30], 'tsl_norm': ('289°', '88%', '6%'), 'tsl': (0.8035714285714285, 0.875, 0.06274509803921569)}**
- `get_complementary("#19021e")` retourne **"#071e02"**

## Ressources
Pour effectuer des tests, vous pouvez utiliser des outils en ligne tels que [colorpicker](https://colorpicker.me/). N'hésitez pas à consulter des ressources en ligne pour vous aider.

## Indices
Voici quelques indices pour vous aider, mais attention aux spoilers :

- Le nombre hexadécimal d'une couleur représente les valeurs Rouge, Vert et Bleu codées en 6 chiffres hexadécimaux. Les 2 premiers correspondent à la couleur rouge, les 2 suivants au vert et les 2 derniers au bleu. Pour convertir cette valeur hexadécimale en décimal, vous devez convertir chaque paire de chiffres.

- La bibliothèque `colorsys` peut vous aider à réaliser les conversions. En particulier, les fonctions `colorsys.rgb_to_hls` et `colorsys.hls_to_rgb` peuvent être utiles.

- Pour trouver la couleur complémentaire, il faut passer par le format TSL, en faisant une rotation de 180° sur la teinte. Pour faire cette rotation, vous devez normaliser la valeur de la teinte TSL, qui est généralement [0, 1] en [0°, 360°], puis ajouter 180°.

Bonne programmation !

Ce fichier "README.md" sert de guide pour les utilisateurs qui souhaitent participer à votre projet en créant ce programme de couleur complémentaire. Vous pouvez le personnaliser davantage en fonction de vos besoins.

