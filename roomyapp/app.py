import json
from flask import Flask, request, jsonify, abort
from logbook import Logger

app = Flask(__name__)
log = Logger(__name__)

from models.events import CameraEvent
from models.device import CameraDevice
from models.store import EventStore, DeviceStore

event_store = EventStore()
device_store = DeviceStore()


@app.route("/")
def index():
    return "Minge."


@app.route("/device/register", methods=['POST'])
def register_device():
    payload = json.loads(request.data)
    # TODO: Change to device.validate()
    if payload.get('location'):
        device = CameraDevice(location=payload.get('location'))
        device_store.add(device)
        # TODO: Return Safe JSON straight from the object
        return jsonify({'device_id': str(device.guid)})
    else:
        abort(405, 'Invalid payload')


@app.route("/event/camera/<device_id>", methods=["POST"])
def camera_event(device_id):
    payload = json.loads(request.data)
    count = payload.get('count')
    log.info('Got count from {0} of {1}'.format(device_id, count))
    camera_event = CameraEvent(device_id=device_id, count=count)
    event_store.add(camera_event)
    log.debug('Now have {} in event store'.format(len(event_store)))
    return jsonify({'status': 'OK'})


if __name__ == "__main__":
    app.run(debug=True)
