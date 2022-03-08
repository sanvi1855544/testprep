from flask import Blueprint, render_template, request

shruti_bp = Blueprint('Shruti', __name__,
                     url_prefix='/Shruti',
                     template_folder='templates',
                     static_folder='static', static_url_path='static/Shruti')

@shruti_bp.route("/", methods=['GET','POST'])
def shruti_index():

    return render_template("Shruti.html")