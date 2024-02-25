from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def name(name):
    print (name)
    return 'Hi ' + (name)

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    print(num)
    print(name)
    return num * f'{name}'

if __name__=="__main__":
    app.run(debug=True)
