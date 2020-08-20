from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
def index():
    print("Request received")
    tweet = request.json
    print("Tweet is: " + str(tweet['tweet']))
    return "true"
