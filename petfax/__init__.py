from flask import Flask

def create_app():
   app = Flask(__name__)

   @app.route('/')
   def hello():
      return "Hello Petfax"

   from . import pet
   app.register_blueprint(pet.bp) 

   from . import facts
   app.register_blueprint(facts.bp)

   return app




"""
ex:

@app.route('/thing/<int = thingId>', methods("GET", "POST"))
def thing (thingId):
   return thingId

"""