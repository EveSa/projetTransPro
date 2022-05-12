import spacy
from spacy.tokens import DocBin
from spacy import displacy

trained_nlp=spacy.load('./models/output/model-best')

text = open("corpus_final_annote.txt").read()

#nlp = spacy.blank("fr")
#doc_bin = DocBin().from_disk("./train.spacy")
#docs = list(doc_bin.get_docs(nlp.vocab))

doc = trained_nlp(text)

for ent in doc.ents:
    print (ent.text, ent.label_)

displacy.serve(doc, style="ent")