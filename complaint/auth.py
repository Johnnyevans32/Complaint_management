from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User
from . import login_manager

#Blueprint auth
auth =  Blueprint('auth_bp' , __name__)


@auth.route("/", methods=["GET", "POST"])
def login():

    """User login page."""

    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.form'))

    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        data = request.form.to_dict()
        email, password = data.values()
        user = User.query.filter_by(email=email).first()
        if data:
            login_user(user, remember=False)
            next = request.args.get("next")
            return redirect(next or url_for("main_bp.form"))
        flash('Invalid username/password combination')

    # GET: Serve Log-in page
    return render_template("login.html")

@auth.route("/signup", methods=["GET", "POST"])
def signup():

    """User sign-up page."""

    # POST: Sign user in
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get("password")
        user_check = User.query.filter_by(email=email).first()
        if user_check is None:
            user = User(
                name=name,
                email=email,
                password=generate_password_hash(password)
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("main_bp.index"))

        flash('A user already exists with that email address.')
    # GET: Serve Sign-up page
    return render_template("signup.html")


@auth.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None





#from flask import Flask, render_template, url_for, request, redirect, flash
#import requests
#import json
#import hashlib
#
#app = Flask(__name__)
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template('404.html'), 404
#
#@app.route('/', methods=['POST', 'GET'])
#def form():
#    if request.method == 'POST':
#        data =  request.form.to_dict()
#        request_api(data)
#        texts = get_complaints()
#        return redirect(url_for("form"))
#    return render_template("index.html", value=get_complaints())
#
#
#def request_api(data):
#    #data["category"] = [{"name":"Selling"}]
#    response = requests.post('https://complaint.microapi.dev/v1/complaint/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
#    if response.status_code != 201:
#
#    ## flash is not working yet
#        flash('Please try again.')
#    else:
#        flash('Complaint has successfully being submitted!!')
#
#
#
#@app.route('/delete/<_id>', methods=['GET'])
#def delete(_id):
#    response = requests.delete('https://complaint.microapi.dev/v1/complaint/delete/'+str(_id), headers={'Content-Type': 'application/json'})
#    return redirect(url_for("form"))
#
#@app.route('/update/<_id>', methods=["POST"])
#def update(_id):
#    data = request.form.to_dict()
#    data["status"] =  "closed"
#    response = requests.patch('https://complaint.microapi.dev/v1/complaint/update/'+str(_id), headers={'Content-Type': 'application/json'}, data=json.dumps(data))
#    print(data, response.text)
#    return redirect(url_for("form"))
#
#
#def get_complaints():
#    response = requests.get('https://complaint.microapi.dev/v1/complaint/all')
#    all_complaints = response.json()
#    return all_complaints
