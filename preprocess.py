import spacy
from spacy.tokens import DocBin
from glozz2tuples import annotations

#On ouvre le corpus annoté
corpus_xml=open("corpus_final_annote.xml.aa").read()
#Et le corpus non annoté
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
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")