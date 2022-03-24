#On utilise pour l'OCR pdfminer.six qu'on peut installer avec la commande `pip install pdfminer.six`

from pdfminer.high_level import extract_text
import glob
import os

#On fait une liste des noms des fichiers à traiter
direct = glob.glob('corpus_final/*.pdf')

#On ouvre un fichier qui contiendra le résultat final
corpus_OCR = open('corpus_final.txt', 'w')

#On parcours les fichiers pour l'OCR
for file in direct :
    text = extract_text(file)
    corpus_OCR.write(text)
    print('done')