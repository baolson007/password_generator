from flask import Flask
from password_generator import PasswordGenerator
import os;

app=Flask(__name__, static_folder='client/build', static_url_path='')

@app.route("/home")
def home():
    pwd = PasswordGenerator()
    return {"password" : [str(pwd)] }

@app.route("/dummyPassword")
def dev():
    return{"password" : ["Abc123!@#$"] }


def index():
    return app.send_static_file('index.html')
    
@app.route('/')
def serve():
    return app.send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)#, host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))