from docx import Document
import os

def charger_modele(nom_fichier):
    chemin = os.path.join("modeles", nom_fichier)
    return Document(chemin)

def remplacer_balises(document, champs):
    for paragraphe in document.paragraphs:
        for cle, valeur in champs.items():
            if f"{{{{{cle}}}}}" in paragraphe.text:
                for run in paragraphe.runs:
                    run.text = run.text.replace(f"{{{{{cle}}}}}", valeur)
    return document

def generer_lettre(nom_modele, champs, nom_sortie):
    doc = charger_modele(nom_modele)
    doc = remplacer_balises(doc, champs)
    
    if not os.path.exists("output"):
        os.makedirs("output")
        
    chemin_sortie = os.path.join("output", nom_sortie)
    doc.save(chemin_sortie)
    return chemin_sortie