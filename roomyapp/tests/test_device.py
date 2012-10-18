#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.pardir)

from roomyapp.models.device import Device, CameraDevice
from roomyapp.models.store import UserStore


class TestDevice(object):

    def setup(self):
        self.d = Device()
        self.user_store = UserStore()

    def teardown(self):
        pass

    def test_device_has_an_id(self):
        assert self.d.guid

    def test_device_has_a_created_at_timestamp(self):
        assert self.d.created_at

    # def test_device_has_a_valid_user_associated_with_it(self):
    #     assert self.user_store.find_by_guid is self.d.belongs_to


class TestCameraDevice(object):

    def setup(self):
        self.cd = CameraDevice(location_name="Mill Lane")

    def teardown(self):
        pass

    def test_it_looks_like_a_camera_device(self):
        assert self.cd.location_name == "Mill Lane"

    def test_repr(self):
        assert repr(self.cd).startswith("<CameraDevice@")
