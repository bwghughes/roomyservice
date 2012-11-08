#!/usr/bin/env python
from datetime import datetime
from schematics.models import Model
from schematics.types import StringType, UUIDType, DateTimeType, IntType\
                             , URLType


class Event(Model):
    guid = UUIDType(auto_fill=True)
    device_id = StringType(max_length=36, required=True)
    timestamp = DateTimeType(default=datetime.now)


class CameraEvent(Event):
    count = IntType(required=True)
    image_location = URLType(default=None)

    def __init__(self, *args, **kwargs):
        super(CameraEvent, self).__init__(*args, **kwargs)
