from chiffrage import *

import sys

print("Bienvenue dans le gestionnaire de mot de passe ")
print("-----------------------------------------------")

choix = 0

if len(sys.argv) > 1:
    choix = int(sys.argv[1])

while True:
    if choix == 0:
        print("[1] -> Mot de passe aléatoire")
        print("[2] -> Chiffrer mot de passe")
        print("[3] -> Dechiffrer mot de passe")
        print("[4] -> Sortir")
        choix = int(input("Votre choix : "))

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
        exit(0)

    print("\n")
    choix = 0

print("Merci de votre utilisation")
