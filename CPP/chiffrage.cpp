#include <iostream>
#include <string>



using namespace std;

string genererMotDePasse(int taille)
{
	int chiffreA;
	char caracteres[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','@','#','%','$'};
	if (taille <= 0 )
		taille = 1;
	string resultat("");
	for (int i = 0; i < taille; i++)
	{
		chiffreA = rand() % 39 + 0;
		resultat += caracteres[chiffreA];
	}
	return resultat;

}

string chiffrer(string texte, int decalage)
{
    char caracteres[] = {'a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','0','1','2','3','4','5','6','7','8','9','.','@','#','%','$','!'};
    string resultat("");
    bool dansListe(false);
    for (int i = 0; i < texte.size(); i++)
    {
        dansListe = false;
        int indicateur = 0;
        for (int j = 0; j < 68-decalage; j++)
        {
            if (caracteres[j] == texte[i])
            {
                dansListe = true;
                indicateur = j;
            }
            if (dansListe)
            {
            resultat += caracteres[indicateur+decalage];
            break;
            }
        
        }
    }
    cout << endl << resultat << endl;
    return resultat;
}
