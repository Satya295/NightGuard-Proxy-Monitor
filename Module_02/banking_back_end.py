import flask
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Allow cross-origin
CORS(app)
cors = CORS(app, resources={
    r"/": {
        "origins": "*"
    }
})


# function send keepalive response messages to the proxy
@app.route("/keepalive", methods=["GET"])
def send_keepalive():
    print("***** send_keepalive is calling *****")
    return "success"


app.run(port=5502)
