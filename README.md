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

La bibliothèque `pdfplumber`, qui utilise `pdfminer.six` la version adaptée de pdfminer pour python3, nous permet de réaliser l'OCR de l'ensemble du corpus automatiquement en itérant la requête sur tous les fichiers du dossier `corpus_final` fournit par les chercheuses avec une boucle `for`.
On essaie également une OCRisation avec la bibliothèque `pymuPDF` en bouclant avec la même méthode.


******************************************

# <mark>Soutenance</mark>

## <mark> Problématique</mark>

Avec l'impact de la COVID-19 sur l'économie, les transitions professionnelles se sont faites plus courante. L'étude vise à rechercher l'influence des médias dans le changement de la perception des transitions professionnelles et les procédés à l'origine de ces modifications de connotations. Cette étude du domaine de la psychologie nécessite le concours du TAL : en effet, les chercheuses souhaitent analyser un nombre important de texte issus de la presse afin de pouvoir inférer des hypothèses. Nous avons donc été chargées d'analyser un corpus à l'aide des méthodes du TAL.

Nous devions mettre en place un modèle pour reconnaître automatiquement les transitions professionnelles dans les textes journalistiques.

Les 30 articles qui constituent ce corpus ont été récupérées dans la base de données 'Europresse' à l'aide d'une recherche full-text utilisant les expressions régulières.

## <mark> Le projet</mark>
### <mark>qu'est ce qu'on devait faire</mark>

À partir d'un corpus tirés d'articles de journaux et concernant la transition professionnelles au format pdf, nous devions mettre en place un modèle permettant de reconnaître automatiquement les acteurs des transitions ainsi que leurs informations personelles et leur métier avant et après la transition.

### <mark>quelles sont les conventions</mark>

CatPersonneMentionnee
- Enonciateur
  - Oui
  - Non
- TypePersonneMentionee
  - Acteur Transition
  - TemoinTransition
  - ActeurPotentielTransition
- NomDeMétier
  - NomDeMétier
  - Aucune
- Nom
  - Nom
  - Aucune

InformationsPersonnelles
- TypeInformation
  - Nom
  - Age
  - Métier
  - LieuDeVie
  - LieuDeTravail
  - Donnée Chiffrée
- MetiersSiActeurTransition 
  - MétierAvant
  - MétierApres
  - Aucune

Nous avons également annotés les relations mais elles n'ont pas été prise en compte dans notre modèle :
- coreference
- relationDonneeChiffree
- relationInformationsPersonnelles

### <mark>comment elles entrent dans le projet général</mark>

## <mark>Comment on l'a fait </mark>

### Organisation du travail

- 2 semaines pour l'OCRisation
  - utilisation de plusieurs logiciel différents 
  - intérêt des différentes méthodes
- 1 semaine pour l'annotation
- 1 semaine pour la conversion des données Glozz en Données pour Spacy
- Reprise de l'annotation après changement des conventions
- 1 semaine pour l'immplémentation de l'apprentissage automatique
- 1 semaine pour la visualisationd des résultats avec dislacy
- 1 semaine pour l'analyse des résultats

### <mark>annotation mannuelle/accord interanno/outil)</mark>
- <mark>Statiqtique sur les annotations manuelles (nb catégorie, ...)</mark>

#### Annotation des information personelle avec Glozz

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

### <mark>Annotation automatique (Unitex/Spacy)</mark>

#### Initialiser le fichier de configuration du modèle

En suivant les consignes disponible sur la documentation de [SpaCy](https://spacy.io/usage/training) et ce [site-web](https://ner.pythonhumanities.com/03_02_train_spacy_ner_model.html) qui contient également des informations intéressantes.
Le fichier de configuration rassemble toutes les données nécéssaire à l'apprentissage du modèle. Il est le seul fichier à être appelé avec la commande `spacy train`.
Il faut donc au moment de la création du fichier de configuration choisir la partition du corpus et l'utilisation ou non d'un pretraining (qui ne nécéssite pas d'annotation, juste un texte brut)

On doit également initialiser les labels avec `python -m spacy init labels config.cfg ./corpus `

`config.cfg`

#### Convertir la sortie Glozz pour quelle soit utilisable avec Spacy

Récupérer le texte du paragraphe, récupérer les EN quand elles sont comprises dans les bornes du paragraphes. Transformer le tout en un tuple contenant le texte du paragraphe et la liste des tuples contenants les EN.

`glozz2tuples.py`

#### Entrainement d'un modèle Spacy

La ligne de commande qui permet de voir un résultat :

  `python3 -m spacy train config.cfg --output ./models/output`

## <mark>Evaluation de la detection</mark>
- <mark>On a pas déclarer tout ce qu'o a fait manuellement</mark>

### Analyse des résultats

#### Matrice de confusion

#### Pourquoi l'apprentissage à fait ces erreurs

#### Rappel, Précision et F-mesure

## <mark>Conclusion critique des résultats</mark>

### Critiques 

- le peut de cohérence dans les annotations
  - On aurait préféré une catégorie typeDésignation dans CatPersonneMentionnée par exemple plutôt que Métier+Nom
  - On a décidé de ne pas utiliser la valeur "Nom" de Information personnelles pour éviter les confusions pour Spacy.
  - On pense qu'il serait nécéssaire de ajouter une valeur de "désignation collective" ou "désignation individuelle"
- On peut aussi se poser la question de la pertinence de l'annotation de toutes les coréférence du texte.

********************

Critère de notatino

- aisance à l'oral
  - 20-25min oral
  - 15 min de question
- un dossier zippé
  - avec un document explicatif 
  - les scripts
  - ...
- organisation de travail
