from flask import Blueprint, render_template
from app.models import Brand, Product
web = Blueprint('web', __name__, url_prefix='/', template_folder="./templates")


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/brand')
def get_brand():
    return render_template('brand.html')


