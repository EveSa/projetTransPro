# projetTransPro

## Conventions : 

CatPersonneMentionnee : 
- Enonciateur : oui/non
- TypePersonneMentionnee : ActeurTransition/TemoinTransition/ActeurPotentielTransition
- NomDeMétier : NomDeMétier/Aucune
- Nom : Nom/Aucune

InformationsPersonnelles : 
- TypeInformation : Nom --> On ne l'utilise pas/Age/Métier/LieuDeVie/LieuDeTravail/Donnée chiffrée
- MetiersSiActeurTransition : MétierAvant/MétierApres/Aucune

Relations : 
- coreference
- relationDonneeChiffree
- relationInformationsPersonnelles

On annote les pronoms aussi --> Personne mentionné et aucun dans nom et métier

Laurent est conseiller immobilier. --> information perso, nom de métier
Laurent, conseiller immobilier --> information perso, nom de métier
D'après le conseiller immobilier, .... --> personne mentionnée, nom de métier