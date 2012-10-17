#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.pardir)

from nose.tools import raises

from models.events import Event
from models.store import EventStore, InvalidObjectTypeForStore


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
