from flask import Flask, request
import cfg_watering
import os
app = Flask(__name__)
cfg = cfg_watering.Cfg()


@app.route('/', methods=['GET'])
def index():
    return 'Hello, Welcome to Plant Watering Client HomePage'


@app.route('/plant/auto_water', methods=['GET'])
def auto_water():
    os.system('python3 /home/pi/Desktop/PlantWatering/auto_water.py')
    return "Activated"


if __name__ == '__main__':
    app.run(host=cfg.flaskAddress, port=cfg.flaskPort)
