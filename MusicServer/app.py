from flask import Flask, jsonify
import music_server
import cfg_automation
import logger
cfg = cfg_automation.Cfg()
logger = logger.Logger('Flask').logger

app = Flask(__name__)

try:
    music_server = music_server.MusicServer()
except AttributeError:
    logger.error("Problem with connection to Music Server")


@app.route('/', methods=['GET'])
def index():
    return 'Hello, Welcome to the music Server REST API'


@app.route('/music_server/give_list', methods=['GET'])
def give_list():
    music_list = music_server.give_list()
    return_dict = {'songs': music_list}
    return jsonify(return_dict)


@app.route('/music_server/give_uris', methods=['GET'])
def give_uris():
    music_uris = music_server.give_uris()
    return_dict = {'uris': music_uris}
    return jsonify(return_dict)


@app.route('/music_server/test', methods=['GET'])
def test():
    return "Test"


if __name__ == '__main__':
    app.run(host=cfg.flaskAddress, port=cfg.flaskPort)
