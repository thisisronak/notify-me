from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is the tasknotifier app speaking--- Beware!"

if __name__ == "__main__":
    app.run()