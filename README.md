#### Tâches à realiser 
- convertir les pdf en txt
  - enlever les métadonnées
  - formatter le texte obtenu
- faire une convention pour les entités nommées
- diviser le corpus en 3 parties (il y a 31 textes, on fait 10 textes par parties ?)
  - trois partie : apprentissage, test et évalutation
  - critique : pourquoi ne pas faire la méthode par pli ?x
- annoter manuellement en EN une des parties du corpus ( préférablement toute annoter tous les textes pour le AIA)
- réaliser un automate / un programme qui reconnaît les EN
- les tester sur une deuxième partie du corpus 
- ajuster le programme /automate en fonction
- produire des résultats finaux sur la dernière partie du corpus avec rappel, précision et f-mesure et si possible les comparer avec un Accord inter Annotateur

***********
# Obtenir un corpus exploitable à partir de fichier pdf
## Convertir les pdf en format txt

La bibliothèque `pdfplumber`, qui utilise `pdfminer.six` la version adaptée de pdfminer pour python3, nous permet de réaliser l'OCR de l'ensemble du corpus automatiquement en itérant la requête sur tous les fichiers du dossier `corpus_final` fournit par les chercheuses avec une boucle `for`.
On essaie également une OCRisation avec la bibliothèque `pymuPDF` en bouclant avec la même méthode.

## Enlever les métadonnées 

## Formater le texte



# Annotation des information personelle avec Glozz

- age
- nom
- status
- endroit ou il travaille
Utiliser les étiquettes ESLO
- annoter distinctement les acteurs (verbe d'actions ?) et les témoins de transition (plus passif ?)

## Exemples

Laurent est conseiller immobilier. --> information perso, nom de métier
Laurent, conseiller immobilier --> information perso, nom de métier
D'après le conseiller immobilier, .... --> personne mentionnée, nom de métier

# Convertir la sortie Glozz pour quelle soit utilisable avec Spacy

Récupérer le texte du paragraphe, récupérer les EN quand elles sont comprises dans les bornes du paragraphes. Transformer le tout en un tuple contenant le texte du paragraphe et la liste des tuples contenants les EN.
Il faut également récupérer les relations.

# Analyse des résultats

## Matrice de confusion

### Pourquoi l'apprentissage à fait ces erreurs

## Rappel, Précision et F-mesure




# Organisation du travail

- 2 semaines pour l'OCRisation
  - utilisation de plusieurs logiciel différents 
  - intérêt des différentes méthodes
- 1 semaine pour l'annotation
- 1 semaine pour la conversion des données Glozz en Données pour Spacy
- Reprise de l'annotation après changement des conventions
- 1 semaine pour l'immplémentation de l'apprentissage automatique
- 1 semaine pour l'analyse des résultats

******************************************

# Soutenance

## Problémtique

## Le projet
### qu'est ce qu'on devrait faire

### quelles sont les conventions

### comment elles entrent dans le projet général

## Comment on 'la fait 
### annotation mannuelle/accord interanno/outil)
- Statiqtique sur les annotations manuelles (nb catégorie, ...)

### Annotation automatique (Unitex/Spacy)

## Evaluation de la detection
- On a pas déclarer tout ce qu'o a fait manuellement

## Conclusion critique des résultats

### Critiques 

- le peut de cohérence dans les annotations
  - On aurait préféré une catégorie typeDésignation dans CatPersonneMentionnée par exemple plutôt que Métier+Nom
  - On a décidé de ne pas utiliser la valeur "Nom" de Information personnelles pour éviter les confusions pour Spacy.
  - On pense qu'il serait nécéssaire de ajouter une valeur de "désignation collective" ou "désignation individuelle"
- On peut aussi se poser la question de la pertinence de l'annotation de toutes les coréférence du texte.

********************
Critère de notatino

- aisance à l'oral
- un dossier zippé
  - avec un document explicatif 
  - les scripts
  - ...
- organisation de travail
