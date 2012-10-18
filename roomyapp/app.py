#!/usr/bin/env python
import json
from logbook import Logger
from flask import Flask, request, jsonify, abort, make_response, render_template
from dictshield.base import ShieldException

from models.events import CameraEvent
from models.device import CameraDevice
from models.store import EventStore, DeviceStore


app = Flask(__name__)
log = Logger(__name__)
__version__ = "0.1"

event_store = EventStore()
device_store = DeviceStore()


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
    camera_event = CameraEvent(**json.loads(request.data))
    if device_id in device_store.devices():
        try:
            # Now we need to set it
            camera_event.device_id = device_id
            camera_event.validate()
            event_store.add(camera_event)
            return jsonify({'status': 'OK'})
        except ShieldException, e:
            print e
            log.error("Invalid payload - {}".format(e))
            abort(405, 'Invalid payload')
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
