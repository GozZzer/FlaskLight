from flask import Flask, render_template, url_for, request, redirect
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SPEED'] = 10
app.config['COLOR'] = "#ff0000"
app.config["ENABLE"] = False


@app.route('/')
def index():
    return render_template('overview.html', speed=app.config["SPEED"], color=app.config["COLOR"], enabled=app.config["ENABLE"])


@app.route("/speed/", methods=["GET", "POST"])
def speed():
    if request.method == "POST":
        app.config["SPEED"] = request.form["speed"]
        if not app.config["SPEED"]:
            app.config["SPEED"] = 10
    return render_template('speed.html', speed=app.config["SPEED"])


@app.route("/color/", methods=["GET", "POST"])
def color():
    if request.method == "POST":
        app.config["COLOR"] = request.form["color"]
        if not app.config["COLOR"]:
            app.config["COLOR"] = "#ff0000"
    return render_template('color.html', color=app.config["COLOR"])


@app.route("/enable/", methods=["GET", "POST"])
def enable():
    if request.method == "POST":
        try:
            req = request.form["enable"]
            app.config["ENABLE"] = True
        except BadRequest:
            app.config["ENABLE"] = False
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)