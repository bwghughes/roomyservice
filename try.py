import os
import hashlib
from datetime import datetime
from dictshield.document import Document
from dictshield.fields import StringField, UUIDField, DateTimeField, SHA1Field, EmailField

shared_private_key = os.environ.get('ROOMY_APPLICATION_KEY', None)

class Thing(Document):

    def create_signature(data):
        return hashlib.sha1(repr(data) + "," + shared_private_key).hexdigest()

    def verify_signature(data, signature):
        return signature == create_signature(data)

    guid = UUIDField(auto_fill=True)
    created_at = DateTimeField(default=datetime.now)
    name = StringField()
    email = EmailField()
    api_token = SHA1Field(default=create_signature(guid))




