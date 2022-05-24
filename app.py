from __init__ import app
from flask import Flask, render_template, request
from crud.app_crud import app_crud
from crud.app_crud_api import app_crud_api
from Sanvi.templates.Sanvi import sanvi_bp
from Shruti.templates.Shruti import shruti_bp
from Kian.templates.Kian import kian_bp
from Gennalyn.templates.Gennalyn import gennalyn_bp

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


@app.route("/")
def index():
    import requests
    URL = "https://last-airbender-api.herokuapp.com/api/v1/characters/random"
    r = requests.get(url=URL)
    data = r.json()
    return render_template("index.html", data=data)  # "Test Prep Website"


# about pages
@app.route("/Gennalyn/")
def Gennalyn():
    return render_template("Gennalyn.html")


@app.route("/Sanvi/")
def Sanvi():
    return render_template("Sanvi.html")

@app.route("/Kian/")
def Kian():
    return render_template("Kian.html")


# PBL pages

@app.route('/Hangman/')
def Hangman():
    return render_template("Hangman.html")

@app.route('/tictactoe/')
def tictactoe():
    return render_template("tictactoe.html")

@app.route('/diagnostic/')
def diagnostic():
    return render_template("diagnostic.html")

@app.route('/flashcard/')
def flashcard():
    return render_template("flashcard.html")

@app.route('/snake/')
def snake():
    return render_template("snake.html")


@app.route('/pingpong/')
def pingpong():
    return render_template("pingpong.html")

@app.route('/replit/')
def replit():
    return render_template("replit.html")

@app.route('/replit2/')
def replit2():
    return render_template("replit2.html")


@app.route('/lookup')
def lookup():
    query = request.args.get('lookup')
    # req_search = query.filter_by(req_no=query)

    page = query + '.html'
    from pathlib import Path
    my_file = Path("templates/" + page)
    if my_file.exists():
        return render_template(page)
    else:
        return render_template('lookup.html', req_search=query)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

app.register_blueprint(sanvi_bp)
app.register_blueprint(shruti_bp)
app.register_blueprint(kian_bp)
app.register_blueprint(gennalyn_bp)

