#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.pardir)

from roomyapp.models.device import Device, CameraDevice


class TestDevice(object):

    def setup(self):
        self.d = Device()

    def teardown(self):
        pass

    def test_device_has_an_id(self):
        assert self.d.guid

    def test_device_has_a_created_at_timestamp(self):
        assert self.d.created_at


class TestCameraDevice(object):

    def setup(self):
        self.cd = CameraDevice(location_name="Mill Lane")

    def teardown(self):
        pass

    def test_it_looks_like_a_camera_device(self):
        assert self.cd.location_name == "Mill Lane"

    def test_repr(self):
        assert repr(self.cd).startswith("<CameraDevice@")
