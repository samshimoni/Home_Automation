from flask import Flask, request
import subprocess
import cfg_watering
import os
app = Flask(__name__)
cfg = cfg_watering.Cfg()


@app.route('/', methods=['GET'])
def index():
    return 'Hello, Welcome to Plant Watering Client HomePage'


@app.route('/plant/auto_water', methods=['GET'])
def auto_water():
    proc = subprocess.Popen(['./auto_water.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    response = proc.stdout.read().decode()
    return response


if __name__ == '__main__':
    app.run(host=cfg.flaskAddress, port=cfg.flaskPort)
