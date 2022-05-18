#pip install pdfminer.six`
import pdfminer
from pdfminer.high_level import extract_text
import glob

directory = glob.glob('corpus_final/*.pdf') #on garde dans une liste tous les noms de pdf
corpus_OCR = open('corpus_final_pdfminerpy.txt', 'w') #on ouvre le fichier final

for file in directory : #pour chaque pdf dans le dossier
    print(f"On traite : {file}") #on écrit la phase de traitement dans le terminal
    text = extract_text(file) #on extrait le texte du pdf
    text = text.replace("\n", " ") #on remplace les sauts de ligne par un espace
    text = text.replace("-","") #on remplace les tirets pour les mots sur deux lignes par rien (ex: heureu-sement)
    corpus_OCR.write(text) #on écrit le texte dans le fichier txt final