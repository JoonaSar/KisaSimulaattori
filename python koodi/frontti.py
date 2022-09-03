from flask import Flask, redirect, url_for, render_template
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():

    # Listaa tallennetut kisat
    p = Path("./saves")
    tallennetut_kisat = [f.name for f in p.iterdir() if f.is_file]


    return render_template("main.html", kisat=tallennetut_kisat)

@app.route("/testi")
def testi():
    return "Testi sivu"

@app.route("/kisa/<filename>")
def avaa_kisa(filename):
    return render_template("kisa.html", filename = filename)

if __name__ == "__main__":
    app.run(debug = True)