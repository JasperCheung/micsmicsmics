from flask import Flask
import os

app = Flask(__name__)

try:
    app_settings = os.environ['APP_SETTINGS']
    print("WE SEE:", os.environ['APP_SETTINGS'])
except:
    app_settings = "config.DevelopmentConfig"

app.config.from_object(app_settings)
print(app_settings)



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
    app.run()
