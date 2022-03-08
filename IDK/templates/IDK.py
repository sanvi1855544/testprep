from flask import Blueprint, render_template, request

IDK_bp = Blueprint('IDK', __name__,
                     url_prefix='/IDK',
                     template_folder='templates',
                     static_folder='static', static_url_path='static/IDK')

@IDK_bp.route("/", methods=['GET','POST'])
def IDK_index():

    return render_template("IDK.html")