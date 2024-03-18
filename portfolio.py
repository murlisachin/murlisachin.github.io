from flask import Flask, render_template, request, redirect, Response
import csv

app = Flask(__name__)


@app.route('/')
def portfolio_home():
    return render_template('./index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return Response(status=204)
        except:
            return 'Error saving to database.'
    else:
        return 'Error'


def write_to_csv(data):
    with open('./database.csv', 'a', newline= '') as db:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
        