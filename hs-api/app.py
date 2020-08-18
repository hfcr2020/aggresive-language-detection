from flask import Flask, request
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model('../my_model')


@app.route("/", methods=["POST"])
def index():
    print("Request received")
    tweet = request.json
    prediction = model.predict(tweet['tweet'])
    hate_speech = prediction > 0.5
    return hate_speech
