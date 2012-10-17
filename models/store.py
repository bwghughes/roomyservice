#!/usr/bin/env python

from models.events import Event

class InvalidObjectTypeForStore(Exception):
    pass


class ObjectStore(object):
    def __init__(self, *args, **kwargs):
        self.store = {}

    def add(self, obj):
        self.store[obj.guid] = obj
        return True

    def find_by_guid(self, guid):
        return self.store.get(guid, None)

    def __len__(self):
        return len(self.store)


class EventStore(ObjectStore):
    def __init__(self, *args, **kwargs):
        super(EventStore, self).__init__(*args, **kwargs)

    def add(self, obj):
        if not isinstance(obj, Event):
            raise InvalidObjectTypeForStore("Object should be a {} but is a {}"
                                            .format(Event, type(obj)))
        super(EventStore, self).add(obj)
