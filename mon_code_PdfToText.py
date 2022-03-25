# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:04:32 2022

@author: Estelle Salmon
"""
# =============================================================================
# # on importe les modules nécessaires
# import PyPDF2
# 
# # ouverture binary mdoe pour lecture
# objetFichierPDF = open(r'C:\Users\estel\Documents\M1_TAL\stage\pdfToText\enrichissementCorpus.pdf','rb')
# 
# # création d'un objet reader de pdf
# pdfReader = PyPDF2.PdfFileReader(objetFichierPDF)
# 
# # on imprime le nombre de pages du document pdf
# print(pdfReader.numPages)
# 
# 
# for page in pdfReader.pages:
#     print(page.extractText())
# 
# # creation d'un objet page
# #objetPage = pdfReader.getPage(0)
# 
# 
# # extraction du texte de la page
# #print(objetPage.extractText())
# 
# # on ferme l'objet fichier pdf
# objetFichierPDF.close()
# =============================================================================


import re 
import pdfplumber
pdf = pdfplumber.open(r'C:\Users\estel\Documents\M1_TAL\stage\pdfToText\mon_code\article.pdf')
#page = pdf.pages[2]
nbPagesPdf = len(pdf.pages)

page = pdf.pages[2]
# page 1 titre 
bounding_box_page1_titre = (220,100,612,200)
boite_page1_boxTitre = page.crop(bounding_box_page1_titre, relative=False)
# page 1 box 1
bounding_box_page1_box1 = (220,220,400,750)
boite_page1_box1 = page.crop(bounding_box_page1_box1, relative=False)
# page 1 box 2
bounding_box_page1_box2 = (400,200,612,750)
boite_page1_box2 = page.crop(bounding_box_page1_box2, relative=False)
    
mots_page1_box1 = boite_page1_box1.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
mots_page1_box2 = boite_page1_box2.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
mots_page1_boxTitre = boite_page1_boxTitre.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
    
    
liste=[]


#### PAGE 1 #######
for i in range(len(mots_page1_boxTitre)):
    occurrence = mots_page1_boxTitre[i]
    # parcours des elements du dico
    for k,v in occurrence.items():
        if k == 'text':
            liste.append(v)
liste.append("\n")
            
sous_liste = []
for i in range(len(mots_page1_box1)):
    occurrence = mots_page1_box1[i]
    # parcours des elements du dico
    for k,v in occurrence.items():
        if k == 'text':
            sous_liste.append(v)

# on traite le premier mot de l'article avec la lettre majuscule
premierMot = sous_liste[0] + sous_liste[1]
sous_liste[0] = premierMot
del sous_liste[1] 
liste = liste + sous_liste
print(liste)
    
for i in range(len(mots_page1_box2)):
    occurrence = mots_page1_box2[i]
    # parcours des elements du dico
    for k,v in occurrence.items():
        if k == 'text':
            liste.append(v)
            
            
            
# boucle pour le reste des pages
for i in range(3,nbPagesPdf):
    page = pdf.pages[i]
    
    
    # autres pages box 1
    bounding_box_autrePage_box1 = (50,50,220,750)
    boite_autrePage_box1 = page.crop(bounding_box_autrePage_box1, relative=False)
    # autres pages box 2
    bounding_box_autrePage_box2 = (220,50,400,750)
    boite_autrePage_box2 = page.crop(bounding_box_autrePage_box2, relative=False)
    # autres pages box 3
    bounding_box_autrePage_box3 = (400,50,610,750)
    boite_autrePage_box3 = page.crop(bounding_box_autrePage_box3, relative=False)
    
    # marche pour les espaces
    # .extractText
   
    mots_autrePage_box1 = boite_autrePage_box1.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
    mots_autrePage_box2 = boite_autrePage_box2.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
    mots_autrePage_box3 = boite_autrePage_box3.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True, use_text_flow=False, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[])
    

    # on vérifie la segmentation - les mots avec les espaces avec la méthode au dessus pour ajouter les paramètres 
    # parcours de la liste qui contient les dicos avec les infos
    
    #### AUTRES PAGES #####
    for i in range(len(mots_autrePage_box1)):
        occurrence = mots_autrePage_box1[i]
        # parcours des elements du dico
        for k,v in occurrence.items():
            if k == 'text':
                liste.append(v)
                
    for i in range(len(mots_autrePage_box2)):
        occurrence = mots_autrePage_box2[i]
        # parcours des elements du dico
        for k,v in occurrence.items():
            if k == 'text':
                liste.append(v)
                
    for i in range(len(mots_autrePage_box3)):
        occurrence = mots_autrePage_box3[i]
        # parcours des elements du dico
        for k,v in occurrence.items():
            if k == 'text':
                liste.append(v)

#print(liste)
  
# =============================================================================
# [re.sub("(.*)-",r"\1",token) for token in liste]
#     
# =============================================================================
#print(liste)
# =============================================================================
# for token in liste :
#     token = re.sub("-$","",token)
#     print(token)
#     liste.append(token)
# =============================================================================

            

# boucle pour écrire dans fichier avec espaces en plus des token
with open(r'C:\Users\estel\Documents\M1_TAL\stage\pdfToText\mon_code\article.txt','w', encoding="utf-8") as out:
    for token, next_token in zip(liste, liste[1:]): 
        #print(token,"+++", next_token)
        if token.endswith("-") and re.match(r"^[a-z]+", next_token):
            sansTiret = re.sub(r"-$","",token)    
            out.write(sansTiret)
            print(token,"%%%", next_token)
        elif token.endswith("-") and re.match(r"^[A-Z]+", next_token):
            sansTiretMaj = re.sub(r"-$", "-",token)
            out.write(sansTiretMaj)
            print(token, "6666666", next_token)
        # ici on gère l'espace (qui doit être supprimé) qui a été inséré après le retour à la ligne à la fin du titre
        elif token == "\n" :
            out.write(token)
        else :
            out.write(token)
            out.write(" ")
    
   

      
 
    
    
    
# =============================================================================
# with open (r'C:\Users\estel\Documents\M1_TAL\stage\pdfToText\mon_code\article.txt','r', encoding="utf-8") as post_traitement:
#     pourModif = post_traitement.readlines()
#     re.sub("-\s", "")
# =============================================================================
    
    
# on va venir mettre chaque mot dans une liste avec des espaces entre chaque mot
# on fait ça pour chaque boite de chaque page de chaque document 


# gérer les - entre deux mots (tiret suivi d'un espace à supprimer)
# pb pour Saint Louis > indice MAJ
# première lettre de première page à coller aux autres

# titre sur ligne 1 
# texte sur ligne 2

#for i in range(len(mots)):
    #print(mots[i])


pdf.close()


# ça prend les trucs de la fin "cet article est paru + lien"


# titre articles parfois très long > taille bloc article et autres blocs en fonction de la position de la première lettre du texte

# =============================================================================
# from PyPDF2 import PdfFileWriter, PdfFileReader
# 
# output = PdfFileWriter() 
# input = PdfFileReader(open('test.pdf', 'rb')) 
# 
# n = input.getNumPages()
# 
# for i in range(n):
#   page = input.getPage(i)
#   page.cropBox.upperLeft = (100,200)
#   page.cropBox.lowerRight = (300,400)
#   output.addPage(page) 
#   
# outputStream = open('result.pdf','wb') 
# output.write(outputStream) 
# outputStream.close()
# =============================================================================

