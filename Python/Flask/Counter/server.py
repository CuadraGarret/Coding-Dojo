from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'sh this is a secret'


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    return render_template('counter.html', counter=session['counter'])

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session['counter'] = 1
    return redirect('/')


@app.route('/counter', methods=['POST'])
def counter():
    session['counter'] += 1
    return redirect('/')

@app.route('/plus_two', methods=['POST'])
def plus_two():
    session['counter'] += 2
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)