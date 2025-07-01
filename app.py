from flask import Flask, render_template, request, send_file
from generate_letter import generer_lettre  # Assure-toi que ce nom est correct
import os

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nom = request.form["nom"]
        date = request.form["date"]
        objet = request.form["objet"]
        corps = request.form["corps"]
        
        champs = {
            "nom": nom,
            "date": date,
            "objet": objet,
            "corps": corps
        }
        
        nom_fichier = f"{nom.replace(' ', '_')}_lettre.docx"
        chemin = generer_lettre("modeles/convocation.docx", champs, nom_fichier)
        
        return send_file(chemin, as_attachment=True)
    
    return render_template("index.html")

if _name_ == "_main_":
    app.run(debug=True)