from chiffrage import *
from fichier import *

import sys

choix = 0
if len(sys.argv) > 1:
    choix = int(sys.argv[1])


print("Bienvenue dans le gestionnaire de mot de passe ")
print("-----------------------------------------------")

while True:
    if choix == 0:
        print("[1] -> Mot de passe aléatoire")
        print("[2] -> Chiffrer mot de passe")
        print("[3] -> Dechiffrer mot de passe")
        print("[4] -> Ajouter des identifiants")
        print("[5] -> Lire des identifiants")
        print("[6] -> Sortir")
        choix = int(input("\nVotre choix : "))


    if choix == 1:
        nombre = int(input("Entrez la taille du mot de passe \n"))
        print("\nMot de passe -> {}".format(genererMotDePasse(nombre)))


    elif choix == 2:
        achiffrer = input("Entrez le texte à chiffrer \n")
        print("\nTexte chiffré -> {}".format(chiffrer(achiffrer)))


    elif choix == 3:
        adechiffrer = input("Entrez le texte à dechiffrer \n")
        print("\nTexte déchiffré -> {}".format(dechiffrer(adechiffrer)))


    elif choix == 4:
        site = input("Entrez le nom du site \n")
        email = input("Entrez l email \n")
        mdp = input("Entrez le mot de passe \n")
        if ajouterIdentifiants(site, email, mdp) == 0:
            print("Ajout réussi !")
        else:
            print("Erreur")


    elif choix == 5:
        site = input("Entrez le nom du site \n")
        resultat = lireIdentifiant(site)
        if len(resultat) > 0:
            for identifiants in resultat:
                print("\nResultat:")
                print(identifiants[0] + " : " + identifiants[1])
        else:
            print("La recherche n a pas abouti")

    elif choix == 6:
        exit(0)

    print("\n")
    choix = 0
