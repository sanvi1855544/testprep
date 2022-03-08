from flask import Blueprint, render_template, request

sanvi_bp = Blueprint('Sanvi', __name__,
                       url_prefix='/Sanvi',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/Sanvi')

@sanvi_bp.route("/", methods=['GET','POST'])
def sanvi_index():

    return render_template("Sanvi.html")