from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from generate_letter import generer_lettre
import os

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

# Page principale
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            modele_sel = request.form["modele"]
titre_modele = modeles.get(modele_sel, modele_sel)
            champs = {
                "nom":   request.form["nom"],
                "date":  request.form["date"],
                "objet": request.form["objet"],
                "corps": request.form["corps"]
            }
 # Récupérer le sexe sélectionné dans le formulaire
            sexe = request.form.get("sexe")
            if sexe == "femme":
                civilite_signataire = "Madame"
            elif sexe == "homme":
                civilite_signataire = "Monsieur"
            else:
                civilite_signataire = ""

            champs["civilite_signataire"] = civilite_signataire

            if not all(champs.values()) or not civilite_signataire:
                flash("Veuillez remplir tous les champs et sélectionner le sexe.", "warning")
                return redirect(url_for("index"))

            if not all(champs.values()):
                flash("Veuillez remplir tous les champs.", "warning")
                return redirect(url_for("index"))

            nom_sortie = f"{champs['nom'].replace(' ', '_')}_{modele_sel}.docx"
            chemin = generer_lettre(f"{modele_sel}.docx", champs, nom_sortie)
                return send_file(chemin, as_attachment=True)
         except Exception as e:
            flash(f"Erreur : {e}", "danger")
                 return redirect(url_for("index"))

    # Pour l'affichage GET : liste des modèles disponibles
    modeles ={
    "autorisation_construire": "Demande d'autorisation de construire",
    "reponse_reclamation": "Réponse à une réclamation",
    "relance_pieces": "Relance pour pièces manquantes",
    "avis_defavorable": "Avis technique défavorable",
    "convocation_commission": "Convocation à une commission d’instruction"
}

    return render_template("index.html", modeles=modeles)

if __name__ == "__main__":
    if not os.path.isdir("output"):
        os.makedirs("output")
    app.run(debug=True)