from flask import Flask, render_template, url_for, request, redirect, flash
import requests
import json
import hashlib

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def name():
    texts=get_complaints()
    return render_template( "index.html",   value=texts )

@app.route('/index')
def nam():
    texts = get_complaints()
    return render_template('index.html',    value = texts)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/submit_form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data =  request.form.to_dict()
        request_api(data)
        texts = get_complaints()
        return render_template('index.html', value=texts)
    else:
    	return 'bad'


def request_api(data):
    response = requests.post('http://complaint.microapi.dev/v1/complaint/new',headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    if response.status_code != 201:
        flash('Please try again.')
    else:
        flash('complaint has successfully being submitted!!')




def get_complaints():
    response = requests.get('http://complaint.microapi.dev/v1/complaint/all')
    all_complaints = response.json()   
    return all_complaints