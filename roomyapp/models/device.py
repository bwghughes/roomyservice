from datetime import datetime
from dictshield.document import Document
from dictshield.fields import StringField, UUIDField, DateTimeField


class Device(Document):
    guid = UUIDField(auto_fill=True)
    created_at = DateTimeField(default=datetime.now)
    #belongs_to = UUIDField(auto_fill=False, required=True)


class CameraDevice(Device):
    _public_fields = ['guid', 'created_at', 'location']
    location = StringField(required=True)

    def __init__(self, *args, **kwargs):
        super(CameraDevice, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<CameraDevice@{0}>".format(self.location)
