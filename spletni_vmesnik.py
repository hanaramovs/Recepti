import bottle
import model


@bottle.get('/')
def index():
    return bottle.template(
        "views/base.tpl",
        ingredient_name = model.Ingredient.name,
        amount = model.Ingredient.amount,
        unit = model.Ingredient.unit,
        )




@bottle.get('/cookbook')
def index():
    return bottle.template("views/cookbook.tpl")    

@bottle.get('/recepie')
def index():
    return bottle.template("views/recepie.tpl")    


#to mora biti na dnu datoteke 
bottle.run(debug=True, host="localhost", reloader=True)