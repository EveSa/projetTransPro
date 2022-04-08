import os
from os import listdir
import re

os.chdir("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//")
#on va utiliser la technique des buffers pour avoir le contexte avant (histoire de prendre les bons index)
buf = ["-", "-", "-", "-", "-"] #contexte pour l'indice de début de mot
buf2 = ["-", "-", "-"] #contexte pour l'indice de fin de mmot
buf3 = [] #liste de l'indice de début de mot et fin de mot
with open("annotationEvalFinale.xml", "w") as annotationFinale :
    for fichier in listdir("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//glozz//") :
        if fichier.endswith(".aa") :
            with open("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//glozz//" +fichier, encoding="utf-8") as annotationaa : 
                for ligne in annotationaa :
                    #on vérifie que les lignes que l'on ne veut pas ne soit pas écrite
                    if buf2[0] == "-" and buf2[1] == "-" and buf2[2] == "-" and '</featureSet>' not in buf[0] and '</featureSet>' not in buf[1]  and '</featureSet>' not in buf[2] :
                        annotationFinale.write(ligne)
                    buf.pop(0)
                    categorie = re.match("</featureSet>", ligne)
                    if categorie :
                        buf.append("</featureSet>") #on va ajouter la fin du featureSet qui nous permet de savoir que l'index qui suit doit être enregistré (c'est l'index de début de mot)
                    else : 
                        buf.append("non") #ça permet de décaler le buffer dans le texte
                    if buf2[0] != "-" : #si le contexte est au bon endroit on attrape l'index de fin de mot
                        positionend = re.match('<singlePosition index="([^<]+?)"/>', ligne)
                        print(positionend.group(1))
                        buf3.append(int(positionend.group(1))) #ajout de l'index de fin de mot dans la liste
                        buf2.pop(0) 
                        buf2.append("-") #on décale le buffer2 dans le texte
                    elif buf2[1] != "-" or buf2[2] != "-" :
                        buf2.pop(0)
                        buf2.append("-") #on décale le buffer2 dans le texte
                    if '</featureSet>' in buf[0] : # selon le buffer on est à la ligne de l'index; l'utilisation du contexte nous évite un problème au niveau du None de match
                        positionstart = re.match('<singlePosition index="([^<]+?)"/>', ligne)
                        buf2.pop(0)
                        buf2.append(positionstart.group(1)) #on décale le buffer2 dans le texte
                        buf3.append(int(positionstart.group(1))) #ajout dans le buffer2 de la position du début du mot à extraire du texte des corpus
                        print(positionstart.group(1))
                    if len(buf3) == 2 : #si on a le début et la fin du mot à extraire on le fait
                        with open("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//corpus_final.txt", encoding="utf-8") as pdfs :
                            mots = []
                            lettres = []
                            for ligne in pdfs :
                                lettres += list(ligne) #on fait une liste de chaque lettre du texte 
                                remplacement = "".join(lettres[buf3[0]:buf3[1]]) #on joint les lettres pour créer le mot final qui remplacera les index de position de mots dans le fichier xml
                        print(remplacement)
                        buf3.pop(0)
                        buf3.pop(0)
                        annotationFinale.write(f'<singlePosition index="{remplacement}"/>')

#### PROBLEMES
#1. Les mots sortis des index="" sont pas les bons --> peut-être un problème au niveau de l'extraction du texte lettre par lettre? (genre il prend pas les caractères non printable?)
