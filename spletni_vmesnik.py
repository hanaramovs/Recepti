import bottle
import model


@bottle.get('/')
def index():
    return bottle.template(
"views/base.tpl")


@bottle.post('/cookbook/')
def index():
    moka = model.Ingredient(['Moka',bottle.request.forms.getunicode("Moka"),'g'])
    sladkor = model.Ingredient(['Sladkor',bottle.request.forms.getunicode("Sladkor"),'g'])
    mleko = model.Ingredient(['Mleko',bottle.request.forms.getunicode("Mleko"),'dcl'])
    kakav = model.Ingredient(['Kakav',bottle.request.forms.getunicode("Kakav"),'g'])
    jajca = model.Ingredient(['Jajca',bottle.request.forms.getunicode("Jajca"),'kos'])
    maslo = model.Ingredient(['Jajca',bottle.request.forms.getunicode("Maslo"),'g'])
    pecilni_prasek = model.Ingredient(['Jajca',bottle.request.forms.getunicode("Pecilni prašek"),'kos'])
    smetana = model.Ingredient(['Jajca',bottle.request.forms.getunicode("Smetana"),'g'])
    skuta = model.Ingredient(['Jajca',bottle.request.forms.getunicode("Skuta"),'g'])

    seznam_zivila_na_voljo = [moka,sladkor,mleko,kakav,jajca,maslo,pecilni_prasek,smetana,skuta]
    
    return bottle.template("views/cookbook.tpl", seznam_zivila_na_voljo=seznam_zivila_na_voljo)   

@bottle.post('/recepie/')
def index():
    recept = model.Recipe()
    return bottle.template("views/recepie.tpl", recept)    


#to mora biti na dnu datoteke 
bottle.run(debug=True, host="localhost", reloader=True)