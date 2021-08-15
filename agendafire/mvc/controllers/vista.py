import web  # IMPORTACCION DE WEB.
import pyrebase
import requests
from getpass import getpass

render = web.template.render("mvc/views/")

class Vista():

    def GET(self):
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
            
            db = firebase.database()
            result = db.child("agenda").get()
            return render.vista(result)

        except Exception as e:
            return "Error " + str(e.args)
