import os
from os import listdir
import re

os.chdir("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//")
buf = ["-", "-", "-", "-", "-"]
buf2 = ["-", "-", "-"]
buf3 = []
with open("annotationEvalFinale.xml", "w") as annotationFinale :
    for fichier in listdir("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//glozz//") :
        if fichier.endswith(".aa") :
            with open("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//glozz//" +fichier, encoding="utf-8") as annotationaa : 
                for ligne in annotationaa :
                    buf.pop(0)
                    categorie = re.match("</featureSet>", ligne)
                    if categorie :
                        buf.append("</featureSet>")
                    else : 
                        buf.append("non")
                    if buf2[0] != "-" :
                        positionend = re.match('<singlePosition index="([^<]+?)"/>', ligne)
                        print(positionend.group(1))
                        buf3.append(int(positionend.group(1)))
                        buf2.pop(0)
                        buf2.append("-")
                    elif buf2[1] != "-" or buf2[2] != "-" :
                        buf2.pop(0)
                        buf2.append("-")
                    if '</featureSet>' in buf[0] :
                        positionstart = re.match('<singlePosition index="([^<]+?)"/>', ligne)
                        if positionstart : 
                            buf2.pop(0)
                            buf2.append(positionstart.group(1))
                            buf3.append(int(positionstart.group(1)))
                            print(positionstart.group(1))
                    if len(buf3) == 2 :
                        with open("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//corpus_final.txt", encoding="utf-8") as pdfs :
                            mots = []
                            lettres = []
                            for ligne in pdfs :
                                lettres += list(ligne)
                                remplacement = "".join(lettres[buf3[0]:buf3[1]])
                        print(remplacement)
                        buf3.pop(0)
                        buf3.pop(0)
                        annotationFinale.write(f'<singlePosition index="{remplacement}"/>')
                    search1 = re.match("<start>", ligne)
                    search2 = re.match("</start>", ligne)
                    search3 = re.match("<end>", ligne)
                    search4 = re.match("</end>", ligne)
                    search5 = re.match(r"<singlePosition.*", ligne)
                    if search1 == None and search2 == None and search3 == None and search4 == None and search5 == None :
                        annotationFinale.write(ligne)