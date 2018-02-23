from flask import Blueprint, render_template, abort
import json
from jinja2 import TemplateNotFound

Home = Blueprint('Home', __name__,
                        template_folder='/templates')
with open('./defineConfig.json', 'r') as json_data:
    define = json.load(json_data)

@Home.route('/', defaults={'/': 'index'})
@Home.route('/')
def index():
    try:
        enigmes = [0,0,0,0]
        portes = [0,0]
        leds = [0]
        return render_template('home/index.html', enigmes = define["enigme"], portes = define["porte"], leds = leds)
    except TemplateNotFound:
        return "not good !!"
        # abort(404)
