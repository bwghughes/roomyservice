#!/usr/bin/env python
import json
import uuid
from flask import request, jsonify, abort, make_response
from flask.ext.classy import FlaskView, route

from models.events import CameraEvent
from models.device import CameraDevice
from models.store import EventStore, DeviceStore

from schematics.base import TypeException


__version__ = "0.1"

event_store = EventStore()
device_store = DeviceStore()


class ApiView(FlaskView):

    def index(self):
        return jsonify(dict(version=__version__))

    @route("/device", methods=["POST"])
    def add(self):
        device = CameraDevice(**json.loads(request.data))
        try:
            device.validate()
            device_store.add(device)
            response = make_response()
            response.headers = dict(content_type="application/json")
            response.data = device.make_json_publicsafe(device)
            return response
        except TypeException, e:
            print e
            abort(405, 'Invalid payload')

    @route("/device/event/<device_id>/", methods=["POST"])
    def camera_event(self, device_id):
        camera_event = CameraEvent(**json.loads(request.data))
        # TODO: Write UUID converter and commit to Werkzeug Project
        if uuid.UUID(device_id) in device_store.devices():
            try:
                # Now we need to set it
                camera_event.device_id = device_id
                camera_event.validate()
                event_store.add(camera_event)
                return jsonify({'status': 'OK'})
            except TypeException, e:
                print e
                log.error("Invalid payload - {}".format(e))
                abort(405, 'Invalid payload')
        else:
            abort(404)
