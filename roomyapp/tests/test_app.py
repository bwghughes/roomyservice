#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.pardir)

import json
from flask.ext.testing import TestCase
from roomyapp.app import app
from roomyapp.models.device import CameraDevice


class TestEventAPI(TestCase):

    def create_app(self):
        #app.config['TESTING'] = True
        return app

    def test_we_can_get_the_index(self):
        response = self.client.get("/")
        print response.data
        self.assert_200(response)

    def test_we_cant_post_a_camera_event_for_a_non_existent_device(self):
        response = self.client.post("/event/camera/some_cock_and_bull",
                                    data=json.dumps(dict(count=1)),
                                    content_type="application/json")
        self.assert_404(response)

    def test_we_can_post_an_event_for_an_existing_device(self):
        response = self.client.post("/device/register",
                                    data=json.dumps(dict(location="Mill Lane")),
                                    content_type="application/json")
        new_device = CameraDevice(**response.json)
        url = "/event/camera/{0}".format(new_device.guid)
        print url
        response = self.client.post(url, data=json.dumps(dict(count=1)),
                                    content_type="application/json")
        self.assert_200(response)
        self.assertEquals(response.json, {"status": "OK"})


class TestDeviceAPI(TestCase):

    def create_app(self):
        #app.config['TESTING'] = True
        return app

    def test_we_can_add_a_new_device(self):
        payload = json.dumps(dict(location="Mill Lane"))
        response = self.client.post("/device/register", data=payload,
                                    content_type="application/json")
        self.assert_200(response)
        self.assertIn('location', response.json.keys())

    def test_we_bork_on_adding_a_new_device_with_a_wonky_payload(self):
        payload = json.dumps(dict(wonky="donkey"))
        response = self.client.post("/device/register", data=payload,
                                    content_type="application/json")
        self.assert_405(response)
