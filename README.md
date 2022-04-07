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



# Annotation des information personelle

- age
- nom
- status
- endroit ou il travaille
Utiliser les étiquettes ESLO
- annoter distinctement les acteurs (verbe d'actions ?) et les témoins de transition (plus passif ?)
