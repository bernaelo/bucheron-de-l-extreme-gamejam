import pickle as pk

##Permet de reset tout le fichier des scores (supprime les high scores donc WOLAH FAUT PAS Y TOUCHER)
#scores = []
#fichier = open("scores.txt","wb")
#pickled = pk.Pickler(fichier)
#pickled.dump(scores)
#fichier.close()

## Récupération des scores
with open("scores.txt", "rb") as fichier:  # Ouverture en binaire
    unpickled = pk.Unpickler(fichier)
    scores = unpickled.load()  # On récupère la variable
    fichier.close()
    print(scores)

# A supprimer quand on pourra récup le nb de buches dans la tour (le score)
nom = input("Prenom: ")
new_score = int(input("score: "))

##Verification des scores existants ou inexistants selon les noms
try:
    nom_list = [score[0] for score in scores]  # création de la liste des noms
    index = nom_list.index(nom)  # recherche du joueur
    # Si le joueur a un score:
    print("Le joueur {} a déjà un score. il est à l'index n°{} de la liste".format(name, index))
    if new_score > scores[index][1]:  # et que son nouveau score est mieux
        scores[index][1] = new_score
except ValueError:  # Si le joueur n'a pas de score précédent / index(nom) renvoie une ValueError si il trouve pas nom
    print("Le joueur n'a pas de scores précédents")
    scores.append([nom, new_score])  # Ajout du score
print(scores)

## Sauvegarde des scores
with open("scores.txt", "wb") as fichier:
    pickled = pk.Pickler(fichier)
    pickled.dump(scores)
    fichier.close()