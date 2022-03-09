from __init__ import app
from flask import Flask, render_template, request
from Sanvi.templates.Sanvi import sanvi_bp
from Shruti.templates.Shruti import shruti_bp
from Kian.templates.Kian import kian_bp
from Gennalyn.templates.Gennalyn import gennalyn_bp



@app.route("/")
def index():
    import requests
    URL = "https://last-airbender-api.herokuapp.com/api/v1/characters/random"
    r = requests.get(url=URL)
    data = r.json()
    return render_template("index.html", data=data) #"Test Prep Website"

#about pages
@app.route("/Gennalyn/")
def Gennalyn():
    return render_template("Gennalyn.html")

@app.route("/Sanvi/")
def Sanvi():
    return render_template("Sanvi.html")

#PBL pages





@app.route('/lookup')
def lookup():

    query = request.args.get('lookup')
    # req_search = query.filter_by(req_no=query)

    page = query+'.html'
    from pathlib import Path
    my_file = Path("templates/"+page)
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