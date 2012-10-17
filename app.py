import json
from flask import Flask
app = Flask(__name__)

from models.event import CameraEvent
from models.store import EventStore

event_store = EventStore()

@app.route("/event/camera/<device_id>", methods=["POST"])
def camera_event(device_id):
    payload = json.loads(request.data())
    camera_event = CameraEvent(device_id, payload.get('count'))
    return event_store.add(camera_event)

if __name__ == "__main__":
    app.run()