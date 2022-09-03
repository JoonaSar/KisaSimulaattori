from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/testi")
def testi():
    return "Testi sivu"

if __name__ == "__main__":
    app.run(debug = True)