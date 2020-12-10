from flask import Flask, request
from sonos import *
import cfg_sonos
import logger

app = Flask(__name__)
cfg = cfg_sonos.Cfg()
logger = logger.Logger('SonosFlask').logger

try:
    sonos = SonosMove()
except AttributeError:
    logger.error("Problem with connection to Sonos Speaker")


@app.route('/', methods=['GET'])
def index():
    return 'Hello, Welcome to Sonos Client HomePage'


@app.route('/sonos/play', methods=['GET'])
def play_sonos():
    ans = sonos.play()
    return ans


@app.route('/sonos/show_all', methods=['GET'])
def show_all():
    requests.get()


@app.route('/sonos/pause', methods=['GET'])
def pause_sonos():
    ans = sonos.pause()
    return ans


@app.route('/sonos/next', methods=['GET'])
def sonos_next():
    return sonos.next()


@app.route('/sonos/prev', methods=['GET'])
def sonos_prev():
    return sonos.prev()


@app.route('/sonos/add_music', methods=['GET'])
def sonos_add_uris():
    return sonos.add_uri_to_sonos()


@app.route('/sonos/refresh', methods=['GET'])
def sonos_refresh():
    return sonos.refresh()


@app.route('/sonos/volume', methods=['POST'])
def sonos_up():
    volume = request.form.get('volume')
    return sonos.volume(value=volume)


if __name__ == '__main__':
    app.run(host=cfg.flask_host, port=cfg.flask_port)
