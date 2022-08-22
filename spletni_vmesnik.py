# import model
import bottle


@bottle.get('/')
def index():
    return bottle.template("views/base.html")

@bottle.get('/kuhanje')
def index():
    return bottle.template("views/kuhanje.html")    


#to mora biti na dnu datoteke 
bottle.run(debug=True, host="localhost", reloader=True)