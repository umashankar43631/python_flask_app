from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>", methods=['GET'])
def hello(name):
    return f"<H1>Welcome to this website {name}</h1>"

if __name__=="__main__":
    app.run(port=5000,debug=True)

