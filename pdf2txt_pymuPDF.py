import fitz,glob,re

pdf_files=glob.glob("corpus_final/*.pdf")
#On ouvre un fichier qui contiendra le résultat final
corpus_OCR = open('corpus_final.txt', 'w')
for pdf_file in pdf_files :
    print(pdf_file)
    file = fitz.open(pdf_file)
    for i,page in enumerate(file.pages(2)):
        if i == 0:
            text=page.get_text("blocks")
            for blocks in text :
                if blocks[0]>220 and blocks[1]>50 and blocks[3]<750 :
                    texte=re.sub("\n"," ",blocks[4])
                    texte=re.sub("- ","",texte)
                    corpus_OCR.write(texte)
        else :
            text=page.get_text("blocks")
            for blocks in text :
                if blocks[1]>50 and blocks[3]<750 :
                    texte=re.sub("\n"," ",blocks[4])
                    texte=re.sub("- ","",texte)
                    corpus_OCR.write(texte)
    corpus_OCR.write('\n==============================================\n')