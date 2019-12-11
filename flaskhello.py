from flask import Flask

app = Flask(__name__)

# flask webserver: define index route
@app.route("/")

def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
