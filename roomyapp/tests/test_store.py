#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.pardir)

from nose.tools import raises

from roomyapp.models.events import Event
from roomyapp.models.device import CameraDevice
from roomyapp.models.store import EventStore, DeviceStore, InvalidObjectTypeForStore


class TestEventStore(object):

    def setup(self):
        self.es = EventStore()
        self.e = Event(device_id="Hello")

    def teardown(self):
        pass

    def test_we_can_add_an_event_to_the_event_store(self):
        event = Event(device_id="Holy Moma")
        self.es.add(event)
        assert len(self.es) == 1

    def test_we_can_add_multiple_events_to_the_event_store(self):
        for x in xrange(10):
            event = Event(device_id="Device {}".format(x))
            self.es.add(event)
        assert len(self.es) == 10

    @raises(InvalidObjectTypeForStore)
    def test_we_can_add_only_event_types_to_the_events_store(self):
        not_an_event = dict()
        self.es.add(not_an_event)

    def test_we_can_find_by_guid(self):
        self.es.add(self.e)
        event = self.es.find_by_guid(self.e.guid)
        assert event is self.e


class TestDeviceStore(object):

    def setup(self):
        self.ds = DeviceStore()

    def teardown(self):
        pass

    def test_device_can_be_added(self):
        cd = CameraDevice()
        self.ds.add(cd)
        assert len(self.ds) == 1

    def test_device_is_in_devices(self):
        cd = CameraDevice()
        self.ds.add(cd)
        assert str(cd.guid) in self.ds.devices()

    @raises(InvalidObjectTypeForStore)
    def test_we_can_add_only_devices_to_the_device_store(self):
        not_a_device = dict()
        self.ds.add(not_a_device)
