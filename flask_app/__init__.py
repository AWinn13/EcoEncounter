from flask import Flask, session
DB = 'eco_encounters'
app = Flask(__name__)
app.secret_key = "phishrules"
