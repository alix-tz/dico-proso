from flask import render_template
from ..app import app
from ..modeles.donnees import Person
from ..modeles.utilisateurs import User


@app.route("/")
def debut():

    return "Hello"

@app.route("/index")
def index():
    """
    Route qui affiche la liste des personnes (Nom, prenom) de la base.
    """
    personnes = Person.query.order_by(Person.person_id).limit(5).all()
    return render_template("pages/index.html", personnes=personnes)




