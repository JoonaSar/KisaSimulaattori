from contextlib import nullcontext
import re
from flask import Flask, redirect, url_for, render_template, request
from pathlib import Path
from main import luo_kisa

app = Flask(__name__)

@app.route("/")
def home():

    # Listaa tallennetut kisat
    p = Path("./saves")
    tallennetut_kisat = [f.name for f in p.iterdir() if f.is_file]


    return render_template("main.html", kisat=tallennetut_kisat)

@app.route("/uusi_kisa", methods=["POST", "GET"])
def uusi_kisa():
    if request.method=="GET":
        return render_template("uusi_kisa.html", err=False)
    else:
        kisan_nimi = request.form["kisan_nimi"]
        try:
            luo_kisa(kisan_nimi)
        except FileExistsError:
            return render_template("uusi_kisa.html", err = True)
        return redirect(url_for("avaa_kisa", filename=kisan_nimi))



@app.route("/kisa/<filename>")
def avaa_kisa(filename):
    return render_template("kisa.html", filename = filename)

if __name__ == "__main__":
    app.run(debug = True)