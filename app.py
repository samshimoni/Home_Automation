from flask import Flask, request
from sonos import *
import music_server
import Camera.camera
import cfg_automation
import logger
app = Flask(__name__)


try:
    sonos = SonosMove()
    sons_alive = True
except AttributeError:
    print('Sonos or Apachee is down')
    sons_alive = False

cfg = cfg_automation.Cfg()
music_server = music_server.MusicServer()
cam = Camera.camera.Camera()
logger = logger.Logger('Flask').logger


@app.route('/', methods=['GET'])
def index():
    return 'Hello, Welcome to my home automation page'


@app.route('/sonos/play', methods=['GET'])
def play_sonos():
    if sons_alive:
        ans = sonos.play()
        return ans

    return "Sonos is off"


@app.route('/sonos/show_all', methods=['GET'])
def show_all():
    return str(music_server.give_list()).replace(',', '\n')


@app.route('/sonos/pause', methods=['GET'])
def pause_sonos():
    if sons_alive:
        ans = sonos.pause()
        return ans
    return "Sonos is off"


@app.route('/sonos/next', methods=['GET'])
def sonos_next():
    if sons_alive:
        return sonos.next()
    return "Sonos is off"


@app.route('/sonos/prev', methods=['GET'])
def sonos_prev():
    if sons_alive:
        return sonos.prev()
    return "Sonos is off"


@app.route('/sonos/add_music', methods=['GET'])
def sonos_add_uris():
    if sons_alive:
        return sonos.add_uri_to_sonos()
    return "Sonos is off"


@app.route('/sonos/refresh', methods=['GET'])
def sonos_refresh():
    return sonos.refresh()


@app.route('/sonos/volume', methods=['POST'])
def sonos_up():
    volume = request.form.get('volume')
    return sonos.volume(value=volume)


@app.route('/camera/capture', methods=['GET'])
def capture():
    if cam.is_alive():
        cam.capture()
        logger.info('Captured')
        return "Capturing.."
    else:
        logger.error('Failed Capturing')
        return "Failed"


@app.route('/camera/clean', methods=['GET'])
def clean():
    if cam.is_alive():
        cam.clean_dir_from_photos()
        logger.info('Cleaned')
        return "Cleaned.."
    else:
        logger.error('Failed Capturing')
        return "Failed Cleaning"


if __name__ == '__main__':
    app.run(host=cfg.flaskAddress, port=cfg.flaskPort)
