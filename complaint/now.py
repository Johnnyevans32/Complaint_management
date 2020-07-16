from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def lo():
    return render_template("login.html")

@app.route('/signup')
def signup():
    pass


app.run()
