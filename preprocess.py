import spacy
from spacy.tokens import DocBin
import os

os.chdir("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2")
from glozz2tuples import annotations

#On ouvre le corpus annoté
corpus_xml=open("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//glozz//annotation.aa", encoding="utf-8").read()
#Et le corpus de référence
corpus=open("C://Users//elisa//Downloads//Enrichissement de corpus//Projet-2//glozz//annotation.ac", encoding="utf-8").read()

nlp = spacy.blank("fr")
training_data = annotations(corpus_xml,corpus)
# the DocBin will store the example documents
db = DocBin()
for text, annotation in training_data:
    print(text)
    print(annotation)
    doc = nlp(text)
    ents = []
    for start, end, label in annotation:
        span = doc.char_span(start, end, label=label)
        if span!=None :
            ents.append(span)
        print(ents)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")