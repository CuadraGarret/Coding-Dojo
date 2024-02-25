from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = 'G keep it a secret'

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def all_users():
    all_users=User.get_all()
    return render_template("read.html", users=all_users)

@app.route("/users/new")
def new_users():
    return render_template("create.html")

@app.route('/users/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)