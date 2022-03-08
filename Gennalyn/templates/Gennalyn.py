from flask import Blueprint, render_template, request

gennalyn_bp = Blueprint('Gennalyn', __name__,
                       url_prefix='/Gennalyn',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/Gennalyn')

@gennalyn_bp.route("/", methods=['GET','POST'])
def gennalyn_index():

    return render_template("Gennalyn.html")