import fitz,glob,re

pdf_files=glob.glob("corpus_final/*.pdf") #liste de tout les pdf à océriser
corpus_OCR = open('corpus_final.txt', 'w') #On ouvre un fichier qui contiendra le résultat final
testo = open ("testooo.txt",'w')

for pdf_file in pdf_files :
    print(f"On traite : {pdf_file}")
    file = fitz.open(pdf_file) #on ouvre le pdf avec le module d'océrisatione

    for i,page in enumerate(file.pages(2)): #i est le compteur, on commence à la page 3
        
        if i == 0: #si c'est la 1ere page qu'on traite (donc la page 3)
            text=page.get_text("blocks") #on génère des listes de blocs de texte (paragraphes)
            for blocks in text : #pour chaque bloc dans la liste text 
                #block : (x0, y0 ==> point supérieur gauche; x1, y1 => point supérieur droit; le texte contenu dans ce rectangle; le numéro du bloc dans la liste de bloc; image ou non avec 1 ou 0)
                if blocks[0]>220 and blocks[1]>50 and blocks[3]<750 : #si c'est les blocs qui ne sont pas la bande à gauche dans le pdf et pas la bande du bas du pdf
                    texte=re.sub("\n"," ",blocks[4]) #on enlève les éléments qui marquent le saut de ligne dans le texte du bloc
                    texte=re.sub("- ","",texte) #on enlève les éléments de type "heureu(retour à la ligne)-sement" dans le texte du bloc
                    corpus_OCR.write(texte)

        else : #pour les autres pages qui ont la même pagination
            text=page.get_text("blocks") #on génère des listes de blocs de texte (paragraphes)
            for blocks in text : #pour chaque bloc dans la liste text 
                if blocks[1]>50 and blocks[3]<750 : #si c'est les blocs pas dans la bande du bas du pdf
                    texte=re.sub("\n"," ",blocks[4]) #on enlève les éléments qui marquent le saut de ligne dans le texte du bloc
                    texte=re.sub("- ","",texte) #on enlève les éléments de type "heureu(retour à la ligne)-sement" dans le texte du bloc
                    corpus_OCR.write(texte)
    corpus_OCR.write('\n==============================================\n')