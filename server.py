from flask import Flask
from password_generator import PasswordGenerator

app=Flask(__name__)

@app.route("/home")
def home():
    pwd = PasswordGenerator()
    return {"password" : [str(pwd)] }

@app.route("/dummyPassword")
def dev():
    return{"password" : ["Abc123!@#$"] }

if __name__ == "__main__":
    app.run(debug=True)