from flask import Flask, request
from config import *
from sonos import *
import music_server
from Camera.camera import Camera
import Logger

app = Flask(__name__)

try:
    sonos = SonosMove()

except AttributeError:
    print('Sonos or Apachee is down')

music_server = music_server.MusicServer()
camera = Camera(bash_capture_script)

Logger.log.info('starting...')


@app.route('/', methods=['GET'])
def index():
    Logger.log.info('Entered to Main page')
    return 'Hello, Welcome to my home automation page'


@app.route('/sonos/play', methods=['GET'])
def play_sonos():
    if sonos.is_alive():
        ans = sonos.play()
        Logger.log.info('Playing')
        return ans


@app.route('/sonos/show_all', methods=['GET'])
def show_all():
    return str(music_server.give_list()).replace(',', '\n')
    Logger.log.info('Show all')


@app.route('/sonos/pause', methods=['GET'])
def pause_sonos():
    if sonos.is_alive():
        ans = sonos.pause()
        Logger.log.info('Paused')
        return ans


@app.route('/sonos/next', methods=['GET'])
def sonos_next():
    Logger.log.info('Next')
    return sonos.next()


@app.route('/sonos/prev', methods=['GET'])
def sonos_prev():
    Logger.log.info('Prev')
    return sonos.prev()


@app.route('/sonos/add_music', methods=['GET'])
def sonos_add_uris():
    Logger.log.info('Added Music')
    return sonos.add_uri_to_sonos()


@app.route('/sonos/refresh', methods=['GET'])
def sonos_refresh():
    Logger.log.info('Refreshed')
    return sonos.refresh()


@app.route('/sonos/volume', methods=['POST'])
def sonos_up():
    volume = request.form.get('volume')
    return sonos.volume(value=volume)


@app.route('/camera/capture', methods=['GET'])
def capture():
    if camera.is_alive():
        camera.capture()
        Logger.log.info('Captured')
        return "Capturing.."
    else:
        Logger.log.error('Failed Capturing')
        return "Failed"


if __name__ == '__main__':
    app.run(host=IP_ADDRESS, port=PORT)
