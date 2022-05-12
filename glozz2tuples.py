#Ce script permet de tranformer les fichiers issus de Glozz en dictionnaire/liste qui seront utilisés dans l'apprentissage automatique avec Spacy (https://spacy.io/usage/training#training-data)
# Pour finaliser l'apprentissage automatique, il faut faire le fichier init ... et le reste j'ai pas tout compris.

import re

### OUVERTURE DES FICHIERS DE DONNÉES ###

# Ouverture du corpus annoté
corpus_xml=open("corpus_final_annote.xml.aa").read()
# Ouverture du corpus de référence
corpus=open("corpus_final_annote.txt.ac").read()

# Pour vérification de la sortie, on peut ajouter l'ouverture d'un fichier output
#fichier_sortie=open("fichier_sortie.txt", 'w')


### COEUR DU PROGRAMME ###

# On fait du programme une fonction pour pourvoir l'appeler dans notre programme `preprocess.py`
def annotations(corpus_xml,corpus):

	# On instancie des dictionnaires qui recupèrent les données
	paragraph_id={}
	nex_key_assign={}

	# On nettoie le texte et on le split selon </unit> ou </relation>
	corpus_xml=re.sub(r"\n|(\t)+|( )+","",corpus_xml)
	corpus_xml=re.split(r"</unit>|</relation>",corpus_xml)

	# Chercher les début et les fins des paragraphes
	for unit in corpus_xml:
		if re.search(r"<unit.*?>.*?<type>paragraph</type>",unit) :		
			m=re.search(r'<start><singlePositionindex="([0-9]+)"/></start><end><singlePositionindex="([0-9]+)"/></end>',unit)
			#On récupère les index de début et de fin
			start,end=int(m.group(1)),int(m.group(2))	
			#On stocke les infos dans un dic	
			paragraph_id[(start,end)]=[]
			para=corpus[start:end]
			#ça c'est pas pour tout de suite en fait
			if not re.search(r"====",para) :
				nex_key_assign[(start,end)]=para
	#fichier_sortie.write(str(nex_key_assign.items()))


	# Regarder dans quels paragaphes sont les annotations
	##Utiliser un dictionnaire pour ajouter l'annotation pour la clé paragraphe

	for unit in corpus_xml:
		if re.search(r"<unit.*?>.*?<type>(?!paragraph).*?</type>",unit) :	#?! ça veut dire "différent de". On cherche tous les noeuds "<unit>" qui contiennent "paragraph"
			

			#Et là, on récupère les infos
			m=re.search(r'<characterisation><type>([a-zA-Z0-9À-ž]+)<\/type>((<featureSet>((<featurename="[a-zA-Z0-9À-ž]+">([a-zA-Z0-9À-ž]+)<\/feature>)|(<featurename="[a-zA-Z0-9À-ž]+"\/>))+<\/featureSet>)|<featureSet\/)<\/characterisation><positioning><start><singlePositionindex="([0-9]+)"\/><\/start><end><singlePositionindex="([0-9]+)"\/><\/end><\/positioning>',unit)		
			
			#Le nom de l'entité
			en=m.group(1)
			#Son début dans le paragraphe
			start_EN=int(m.group(8))
			#Sa fin dans le paragraphe
			end_EN=int(m.group(9))

			# Et on met tout dans le dico
			for start,end in paragraph_id:
				if start_EN>start and end_EN<end :
					paragraph_id[(start,end)].append((start_EN-start,end_EN-start,en))

	#Petits trucs de test encore
	#print(paragraph_id)
	#
	### IMPLEMENTATION DU DICTIONNAIRE FINAL ###
	dic_final={}
	#Entrer la string dans le dict
	for key, value in paragraph_id.items():
		#Permet d'enlever les erreurs ou le paragraph ne serait pas reconnu
		if nex_key_assign.get(key)==None:
			continue
		# Permet d'enlever toutes les valeurs de paragraph qui ne sont en fait pas annotés
		if value != [] :
			dic_final[nex_key_assign.get(key)]=value
	#print(dic_final)

	# Transformation du dictionnaire en liste pour bien répondre au format d'entrée de SpaCy

	docs=list(dic_final.items())
	#print(docs)

	return docs


training_data = annotations(corpus_xml,corpus)
# Si on laisse le print, il sera lu dans `preprocess`
#print(training_data)



	########### Ce qu'il reste à faire ################
	# - ajouter un findall pour trouver toutes les caractéristiques de l'EN