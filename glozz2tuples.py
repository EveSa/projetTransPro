#Ce script permet de tranformer les fichiers issus de Glozz en dictionnaire/liste qui seront utilisés dans l'apprentissage automatique avec Spacy (https://spacy.io/usage/training#training-data)
# Pour finaliser l'apprentissage automatique, il faut faire le fichier init ... et le reste j'ai pas tout compris.

import re

#On ouvre le corpus annoté
corpus_xml=open("corpus_final_annote.xml.aa").read()
#Et le corpus non annoté
corpus=open("corpus_final_annote.txt.ac").read()

#On instancie les variables
paragraph_id={}
nex_key_assign={}

#On nettoie le texte et on le split selon </unit> ou </relation>
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
print(paragraph_id)

# Regarder dans quels paragaphes sont les annotations
##Utiliser un dictionnaire pour ajouter l'annotation pour la clé paragraphe

for unit in corpus_xml:
	if re.search(r"<unit.*?>.*?<type>(?!paragraph).*?</type>",unit) :	#?! ça veut dire "différent de". On cherche tous les noeuds "<unit>" qui contiennent "paragraph"
		print(unit)	

		#Petit trucs de test
		#(<featureSet>(<featurename="[A-z]+">[A-z]+</feature>)+?</featureSet>|<featureSet/>)
		#(r'<characterisation><type>([A-z]+)</type>.*?</characterisation><positioning><start><singlePositionindex="([0-9]+)"/></start><end><singlePositionindex="([0-9]+)"/></end></positioning>',unit)		
		#(r'<characterisation><type>(CatConditionsTravail)</type><featureSet/></characterisation><positioning><start><singlePositionindex="(3638)"/></start><end><singlePositionindex="(3658)"/></end></positioning>',unit)
		#

		#Et là, on récupère les infos
		m=re.search(r'<characterisation><type>([a-zA-Z0-9À-ž]+)<\/type>((<featureSet>((<featurename="[a-zA-Z0-9À-ž]+">([a-zA-Z0-9À-ž]+)<\/feature>)|(<featurename="[a-zA-Z0-9À-ž]+"\/>))+<\/featureSet>)|<featureSet\/)<\/characterisation><positioning><start><singlePositionindex="([0-9]+)"\/><\/start><end><singlePositionindex="([0-9]+)"\/><\/end><\/positioning>',unit)		
		print(m)
		#Le nom de l'entité
		en=m.group(1)
		#Son début dans le paragraphe (il me semble)
		start_EN=int(m.group(8))
		#Sa fin dans le paragraphe
		end_EN=int(m.group(9))
		print(en,start_EN,end_EN)

		# Et on met tout dans le dico
		for start,end in paragraph_id:
			if start_EN>start and end_EN<end :
				paragraph_id[(start,end)].append((start_EN-start,end_EN-start,en))

#Petits trucs de test encore
#print(paragraph_id)
#

#Entrer la string dans le dict
new_dic=dict([(nex_key_assign.get(key), value) for key, value in paragraph_id.items()])
# Faire une liste de tuples qui contiennent ("le paragraphe",[(start,end,EN),(...)])
docs=list(new_dic.items())


########### Ce qu'il reste à faire ################
# - les cas où la regex ne fonctionne pas
# - ajouter le texte du paragraphe dans le dictionnaire
# - vérifier que les index sont les bons pour les EN