import random
from flask import Flask , render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def ind():
    print session["somekey"]
    if not "somekey" in session:
        session["somekey"] = random.randrange(1,101)
        print session["somekey"]
    try:
        session["guess"]= int(session["guess"])
    except KeyError :
        session["guess"]= 0
    return render_template("index.html", num = session['somekey'])
@app .route("/guess", methods = ["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    print session["guess"]
    print type(request.form['guess'])
    return redirect("/")

@app.route("/reset", methods= ["POST"])
def reset():
    session["somekey"] = random.randrange(1,101)
    session["guess"]= 0
    return redirect("/")
app.run(debug= True)    

    