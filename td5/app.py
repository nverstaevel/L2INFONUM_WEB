from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, web!"


# TODO 1: a route /about that returns a short HTML text
# TODO 2: a route /api/info that returns JSON (source, unit, licence) with jsonify
# TODO 3: a route /country/<code> that returns the code in upper case
# TODO 4: make "/" return templates/index.html with render_template
# TODO 5: a route /teapot that returns a message with status code 418


if __name__ == "__main__":
    app.run(debug=True)
