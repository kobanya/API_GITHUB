''' Flask server inicializálása'''

from flask import Flask

app= Flask(__name__)
@app.route('/')

def index():
   return " Igyál több  kávét"

app.run(host="0.0.0.0", port=8080)
 
