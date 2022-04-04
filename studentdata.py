from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def StudentData():
    return "Student data "


@app.route("/search")
def searchstudent():
    return "required student is: "


@app.route("/delete")
def deletestudent():
    return "deleted student is: "


if __name__ == "__main__":

    app.run(debug=True)