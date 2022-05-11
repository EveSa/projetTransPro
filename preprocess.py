import spacy
from spacy.tokens import DocBin
from glozz2tuples import annotations

#On ouvre le corpus annoté
corpus_xml=open("corpus_final_annote.xml.aa").read()
#Et le corpus de référence
corpus=open("corpus_final_annote.txt.ac").read()

nlp = spacy.blank("fr")
training_data = annotations(corpus_xml,corpus)
# the DocBin will store the example documents
db = DocBin()
for text, annotation in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotation:
        span = doc.char_span(start, end, label=label)
        if span!=None :
            ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")
bytes_data = db.to_bytes()

print("done")

#On ouvre le corpus annoté
corpus_xml=open("annotation_Elie.aa").read()
#Et le corpus de référence
corpus=open("annotation_Elie.ac").read()

nlp = spacy.blank("fr")
training_data = annotations(corpus_xml,corpus)
# the DocBin will store the example documents
db = DocBin()
for text, annotation in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotation:
        span = doc.char_span(start, end, label=label)
        if span!=None :
            ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./dev.spacy")

print("done")

