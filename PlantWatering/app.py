from flask import Flask, request
import cfg_watering
import auto_water
import capacitive_sensor
app = Flask(__name__)
cfg = cfg_watering.Cfg()

moisture_sensor = capacitive_sensor.MoistureSensor()


@app.route('/', methods=['GET'])
def index():
    return 'Hello, Welcome to Plant Watering Client HomePage'


@app.route('/plant/auto_water', methods=['GET'])
def water():
    pw = auto_water.PlantWatering()
    if None is request.args.get('pin_number'):
        return 'Pattern should be : ?pin_number=[pin_number]'
    pin_number = int(request.args.get('pin_number'))
    response = pw.auto_water(pin_number, moisture_sensor.read_humidity(pin_number))
    return response


@app.route('/plant/get_humidity', methods=['GET'])
def get_humidity():
    if None is request.args.get('pin_number'):
        return 'Pattern should be : ?pin_number=[pin_number]'
    pin_number = int(request.args.get('pin_number'))
    response = moisture_sensor.read_humidity(pin_number)
    return str(response)


if __name__ == '__main__':
    app.run(host=cfg.flaskAddress, port=cfg.flaskPort)
