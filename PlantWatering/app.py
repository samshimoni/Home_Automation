from flask import Flask, request
import cfg_watering
import auto_water

app = Flask(__name__)
cfg = cfg_watering.Cfg()


@app.route('/', methods=['GET'])
def index():
    return 'Hello, Welcome to Plant Watering Client HomePage'


@app.route('/plant/auto_water', methods=['GET'])
def water():
    pw = auto_water.PlantWatering()
    if None is request.args.get('pin_number'):
        return 'Pattern should be : ?pin_number=[pin_number]'
    pin_number = int(request.args.get('pin_number'))
    response = pw.auto_water(pin_number)
    return response


if __name__ == '__main__':
    app.run(host=cfg.flaskAddress, port=cfg.flaskPort)
