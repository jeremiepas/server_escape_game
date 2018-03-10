from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import pipes
t = pipes.Template()

# ruban = led.LedRGB(int(config['led1']['red']),int(config['led1']['green']), int(config['led1']['blue']))


Enigme_bot = Blueprint('Enigme_bot', __name__,
                        template_folder='/templates')

@Enigme_bot.route('/')
def index():
    with t.open('pipes/enigme_1', 'r') as f:
        p = f.read().split('--')
    return p[0]
        # abort(404)


@Enigme_bot.route('/bot/<bot_etat>', methods = ['POST'])
def led(bot_etat):
    if request.method == 'POST':
        data = request.form

        if (bot_etat == "1"):
            print('pipes/porte_'+data["porte"])
            print(data["etat"])
            with t.open('pipes/porte_'+data["porte"], 'w') as f:
                f.write(data["etat"]+'--True--'+data["etat"]) #valeur,  mode-auto
        return str(data)
