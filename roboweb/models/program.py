import datetime
import uuid
from common.database import Database


class Program:
    def __init__(self, g_code, user, _id=None):
        _id = uuid.uuid4()
        self.g_code = g_code()
        self.created = datetime.datetime.now()
        self.user = user

    class Meta:
        ordering = '-created'

    @classmethod
    def get_programs_by_user(cls, user):
        data = Database.find("programs", {"user": user})
        if data is not None:
            return cls(**data)

    def json(self):
        return {
            "g_code": self.g_code,
            "user": self.user
        }

    def save_program(self):
        """Saves the User to the database"""
        Database.insert("programs", self.json())

