
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <string>


#include "chiffrage.hpp"


using namespace std;

int main(int argc, char *argv[])
{
	srand((unsigned int)time(0));
	char choix('Z');
	int taille;
	cout << "Bienvenue dans le gestionnaire de mot de passe de Gatien" << endl;

	if (argc > 1 )
	{
		choix = *argv[1];
	}
	while (true)
	{
		if (choix == 'Z')
			cout << "Options:" << endl;
			cout << "[1] -> Generer un mot de passe" << endl;
			cout << "[2] -> Chiffrer mot de passe" << endl;
      cout << "[3] -> Dechiffrer mot de passe" << endl;
      cout << "[4] -> Ajouter des identifiants" << endl;
      cout << "[5] -> Lire des identifiants" << endl;
			cout << "[6] -> Quitter" << endl;
			cout << "Entrez votre choix :" << endl;
			cin >> choix;

		if (choix == '1')
		{
			cout << "Entrez la taille du mot de passe : ";
			cin >> taille;
			string mdp = genererMotDePasse(taille);
			cout << "Le mot de passe est : " << mdp;
		}
		else if (choix == '6')
		{
			return 0;
		}
		cout << endl << "---------------------" << endl;
		choix = 'Z';
	}
}
