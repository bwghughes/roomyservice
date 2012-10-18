from datetime import datetime
from dictshield.document import Document
from dictshield.fields import StringField, UUIDField, DateTimeField, EmailField


class User(Document):
    guid = UUIDField(auto_fill=True)
    name = StringField()
    email = EmailField()
    created_at = DateTimeField(default=datetime.now)
