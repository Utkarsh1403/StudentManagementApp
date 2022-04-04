import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def StudentData():
    return flask.render_template("studinfo.html")


@app.route("/search")
def searchstudent():
    return flask.render_template("search.html")


@app.route("/delete")
def deletestudent():
    return flask.render_template("delete.html")


if __name__ == "__main__":

    app.run(debug=True)