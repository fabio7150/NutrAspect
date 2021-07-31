from flask import Flask
from flask import request
from flask import render_template
import pymongo
import os

app = Flask(__name__)



client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['NutrAspectProva']
utenti_collection = db["utenti"]







@app.route('/fx', methods=['GET', 'POST'])
def fromProvaStampa(email):  # put application's code here

    return ''' <h1>{} <- email :D <h1> '''.format(email)


@app.route('/', methods=['GET', 'POST'])
def fromProva():
    emailArr=['capocchia@provole.it','nopon@nopon.it']



    #data = request.data()
    email = request.form.get('email')
    password = request.form.get('password')

    if email is not None and password is not None:
        print('POST pieno')
        print(email)
        print(password)
        print(utenti_collection.find_one({"email": email}))

        if utenti_collection.find_one({"email": email}) is not None:
            return fromProvaStampa(email)

    else:
        print('POST vuoto')
    return render_template('index.html')





@app.route('/login')
def carica():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
