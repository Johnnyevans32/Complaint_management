from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_assets import Environment, Bundle
from flask_login import current_user
from flask import current_app as app
from .models import User
from flask_login import login_required, current_user
import requests
import json
import hashlib

#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
main_bp = Blueprint('main_bp', __name__ )

@main_bp.app_errorhandler((404))
def page_not_found(error):
    return render_template('404.html'), 404

@main_bp.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data =  request.form.to_dict()
        request_api(data)
        texts = get_complaints()
        return redirect(url_for("main_bp.form"))
    return render_template("index.html", value=get_complaints())


def request_api(data):
    #data["category"] = [{"name":"Selling"}]
    response = requests.post('https://complaint.microapi.dev/v1/complaint/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    if response.status_code != 201:

    ## flash is not working yet
        flash('Please try again.')
    else:
        flash('Complaint has successfully being submitted!!')
        return render_template("index.html", value=get_complaints())




@main_bp.route('/delete/<_id>', methods=['GET'])
def delete(_id):
    response = requests.delete('https://complaint.microapi.dev/v1/complaint/delete/'+str(_id), headers={'Content-Type': 'application/json'})
    flash('Complaint Deleted!')
    return redirect(url_for("main_bp.form"))

@main_bp.route('/update/<_id>', methods=["POST"])
def update(_id):
    data = request.form.to_dict()
    data["status"] =  "closed"
    response = requests.patch('https://complaint.microapi.dev/v1/complaint/update/'+str(_id), headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    print(data, response.text)
    return redirect(url_for("main_bp.form"))


def get_complaints():
    response = requests.get('https://complaint.microapi.dev/v1/complaint/all')
    all_complaints = response.json()
    return all_complaints

@main_bp.route('/comments/<_id>', methods=['GET'])
def comments(_id):
    response = requests.get('https://complaint.microapi.dev/v1/'+str(_id)+'/comment/all', headers={'Content-Type': 'application/json'})
    all_comments = response.json()
    return render_template("comments.html", value=all_comments)

@main_bp.route('/new_comment/<_id>', methods=['POST', 'GET'])
def new_comment(_id):
    data = request.form.to_dict()
    response = requests.post('https://complaint.microapi.dev/v1/'+str(_id)+'/comment/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    if response.status_code == 201:
        flash('Comment has successfully being submitted!!')
    else:
        flash('Please try again.')