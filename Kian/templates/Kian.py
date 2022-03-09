from flask import Blueprint, render_template, request

kian_bp = Blueprint('Kian', __name__,
                     url_prefix='/Kian',
                     template_folder='templates',
                     static_folder='static', static_url_path='static/Kian')

@kian_bp.route("/", methods=['GET','POST'])
def Kian_index():

    return render_template("Kian.html")