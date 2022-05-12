import spacy
from spacy.tokens import DocBin
from spacy import displacy
colors={ "CatPersonneMentionnee.Oui.ActeurTransition":"#c0791b",
    "InformationsPersonnelles.M\u00e9tierAvant.M\u00e9tierAvant":"#8dd8d3",
    "InformationsPersonnelles.LieuDeTravail.Auncune":"#0b6374",
    "CatPersonneMentionnee.Non.ActeurTransition.Nom":"#fd5b58",
    "InformationsPersonnelles.M\u00e9tierApres.M\u00e9tierApres":"#599191",
    "InformationsPersonnelles.M\u00e9tier.M\u00e9tierAvant":"#d7e6a3",
    "CatPersonneMentionnee.Non.TemoinTransition.Nom":"#d558ab",
    "InformationsPersonnelles.M\u00e9tier.Auncune":"#27278b",
    "CatPersonneMentionnee.Non.ActeurTransition.NomDeM\u00e9tier":"#569cd6",
    "CatPersonneMentionnee.Non.ActeurTransition":"#9cdcfe",
    "CatPersonneMentionnee":"#d4d4d4",
    "InformationsPersonnelles.LieuDeTravail.PasActeurTransition":"#ce9178",
    "InformationsPersonnelles.Age.PasActeurTransition":"#c586c0",
    "InformationsPersonnelles.Age.Auncune":"#dcdcaa",
    "InformationsPersonnelles.LieuDeVie.PasActeurTransition":"#4ec9b0",
    "InformationsPersonnelles.LieuDeVie.Auncune":"#b5cea8"}
options = {"ents": ["CatPersonneMentionnee.Oui.ActeurTransition",
    "InformationsPersonnelles.M\u00e9tierAvant.M\u00e9tierAvant",
    "InformationsPersonnelles.LieuDeTravail.Auncune",
    "CatPersonneMentionnee.Non.ActeurTransition.Nom",
    "InformationsPersonnelles.M\u00e9tierApres.M\u00e9tierApres",
    "InformationsPersonnelles.M\u00e9tier.M\u00e9tierAvant",
    "CatPersonneMentionnee.Non.TemoinTransition.Nom",
    "InformationsPersonnelles.M\u00e9tier.Auncune",
    "CatPersonneMentionnee.Non.ActeurTransition.NomDeM\u00e9tier",
    "CatPersonneMentionnee.Non.ActeurTransition",
    "CatPersonneMentionnee",
    "InformationsPersonnelles.LieuDeTravail.PasActeurTransition",
    "InformationsPersonnelles.Age.PasActeurTransition",
    "InformationsPersonnelles.Age.Auncune",
    "InformationsPersonnelles.LieuDeVie.PasActeurTransition",
    "InformationsPersonnelles.LieuDeVie.Auncune"], "colors": colors}



trained_nlp=spacy.load('./models/output/model-best')

text = open("corpus_final_annote.txt").read()

#nlp = spacy.blank("fr")
#doc_bin = DocBin().from_disk("./train.spacy")
#docs = list(doc_bin.get_docs(nlp.vocab))

doc = trained_nlp(text)

for ent in doc.ents:
    print (ent.text, ent.label_)

displacy.serve(doc, style='ent',options=options)