from flask import Flask, render_template, url_for, request, redirect, flash
import requests
import json
import hashlib

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data =  request.form.to_dict()
        request_api(data)
        texts = get_complaints()
        return redirect(url_for("form"))
    return render_template("index.html", value=get_complaints())


def request_api(data):
    #data["category"] = [{"name":"Selling"}]
    response = requests.post('https://complaint.microapi.dev/v1/complaint/new', headers={'Content-Type': 'application/json'}, data=json.dumps(data))
    if response.status_code != 201:

    ## flash is not working yet
        flash('Please try again.')
    else:
        flash('Complaint has successfully being submitted!!')



@app.route('/delete/<_id>', methods=['GET'])
def delete(_id):
    response = requests.delete('https://complaint.microapi.dev/v1/complaint/delete/'+str(_id), headers={'Content-Type': 'application/json'})
    return redirect(url_for("form"))


def get_complaints():
    response = requests.get('https://complaint.microapi.dev/v1/complaint/all')
    all_complaints = response.json()
    return all_complaints
