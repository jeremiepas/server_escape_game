from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# ruban = led.LedRGB(int(config['led1']['red']),int(config['led1']['green']), int(config['led1']['blue']))


Led = Blueprint('Led', __name__,
                        template_folder='/templates')

@Led.route('/', defaults={'led': 'index'})
@Led.route('/')
def index():
    try:
        return render_template('led/index.html')
    except TemplateNotFound:
        return "not good !!"
        # abort(404)

@Led.route('/test')
def enigme():
    return "testtest"

@Led.route('/led/<led_id>', methods = ['POST'])
def led(led_id):
    if request.method == 'POST':
        data = request.form
        # if(0 <= int(data['r']) && 0 <= int(data['g']) && 0 <= int(data['b']) && 255 >= int(data['r']) && 255 >= int(data['g']) && 255 >= int(data['b'])):
        ruban[led_id].color(int(data['r']), int(data['g']), int(data['b']))
        return str(data)
    # ruban.color(data['r'],data['g'],data['b'])
#     return render_template('pymeetups.html')
