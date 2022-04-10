import flask
from flask import Flask, render_template,request
import sqlite3
from werkzeug.utils import redirect

con = sqlite3.connect("Studentmang.db",check_same_thread=False)
curr=con.cursor()

listOfTables=con.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENTDATA' ").fetchall()

if listOfTables!=[]:

    print("Table Already Exists ! ")
else:
    con.execute(''' CREATE TABLE STUDENTDATA(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  Name TEXT,COLLEGE_NAME TEXT,
                  BRANCH TEXT,ADMNO INTEGER,USERNAME TEXT,
                  PASSWORD TEXT,DOB TEXT); ''')

    print("Table has created")

app = Flask(__name__)


@app.route('/')
def hello():
    return flask.render_template("login.html")
database={'utkarsh':'123','admin':'12345'}

@app.route("/login",methods=['POST','GET'])
def login():
    name = request.form['username']
    pwd = request.form['password']
    if name not in database:
        flask.render_template("login.html",info='Invalid User')
    elif database[name]!=pwd:
        return flask.render_template("login.html",info='Invalid password')
    else:
        return redirect("/register")
    return flask.render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def StudentData():
    if request.method=="POST":
        getName=request.form["Name"]
        getAdmno=request.form["admno"]
        getcollege=request.form["college"]
        getBranch = request.form["br"]
        getDOB = request.form["DOB"]
        getUsername = request.form["Username"]
        getPass = request.form["pass"]

        print(getName)
        print(getAdmno)
        print(getcollege)
        print(getBranch)
        print(getDOB)
        print(getUsername)
        print(getPass)
        try:
            con.execute("INSERT INTO STUDENTDATA(name,COLLEGE_NAME,BRANCH,ADMNO,USERNAME,PASSWORD,DOB) VALUES('"+getName+"','"+getcollege+"','"+getBranch+"',"+getAdmno+",'"+getUsername+"','"+getPass+"',"+getDOB+")")
            print("Successfully Inserted")
            con.commit()
            return redirect('/Viewall')
        except Exception as e:
            print(e)
    return render_template("studinfo.html")


@app.route("/search",methods=['GET','POST'])
def searchstudent():
    if request.method=="POST":
        getAdmno=request.form['admno']
        print(getAdmno)
        try:
            querry="SELECT * FROM STUDENTDATA WHERE ADMNO="+getAdmno
            print(querry)
            curr.execute(querry)
            print("SUCCESSFULLY SELECTED! ")
            result=curr.fetchall()
            print(result)
            if len(result)==0:
                print("Invalid Admission Number")
            else:
                print(len(result))
                return  flask.render_template("search.html",students=result,status=True)
        except Exception as e:
            print(e)

    return flask.render_template("search.html",students=[],status=False)

@app.route("/delete",methods=['GET','POST'])
def deletestudent():
    if request.method=="POST":
        getAdmno=request.form['admno']
        print(getAdmno)
        try:
            querry="DELETE FROM STUDENTDATA WHERE ADMNO="+getAdmno
            print(querry)
            curr.execute(querry)
            print("SUCCESSFULLY DELETED! ")
            con.commit()
            return redirect('/Viewall')
        except Exception as e:
            print(e)

    return flask.render_template("delete.html")

@app.route("/Viewall")
def Viewall():
    curr = con.cursor()
    curr.execute("SELECT* FROM STUDENTDATA")
    result= curr.fetchall()

    return flask.render_template("Viewall.html",students=result)

if __name__ == "__main__":

    app.run(debug=True)