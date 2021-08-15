import web  # IMPORTACCION DE WEB.
import requests
import json

render = web.template.render("mvc/views/")

class Registro():

    def GET(self):
        try:
            return render.registro()
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            form = web.input()
            nombre = form.nombre
            correo = form.email
            data_json = {
        
                'email':correo,
                'nombre':nombre
                
            }
            requests.post('https://fir-db-9981a-default-rtdb.firebaseio.com/agenda.json',data=json.dumps(data_json))
            web.seeother('/vista')
        except Exception as e:
            return "Error"+ str(e.args)