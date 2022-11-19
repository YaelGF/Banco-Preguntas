import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBPmbcSj2xTLHDhrt4uTJiJOgIUyrjU0CM",
  "authDomain": "banco-de-preguntas-3f964.firebaseapp.com",
  "databaseURL": "https://banco-de-preguntas-3f964-default-rtdb.firebaseio.com",
  "projectId": "banco-de-preguntas-3f964",
  "storageBucket": "banco-de-preguntas-3f964.appspot.com",
  "messagingSenderId": "718216060964",
  "appId": "1:718216060964:web:10190eb3cb95eeaaa5f8b1",
  "measurementId": "G-BMJZZM42NF"
};

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()