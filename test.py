import pyrebase
import requests
import json
from getpass import getpass

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

email = "carmensnow2015@gmail.com"
password = "abcd1234"

user = auth.sign_in_with_email_and_password(email,password)
if user!="":
    print(user['idToken'])
else:
    print("error")
   
try:
    data_json = {
        
        'email':"jane@email.com",
        'nombre':"Jane"
       
    }
    result = requests.post('https://fir-db-9981a-default-rtdb.firebaseio.com/agenda.json',data=json.dumps(data_json))
    print (result)
except Exception as error:
    print(error.args[0])

try:
    print("Done")
    db = firebase.database()
    all_users = db.child("agenda").get()
    for user in all_users.each():
        print(user.key()) # Morty
        print(user.val()) # {name": "Mortimer 'Morty' Smith"}
        print(user.val()['nombre']) # {name": "Mortimer 'Morty' Smith"}
except Exception as e:
    print(e.args[0])  