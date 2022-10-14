import uuid

from flask import session, flash
from common.database import Database
import random


class User:
    def __init__(self, username, email, password, _id=None):
        _id = uuid.uuid4()
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def get_by_email(cls, email):
        """Check the database for a user by email"""
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def register(cls, username, email, password):
        """Registers users, by checking database if it exists, and if not it adds the user"""
        user = cls.get_by_email(email)
        print(user)
        if user is None:
            new_user = cls(username, email, password)
            new_user.save_user()
            # session['email'] = email
            # session['username'] = username
            return True
        else:
            flash("Email already in use")

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password

    @staticmethod
    def login(user_email):
        session['email'] = user_email
        session['username'] = User.get_by_email(user_email).username
        print(session["username"])

    @staticmethod
    def save_reset_token(email, token, time):
        """Saves the reset password token in the database"""
        Database.insert("tokens", {"email": email, "token": token, "time": time})

    @staticmethod
    def get_reset_token(email):
        """Gets the reset password token from the database"""
        data = Database.find_one("tokens", {"email": email})
        if data is not None:
            return data

    @staticmethod
    def update_password(email, password):
        """Used to update new password when tokens match"""
        Database.update_password("users", {"email": email}, {"$set": {"password": password}})

    def json(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    def save_user(self):
        """Saves the User to the database"""
        Database.insert("users", self.json())
