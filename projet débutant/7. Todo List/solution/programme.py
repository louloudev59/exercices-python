# Voici un exemple de code répondant à la consigne

import os

# Vérifier si le fichier de sauvegarde existe
if os.path.exists("taches.txt"):
    with open("taches.txt", "r") as fichier:
        lignes = fichier.readlines()
        taches = {}
        for index, ligne in enumerate(lignes):
            taches[index + 1] = ligne.strip()
else:
    taches = {}

def ajouter_tache(taches):
    tache = input("Entrez la tâche à ajouter : ")
    taches[len(taches) + 1] = tache
    print(f"Tâche '{tache}' ajoutée.")
    sauvegarder_taches(taches)

def supprimer_tache(taches):
    tache_id = int(input("Entrez l'ID de la tâche à supprimer : "))
    if tache_id in taches:
        tache_supprimee = taches.pop(tache_id)
        print(f"Tâche '{tache_supprimee}' supprimée.")
        sauvegarder_taches(taches)
    else:
        print("ID de tâche invalide.")

def afficher_taches(taches):
    if not taches:
        print("Aucune tâche enregistrée.")
    else:
        print("Liste des tâches :")
        for tache_id, tache in taches.items():
            print(f"{tache_id}. {tache}")
    sauvegarder_taches(taches)

def sauvegarder_taches(taches):
    with open("taches.txt", "w") as fichier:
        for tache_id, tache in taches.items():
            fichier.write(f"{tache}\n")
    print("Tâches sauvegardées dans 'taches.txt'.")

while True:
    print("Gestionnaire de Tâches")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Afficher les tâches")
    print("4. Quitter")

    choix = input("Choisis une option : ")

    if choix == "1":
        ajouter_tache(taches)
    elif choix == "2":
        supprimer_tache(taches)
    elif choix == "3":
        afficher_taches(taches)
    elif choix == "4":
        print("Merci d'avoir utilisé le gestionnaire de tâches.")
        break
    else:
        print("Option invalide. Réessaie.")