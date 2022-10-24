from flask import(Blueprint, render_template)
import json

pet_list = json.load(open("pets.json"))

bp = Blueprint("fact", __name__, url_prefix="/facts")

@bp.route("/")
def index():
   return render_template("facts.html", pets=pet_list)