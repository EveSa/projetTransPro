#pip install opencv-python
#python3 -c "import cv2"

import cv2
import numpy as np
import glob
import os

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    "--- Cette fonction permet de faire apparaître les images à une taille spécifique pour ne pas sortir de l'écran ---"
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

#=========================#
def getBoundingBox(jpgFile):
    " Cette fonction retourne la liste des tuple contenant les bords droit, haut, gauche et bas des boîtes marquées en vert dans le fichier jpg donné en argument "
    print(jpgFile) #Vérification du nom du fichier

    image = cv2.imread(jpgFile) #On ouvre l'image avec cv2

    #image = ResizeWithAspectRatio(image, width=900)  #Si besoin il y a de faire apparaître les images

    #=== convert to hsv ===#
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #saturation qui permet de faire ressortir des débuts de bloc
    #===On applique un masque pour ne reconnaître que les parties qui sont en vert (dont le code RGB est entre (36, 25, 25) et (70, 255,255))===#
    mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

    #=== On peut faire apparaître l'image si besoin ===#
    #cv2.imshow("green.png", mask)
    #cv2.waitKey(0)                     # !!!!!!! Il faut appuyer sur n'importe quelle touche du clavier pour sortir

    #=== Finding Contours ===#
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #On récupère les contours

    #print("Contours found= ", str(contours), '\n')     #Pour vérification si besoin

    #=== Draw all contours ===# Pour afficher si besoin
    # -1 signifies drawing all contours#
    #cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    #cv2.imshow('Contours', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


    #=== Récupérer les cases sous forme de tuples ===#
    boundingBoxes=[] #On initialize une liste vide qui contiendra les tuples des contours de la page traitée
    for array in contours : #Les coordonnées sont d'abord sous forme de numpy array
        X = [] #On initialise les listes qui contiendrons les coordonnées X et Y
        Y = []
        if len(array)>= 4 : #On veut éviter les contours qui ne sont pas des rectangles
            for coord in array : #Pour chaques matrices contenues dans la matrice "array"
                X.append(coord[0,0]) #On récupère la valeur de la première colonne du vecteur                
                Y.append(coord[0,1]) #On récupère la valeur de la deuxième colonne du vecteur
            
            ### On a parfois des objet plus grand que des rectangles : pour les tranformer en rectangle, on prend les 4 extrémités (donc les min et les max des coordonnées X et Y)
            x0=min(X)
            top=min(Y)
            x1=max(X)
            bottom=max(Y)
            #On écrit ensuite ces donnnées sous forme de tuple dans une nouvelle variable
            boundingbox=(x0, top, x1, bottom)
            #et on ajoute de nouveau tuple à la liste des limites de boite de la page traitée
            boundingBoxes.append(boundingbox)
    
    return (boundingBoxes)
