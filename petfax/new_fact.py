from flask import (Blueprint, render_template)
import json
pets_list = json.load(open("pets.json"))

bp = Blueprint("new_fact", __name__, url_prefix='/facts/new')

@bp.route("/")
def index():
   return render_template("new_fact.html", pets=pets_list)