from flask import Flask, jsonify, request,send_file
from keras.models import load_model
import pandas as pd
import tensorflow as tf
import keras
from datetime import datetime
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# initialize our Flask application
app = Flask(__name__)

@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(str("Successfully stored  " + str(data)))


@app.route("/message", methods=["GET"])
def message():
    posted_data = request.get_json()
    name = posted_data['name']
    return jsonify(" Hope you are having a good time " + name + "!!!")

@app.route("/hello", methods=["GET"])
def hello():
    return "Rock, Paper and Scissors image classification server.\nAndre Castillo\n" + str(datetime.today())

@app.route("/image", methods=["GET"])
def image():
    if request.args.get('type') == '1':
       filename = 'client_myhand.jpg'
       model.load('rps.h5')
    else:
       filename = 'error.jpg'
    return send_file(filename, "Rock, Paper and Scissors image classification server.\nAndre Castillo\n" + str(datetime.today()))

    
#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)


#@app.route("/login", methods=["POST"])
#def login():
    #command = request.form['command']
    #if command == "client":
    # print("Andre Castillo")
    #return jsonify("Success")

#  main thread of execution to start the server
#if __name__=='__main__':
    #app.run(debug=True)
