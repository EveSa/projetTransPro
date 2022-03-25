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

La bibliothèque `pdfminer.six`, version adaptée de pdfminer pour python3, nous permet de réaliser l'OCR de l'ensemble du corpus automatiquement en itérant la requête sur tous les fichiers du dossier `corpus_final` fournit par les chercheuses avec une boucle `for`.

## Enlever les métadonnées 

## Formater le texte

l'OCRisation se fait dans ce sens là :
corpus_final/Quand la crise bouscules les horizons pro.pdf
corpus_final/Un quart des Français prêt à changer de métier pour avoir un autre cadre de vie.pdf
corpus_final/Coronavirus  Æ Je n'Çtais plus Ö ma place Ø... Apräs laˇpandÇmie, le boom desˇreconversions vers lesˇmÇtiersˇdu bien-àtre.pdf
corpus_final/Ecoeures par le systeme ces soignants quittent l hopital.pdf
corpus_final/Ils quittent leur job pour se lancer dans l artisanat.pdf
corpus_final/simple1.pdf
corpus_final/Reconversion Voici le top 5 des mÇtiers les plus recherchÇs. LaˇcriseˇsanitaireˇaccÇläre les envies deˇchangement.pdf
corpus_final/Temoignage coach pro-Changer de métier-du reve a la realite.pdf
corpus_final/62% des 25-34 ans envisagent sÇrieusement de se reconvertir.pdf
corpus_final/Une reconversion dans l'immobilier.pdf
corpus_final/Temoignage-ras le bol de la routine.pdf
corpus_final/Ce metier je l'aimais mais ce n etait plus acceptable.pdf
corpus_final/Temoignages de jeunes ds l'aero en recvrsion.pdf
corpus_final/Lesˇreconversionsˇprofessionnelles, vÇritable enjeu des prochaines annÇes.pdf
corpus_final/j ai retrouve une utilite sociale.pdf
corpus_final/Les sous-traitants sur le carreau.pdf
corpus_final/d infirmier a videaste.pdf
corpus_final/LeˇCovidˇpousse Ö laˇreconversionˇprofessionnelle.pdf
corpus_final/Temoignage D’aide-soignant à homme toutes mains en auto-entreprise.pdf
corpus_final/Covid-19  Ces soignants qui rendent leur blouse.pdf
corpus_final/Covid 19. Changer de job face Ö la crise, pas si simple.pdf
corpus_final/Leur nouvelle vie aupräs des morts.pdf
corpus_final/Des profils varies se cotoient à l'ecole de Crepes.pdf
corpus_final/Ces signes Çvidents qui prouvent qu'il estˇurgentˇdeˇchangerˇdeˇmÇtier.pdf
corpus_final/Ces ingÇnieurs qui changent de cap.pdf
corpus_final/∑ GuerlÇdan, ilsˇchangent de vieˇprofessionnelleˇapräs la crise duˇCovid.pdf
corpus_final/LeˇCovidˇaccÇlÇrateur desˇreconversions et d'un nouveau rapport auˇtravail.pdf
corpus_final/Milleniaux envisagent de se reconvertir.pdf
corpus_final/Avec la crise, ils veulent changer de mÇtier.pdf
corpus_final/Covidˇ les Franáais ont soif deˇreconversionˇprofessionnelle.pdf
corpus_final/Coronavirus  Laˇcriseˇsanitaireˇa accÇlÇrÇ les envies deˇreconversionˇprofessionnelle.pdf
corpus_final/Apräs la pandÇmie, une envie de reconversion professionnelle.pdf


# Annotation des information personelle

- age
- nom
- status
- endroit ou il travaille
Utiliser les étiquettes ESLO
- annoter distinctement les acteurs (verbe d'actions ?) et les témoins de transition (plus passif ?)
