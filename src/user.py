import hashlib
import json
import persistence as ps


class User:

    def __init__(self, username, password):
        # Check if user exists, if not, create
        juser = ps.get_user(username)

        if hashlib.sha512(password).hexdigest() == str(juser["password"]):
            self.username = username
            self.about = juser["about"]
            self.passwd = juser["password"]
            self.valid = True
        else:
            self.valid = False

    def to_json(self):
        juser = {}
        juser["password"] = self.passwd
        juser["username"] = self.username
        juser["about"] = self.about
        return juser
