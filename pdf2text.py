#On utilise pour l'OCR pdfminer.six qu'on peut installer avec la commande `pip install pdfminer.six`

from pdfminer.high_level import extract_text
import glob
import os

#On fait une liste des noms des fichiers à traiter
directory = glob.glob('corpus_final/*.pdf')

#On ouvre un fichier qui contiendra le résultat final
corpus_OCR = open('corpus_final.txt', 'w')

#On parcours les fichiers pour l'OCR
for file in directory :
    text = extract_text(file)
    text = text.replace("\n", " ")
    text = text.replace("-","")
    corpus_OCR.write(text)
    print('done')