import json
from flask import Flask, request, jsonify, abort, make_response
from logbook import Logger
from dictshield.base import ShieldException

app = Flask(__name__)
log = Logger(__name__)

from models.events import CameraEvent
from models.device import CameraDevice
from models.store import EventStore, DeviceStore

event_store = EventStore()
device_store = DeviceStore()

__version__ = 0.1

@app.route("/")
def index():
    return jsonify(dict(version=__version__))


@app.route("/device/register", methods=['POST'])
def register_device():
    device = CameraDevice(**json.loads(request.data))
    try:
        device.validate()
        device_store.add(device)
        response = make_response()
        response.headers = dict(content_type="application/json")
        response.data = device.make_json_publicsafe(device)
        return response
    except ShieldException:
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
