from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>", methods=['GET'])
def hello(name):
    return f"<H1> My name is {name}</h1>"
@app.route("/", methods=['GET'])
def welcome():
    return "Hello World"

if __name__=="__main__":
    app.run(port=5000,debug=True)

