import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
# Replace with your TensorFlow model loading code
# model = tf.keras.models.load_model("your_model.h5")


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/data', methods = ['POST'])
@cross_origin(origins='*')
def api_test():
    data = request.get_json()
    return data
if __name__ == '__main__':
    app.run()
