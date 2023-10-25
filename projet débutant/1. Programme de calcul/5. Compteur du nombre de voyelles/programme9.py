import time

phrase = input("entrez une phrase ou un mot, n'importe la/lequel/elle:  ")

minuscule = phrase.lower

print("Laissez moi vous dire combien il y a de voyelles dans votre phrase/mot")

compteur = 0
listedesvoyelles = ["i","e","a","u","o"]

for caractères in phrase:
    if caractères in listedesvoyelles:
        compteur = compteur+1
        time.sleep(2)

print ("Le nombre de voyelles dans votre phrase/mot est de :", compteur )