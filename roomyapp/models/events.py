#!/usr/bin/env python
from datetime import datetime
from dictshield.document import Document
from dictshield.fields import StringField, UUIDField, DateTimeField, \
                              IntField, URLField


class Event(Document):
    guid = UUIDField(auto_fill=True)
    device_id = StringField(max_length=36, required=True)
    timestamp = DateTimeField(default=datetime.now)


class CameraEvent(Event):
    count = IntField(required=True)
    image_location = URLField(default=None)

    def __init__(self, *args, **kwargs):
        super(CameraEvent, self).__init__(*args, **kwargs)
