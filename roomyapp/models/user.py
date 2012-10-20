import os
import hashlib
from datetime import datetime
from dictshield.document import Document
from dictshield.fields import (StringField, UUIDField, DateTimeField,
                                SHA1Field, EmailField)

shared_private_key = os.environ.get('ROOMY_APPLICATION_KEY', "InSecureTestKey")

def create_signature(data):
    return hashlib.sha1(repr(data) + "," + shared_private_key).hexdigest()

def verify_signature(data, signature):
    return signature == create_signature(data)

class User(Document):
    guid = UUIDField(auto_fill=True)
    created_at = DateTimeField(default=datetime.now)
    name = StringField()
    email = EmailField()
    api_token = SHA1Field(default=create_signature(guid))

    def validate(self):
        if not verify_signature(selself.api_token):
            raise ShieldException("API Token invalid for this user.")
        super(User, self).validate(*args, **kwargs)

def main():
    t = User(name="Ben Hughes", email="bwghughes@gmail.com")
    print(t.api_token)
    print(t.validate())

if __name__ == '__main__':
    main()