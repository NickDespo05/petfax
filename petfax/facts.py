from flask import(Blueprint, render_template, request, redirect)
import json

pet_list = json.load(open("pets.json"))

bp = Blueprint("fact", __name__, url_prefix="/facts")

@bp.route("/", methods=['POST', "GET"])
def index():
   if request.method == "POST": 
      print(request.form)
      return redirect("/facts")
   else:
      return render_template("facts.html", pets=pet_list)
   
   return "this is the facts index"

