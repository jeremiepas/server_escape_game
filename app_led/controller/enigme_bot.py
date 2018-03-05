from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import pipes
t = pipes.Template()

# ruban = led.LedRGB(int(config['led1']['red']),int(config['led1']['green']), int(config['led1']['blue']))


Bot = Blueprint('Enigme_bot', __name__,
                        template_folder='/templates')

@Bot.route('/', defaults={'led': 'index'})
@Bot.route('/')
def index():
    try:
        return render_template('led/index.html')
    except TemplateNotFound:
        return "not good !!"
        # abort(404)


@Bot.route('/bot/<bot_etat>', methods = ['POST'])
def led(bot_etat, valide):
    if request.method == 'POST':
        data = request.form
        if (bot_etat == 1)
            with t.open('pipes/porte_2', 'w') as f:
                f.write(data["value"]+'--True--'+data["value"]) #valeur,  mode-auto
        return str(data)
