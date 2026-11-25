from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, web!"   # TODO 4B: return the template index.html instead


# TODO 2A: the route /about

# TODO 3A: the route /api/info

# TODO 5B: the route /country/<code>

if __name__ == "__main__":   # keep this block at the END of the file
    app.run(debug=True)
