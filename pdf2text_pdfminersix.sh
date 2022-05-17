#!usr/bin/bash

#echo pip install pdfminer

#utilisation : #bash ./pdf2text_pdfminersix.sh ./corpus_final

dossier=$1 #on récupère le dossier où on va extraire les pdf
SAVEIFS=$IFS #comme les dossiers ont des espaces on change la variable de la boucle qui reconnait les noms de fichier par l'espace
IFS=$(echo -en "\n\b")
for fichier in $(ls $dossier); do #pour chaque fichier dans le dossier
    echo "on traite le fichier : $fichier" #on écrit dans le terminal à quel phase de traitement nous en sommes
    pdf2txt.py $dossier/$fichier >> ./corpus_final_pdminersix.txt  #on utilise pdfminersix sur le fichier et on écrit le résultat dans le fichier txt final
done
IFS=$SAVEIFS
exit
