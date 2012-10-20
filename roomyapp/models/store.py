#!/usr/bin/env python

from roomyapp.models.events import Event
from roomyapp.models.device import Device


class InvalidObjectTypeForStore(Exception):
    pass


class DictBasedObjectStore(object):
    def __init__(self, *args, **kwargs):
        self.store = {}

    def add(self, obj):
        self.store[obj.guid] = obj
        return True

    def find_by_guid(self, guid):
        return self.store.get(guid, None)

    def all(self):
        return self.store.values()

    def __len__(self):
        return len(self.store)

    def __repr__(self):
        return "<DictBasedObjectStore: {0} objects>".format(len(self.store))


class EventStore(DictBasedObjectStore):
    def __init__(self, *args, **kwargs):
        super(EventStore, self).__init__(*args, **kwargs)

    def add(self, obj):
        if not isinstance(obj, Event):
            raise InvalidObjectTypeForStore("Object should be a {} but is a {}"
                                            .format(Event, type(obj)))
        super(EventStore, self).add(obj)


class DeviceStore(DictBasedObjectStore):
    def __init__(self, *args, **kwargs):
        super(DeviceStore, self).__init__(*args, **kwargs)

    def add(self, obj):
        if not isinstance(obj, Device):
            raise InvalidObjectTypeForStore("Object should be a {} but is a {}"
                                            .format(Device, type(obj)))
        super(DeviceStore, self).add(obj)

    def devices(self):
        return [str(key) for key in self.store.keys()]
