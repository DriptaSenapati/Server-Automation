from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to new world 2"

if __name__ == '__main__':
    app.run(debug=True)