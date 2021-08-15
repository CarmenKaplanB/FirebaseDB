import web # IMPORTACCION DE WEB.
import pyrebase
import json

render = web.template.render("mvc/views/") 

class Index():

    def GET(self):
        try:
            result = ""
            return render.index(result) 
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            firebaseConfig  = {
                            "apiKey": "AIzaSyC3WNNu06AteNdfy9F6_7Rus194IgTBe0c",
                            "authDomain": "fir-db-9981a.firebaseapp.com",
                            "databaseURL": "https://fir-db-9981a-default-rtdb.firebaseio.com/",
                            "projectId": "fir-db-9981a",
                            "storageBucket": "fir-db-9981a.appspot.com",
                            "messagingSenderId": "602706046119",
                            "appId": "1:602706046119:web:43f3d385a6b61126afbf82",
                            "measurementId": "G-5Y2GRV0LM0"
                            }
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            form = web.input()
            email = form.email
            contra = form.contra
            user = auth.sign_in_with_email_and_password(email,contra)

            if user != "":
                web.seeother('/vista')
            
        except Exception as e:
            obt = json.loads(str(e.args[1]))
            errorF = obt['error']['message']
            return render.index("Ups... imposible tenemos un error: "+errorF)
            