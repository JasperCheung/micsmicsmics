from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Pages"

@app.route("/hello")
def hello():
    return "Hello, World"

@app.route("/gimme_json", methods=['GET'])
def send_json():
    return {"key":"value"}


if __name__ == '__main__':
    app.run(debug=True)
