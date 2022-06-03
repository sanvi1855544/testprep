import __init__
from flask import Flask, render_template, request
from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from Sanvi.templates.Sanvi import sanvi_bp
from Shruti.templates.Shruti import shruti_bp
from Kian.templates.Kian import kian_bp
from Gennalyn.templates.Gennalyn import gennalyn_bp

from notey.app_notes import app_notes

__init__.app.register_blueprint(app_crud)
__init__.app.register_blueprint(app_crud_api)
__init__.app.register_blueprint(app_notes)


@__init__.app.route("/")
def index():
    import requests
    URL = "https://last-airbender-api.herokuapp.com/api/v1/characters/random"
    r = requests.get(url=URL)
    data = r.json()
    return render_template("index.html", data=data)  # "Test Prep Website"


# about pages
@__init__.app.route("/Gennalyn/")
def Gennalyn():
    return render_template("Gennalyn.html")


@__init__.app.route("/Sanvi/")
def Sanvi():
    return render_template("Sanvi.html")

@__init__.app.route("/Kian/")
def Kian():
    return render_template("Kian.html")


# PBL pages

@__init__.app.route('/Hangman/')
def Hangman():
    return render_template("Hangman.html")

@__init__.app.route('/tictactoe/')
def tictactoe():
    return render_template("tictactoe.html")

@__init__.app.route('/diagnostic/')
def diagnostic():
    return render_template("diagnostic.html")

@__init__.app.route('/flashcard/')
def flashcard():
    return render_template("flashcard.html")

@__init__.app.route('/snake/')
def snake():
    return render_template("snake.html")


@__init__.app.route('/pingpong/')
def pingpong():
    return render_template("pingpong.html")

@__init__.app.route('/replit/')
def replit():
    return render_template("replit.html")

@__init__.app.route('/replit2/')
def replit2():
    return render_template("replit2.html")

@__init__.app.route('/replit3/')
def replit3():
    return render_template("replit3.html")

@__init__.app.route('/test/')
def test():
    return render_template("test.html")



@__init__.app.route('/lookup')
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
    __init__.app.run(host="127.0.0.1", port=8080)

__init__.app.register_blueprint(sanvi_bp)
__init__.app.register_blueprint(shruti_bp)
__init__.app.register_blueprint(kian_bp)
__init__.app.register_blueprint(gennalyn_bp)

