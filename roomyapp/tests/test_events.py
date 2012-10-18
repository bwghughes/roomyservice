#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.pardir)

from roomyapp.models.events import Event, CameraEvent


class TestEvent(object):

    def setup(self):
        self.e = Event(device_id="Hello")

    def teardown(self):
        pass

    def test_event_has_a_device_id(self):
        assert self.e.device_id
        assert self.e.timestamp

    def test_event_has_a_timestamp(self):
        assert self.e.timestamp


class TestCameraEvent(object):
    def setup(self):
        self.ce = CameraEvent(device_id="kjwhk", count=2)

    def teardown(self):
        pass

    def test_camera_event_has_a_count(self):
        assert isinstance(self.ce.count, int)
        assert self.ce.count == 2

    def test_camera_event_is_an_event(self):
        assert isinstance(self.ce, Event)


