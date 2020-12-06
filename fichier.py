from chiffrage import *

def ajouterIdentifiants(site, email, mdp):
    fichier = open("ressources.txt", "a")
    fichier.write("\n" + chiffrer(site) + " - " + chiffrer(email) + " - " + chiffrer(mdp))
    fichier.close()
    return 0

def lireIdentifiant(site):
    resultat = []
    fichier = open("ressources.txt", "r")
    for ligne in fichier:
        a = ligne.split(" - ")
        if dechiffrer(a[0]) == site:
            b = []
            b.append(dechiffrer(a[1]))
            b.append(dechiffrer(a[2]))
            resultat.append(b)
    fichier.close()
    return resultat
