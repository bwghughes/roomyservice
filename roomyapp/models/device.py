from datetime import datetime
from dictshield.document import Document
from dictshield.fields import StringField, UUIDField, DateTimeField


class Device(Document):
    guid = UUIDField(auto_fill=True)
    created_at = DateTimeField(default=datetime.now)


class CameraDevice(Device):
    _public_fields = ['guid', 'created_at', 'location_name']
    location_name = StringField()

    def __init__(self, *args, **kwargs):
        super(CameraDevice, self).__init__(*args, **kwargs)
