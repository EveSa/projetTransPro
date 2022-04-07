# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:04:32 2022

@author: Estelle Salmon

Modification : Eve Sauvage

Commentaires : Elisabeth Savatier
"""
# =============================================================================

import re
# Afin d'utiliser pdfplumber --> pip install pdfplumber
import pdfplumber
import glob
from RecoBordureBoite import getBoundingBox

#On fait une liste des noms des fichiers à traiter
directory = glob.glob('corpus_final/*.pdf')
# directory = glob.glob('corpus_final/Apräs la pandÇmie, une envie de reconversion professionnelle.pdf')    #On peut commencer par un seul fichier pour vérifier que le code fonctionne bien

#On ouvre un fichier qui contiendra le résultat final
corpus_final = open('corpus_final_versionPDFplumber.txt', 'w')

#On parcours les fichiers pour l'OCR
for file in directory :
    print(file)
    pdf = pdfplumber.open(file)
    nbPagesPdf = len(pdf.pages)

    boundingbox_test = getBoundingBox('corpus_final_jpg'+file[12:-4]+'/page3.jpg') #On obtient une liste de tuples contenant les bordures des boîtes qui ont été marquée en vert dans le fichier jpg
    print(boundingbox_test)
    print(boundingbox_test[-1])
    #page où l'article débute véritablement (page 3 du pdf)
    page = pdf.pages[2]

    ## Création des boîtes contenant le texte qui nous intéresse ##

    # page 1 article titre/chapô
    bounding_box_page1_titre = boundingbox_test[-1] #écart gauche, haut, droit, bas de la boite titre/chapô dans la page
    boite_page1_boxTitre = page.crop(bounding_box_page1_titre, relative=False) #on récupère la boîte titre dans la page
    # page 1 article colonne gauche
    bounding_box_page1_box1 = boundingbox_test[0]
    boite_page1_box1 = page.crop(bounding_box_page1_box1, relative=True) #relative=True permet de décaler le haut de la boite en fonction de la taille du titre et du chapô
    # page 1 article colonne droite
    bounding_box_page1_box2 = boundingbox_test[1]
    boite_page1_box2 = page.crop(bounding_box_page1_box2, relative=True)


## Récupération du texte de chaque boîte sous forme de dictionnaire ##

#x_tolérance = écart entre les mots d'une même ligne; y_tolerance = écart des mots entre les lignes; keep_blank_chars = l'espace fait partie intégrante du mot; 
#use_text_flow = utilise-t-on une analyse automatique pour gérer les écarts entre les mots et les lignes à la place de x et y tolerance?; horizontal_ltr = lit-on de gauche à droite?;
#vertical_ttb = lit-on de haut en bas?; extra_attrs = veut-on seulement extraire les mots qui ont des attributs (font, size) particuliers?
    mots_page1_box1 = boite_page1_box1.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
    mots_page1_box2 = boite_page1_box2.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
    mots_page1_boxTitre = boite_page1_boxTitre.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])


    #### PAGE 1 ####

    ## Ecriture du titre dans une liste ##

    liste=[]
    #### PAGE 1 #######
    for i in range(len(mots_page1_boxTitre)):
        occurrence = mots_page1_boxTitre[i] #récupération de chaque élément du dictionnaire (ils contiennent le type de l'élément, son contenu et la position de ce dernier en pixel dans le texte)
        # extraction des mots de chaque élément du dictionnaire
        for k,v in occurrence.items():
            if k == 'text': #si l'élément est un texte alors on extrait son contenu
                liste.append(v)
    liste.append("\n")
 
## Ecriture de la colonne gauche dans une liste ## 
 
    sous_liste = []
    for i in range(len(mots_page1_box1)):
        occurrence = mots_page1_box1[i]
        # extraction des mots de chaque élément du dictionnaire
        for k,v in occurrence.items():
            if k == 'text':
                sous_liste.append(v)

 ## Traitement de la lettre majuscule du premier mot de l'article ##

    premierMot = sous_liste[0] + sous_liste[1] #première lettre + le reste du mot
    sous_liste[0] = premierMot #on remplace la première lettre dans sous_liste[0] par le mot en entier
    del sous_liste[1] #on supprime la sous_liste[1] qui contenait le mot sans sa 1ère lettre
    liste = liste + sous_liste #titre + 1ère colonne
    
## Ecriture de la colonne droite dans une liste ## 

    for i in range(len(mots_page1_box2)):
        occurrence = mots_page1_box2[i]
        # extraction des mots de chaque élément du dictionnaire
        for k,v in occurrence.items():
            if k == 'text':
                liste.append(v)

                       
#### LES AUTRES PAGES ####

    # =========================================#
    # boucle pour le reste des pages
    #==========================================#
    for i in range(3,nbPagesPdf): #on commence la boucle sur la 4ème page
        page = pdf.pages[i]

    ## Création des boîtes contenant le texte qui nous intéresse ##

        # autres pages colonne gauche
        bounding_box_autrePage_box1 = (50,50,220,750) #(x0, top, x1, bottom)
        boite_autrePage_box1 = page.crop(bounding_box_autrePage_box1, relative=False)
        # autres pages colonne du milieu
        bounding_box_autrePage_box2 = (220,50,400,750)
        boite_autrePage_box2 = page.crop(bounding_box_autrePage_box2, relative=False)
        # autres pages colonne droite
        bounding_box_autrePage_box3 = (400,50,610,750)
        boite_autrePage_box3 = page.crop(bounding_box_autrePage_box3, relative=False)

        ## Récupération du texte de chaque boîte sous forme de dictionnaire ##
    
        mots_autrePage_box1 = boite_autrePage_box1.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
        mots_autrePage_box2 = boite_autrePage_box2.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
        mots_autrePage_box3 = boite_autrePage_box3.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])

    ## Ecriture de la colonne gauche dans une liste ## 

        for i in range(len(mots_autrePage_box1)):
            occurrence = mots_autrePage_box1[i]
            # extraction des mots de chaque élément du dictionnaire
            for k,v in occurrence.items():
                if k == 'text':
                    liste.append(v)
            
    ## Ecriture de la colonne du milieu dans une liste ## 

        for i in range(len(mots_autrePage_box2)):
            occurrence = mots_autrePage_box2[i]
            # extraction des mots de chaque élément du dictionnaire
            for k,v in occurrence.items():
                if k == 'text':
                    liste.append(v)
                                   
    ## Ecriture de la colonne droite dans une liste ## 

        for i in range(len(mots_autrePage_box3)):
            occurrence = mots_autrePage_box3[i]
            # extraction des mots de chaque élément du dictionnaire
            for k,v in occurrence.items():
                if k == 'text':
                    liste.append(v)


#### ECRITURE DE LA LISTE DANS UN FICHIER DE SORTIE ####

    # boucle pour écrire dans fichier avec espaces en plus des token
    for token, next_token in zip(liste, liste[1:]): #on affiche les bigrammes de la liste avec zip()
        #on enlève les mots de type "forma- tion"
        if token.endswith("-") and re.match(r"^[a-z]+", next_token):
            sansTiret = re.sub(r"-$","",token)
            corpus_final.write(sansTiret)
        #on enlève les mots de type "- L'étude"
        elif token.endswith("-") and re.match(r"^[A-Z]+", next_token):
            sansTiretMaj = re.sub(r"-$", "-",token)
            corpus_final.write(sansTiretMaj)
        #on garde les sauts de lignes
        elif token == "\n" :
            print(token)
            corpus_final.write(token)
        #on garde les espaces
        else :
            corpus_final.write(token)
            corpus_final.write(" ")
    corpus_final.write(liste[-1]) #écriture du dernier mot de la liste (qui n'est pas pris en compte par [1:])

    corpus_final.write("\n\n________________________________________________________________\n\n")
    print(file ,'done')

#### FERMETURE DES PDF ####


pdf.close()
corpus_final.close()