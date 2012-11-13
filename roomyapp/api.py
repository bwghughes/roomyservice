#!/usr/bin/env python
import json
import uuid
from flask import request, jsonify, abort, make_response
from flask.ext.classy import FlaskView, route
from schematics.base import TypeException

from .models.events import CameraEvent
from .models.device import CameraDevice
from .models.store import EventStore, DeviceStore

event_store = EventStore()
device_store = DeviceStore()

__version__ = "0.1"


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
    def camera_event(self, device_id=None):
        try:
            camera_event = CameraEvent(**request.json)
            camera_event.device_id = device_id
            camera_event.validate()
            event_store.add(camera_event)
            return jsonify({'status': 'OK'})
        except TypeException, e:
            print e
            log.error("Invalid payload - {}".format(e))
            abort(405, 'Invalid payload')

    def before_camera_event(self, *args, **kwargs):
        if not uuid.UUID(kwargs.get('device_id')) in device_store.devices():
            abort(404)
