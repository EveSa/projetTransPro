import spacy
from spacy.tokens import DocBin
from spacy import displacy

text = open("corpus_final_annote.txt").read()

#nlp=spacy.load(path)

nlp = spacy.blank("fr")
doc_bin = DocBin().from_disk("./train.spacy")
docs = list(doc_bin.get_docs(nlp.vocab))

doc = nlp(text)
displacy.serve(doc, style="ent")