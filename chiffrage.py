from random import randint

def genererMotDePasse(taille):
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','@','#','%','$']
    resultat = ""
    for i in range(taille):
        lettreAleatoire = caracteres[randint(0,len(caracteres)-1)]
        if randint(0,1) == 0:
            lettreAleatoire = lettreAleatoire.upper()
        resultat += lettreAleatoire
    return resultat

def chiffrer(texte, decalage=4):
    # Decalage ]0;4]
    caracteres = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','0','1','2','3','4','5','6','7','8','9','@','#','%','$']
    resultat = ""
    for lettre in texte:
        dansListe = False
        for x in range(len(caracteres)-decalage):
            if caracteres[x] == lettre:
                dansListe = True
                break
        if dansListe:
            resultat += caracteres[x+decalage]
        else:
            resultat += "---"
    return resultat

def dechiffrer(texte, decalage=4):
    caracteres = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','0','1','2','3','4','5','6','7','8','9','@','#','%','$']
    resultat = ""
    for lettre in texte:
        dansListe = False
        for x in range(len(caracteres)):
            if caracteres[x] == lettre:
                dansListe = True
                break
        if dansListe:
            resultat += caracteres[x-decalage]
        else:
            resultat += "---"
    return resultat
