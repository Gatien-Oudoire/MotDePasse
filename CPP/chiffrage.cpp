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
