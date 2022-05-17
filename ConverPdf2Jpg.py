from pdf2image import convert_from_path
import glob
import os

#On rentre dans le dossier qui contiendra toutes les photos
os.chdir('corpus_final_jpg')
workPath=os.getcwd() #On stocke la valeur du path dans une variable car on y revient souvent

#On fait une liste des noms des fichiers à traiter
directory = glob.glob('./corpus_final/*.pdf')

#On parcours les fichiers pour la conversion
for file in directory :
    name=file[16:-4] #On enlève la partie 'corpus_final/' et '.pdf' 
    print(name) #vérification du nom
    new_dir=os.path.join(workPath,name) #On determine un nom de répertoire qui contiendra les pages sous forme d'image
    print(new_dir) #varification du nom
    if not os.path.exists(new_dir): #On crée le répertoire s'il n'existe pas
        os.mkdir(new_dir)
        print('done') #vérification de l'accomplissement
    os.chdir(new_dir) #On rentre dans ce nouveau dossier
    pages = convert_from_path('../'+file, 72) #On utilise la méthode 'convert_from_path' de pdf2img avec une résolution de 72 ce qui correspond à la résolutino des pdf après traitement de pdfplumber
    i=0 #On initialise un compteur pour le nom des pages
    for page in pages:
        i +=1
        page.save('page'+str(i)+'.jpg', 'JPEG') #On enregistre les pages avec ce nouveau nom
    os.chdir(workPath) #On retourne dans el répertoire d'origine