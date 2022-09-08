from flask import Flask, request, render_template
import json
from module import *

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        json_data = json.loads(request.data)
    return render_template('index.html')
