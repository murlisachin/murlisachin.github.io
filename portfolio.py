from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def portfolio_home():
    return render_template('./index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return render_template('./thank-you.html')
    else:
        return 'error'


# @app.route('/<string: page_name>')
# def html_page(page_name):
#     return render_template(page_name)


# @app.route("/<username>/<int:id>")
# def user(username=None, id=None):
#     return render_template('./index.html', name=username.title(), id_num=id)


# @app.route("/blog")
# def blog():
#     return "<p>This is a blank blog.</p>"


# @app.route("/about")
# def about():
#     return render_template('./about.html')
