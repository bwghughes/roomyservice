from datetime import datetime
from schematics.models import Model
from schematics.types import StringType, UUIDType, DateTimeType


class Device(Model):
    guid = UUIDType(auto_fill=True)
    created_at = DateTimeType(default=datetime.now)
    #belongs_to = UUIDField(auto_fill=False, required=True)


class CameraDevice(Device):
    _public_fields = ['guid', 'created_at', 'location']
    location = StringType(required=True)

    def __init__(self, *args, **kwargs):
        super(CameraDevice, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<CameraDevice@{0}>".format(self.location)
