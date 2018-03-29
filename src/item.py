import json
import uuid
import persistence as ps


class Item:

    def __init__(self, jitem):
        # Create new ID if new squad
        if jitem["uid"] == "":
            self.uid = uuid.uuid4().hex
        else:
            self.uid = jitem["uid"]

        self.id = jitem["id"]
        self.name = jitem["name"]
        self.cost = jitem["cost"]
        self.type = jitem["type"]
        self.value = jitem["value"]
        self.description = jitem["description"]

    def to_json(self):
        jitem = {}
        jitem["uid"] = self.uid
        jitem["id"] = self.id
        jitem["name"] = self.name
        jitem["cost"] = self.cost
        jitem["type"] = self.type
        jitem["value"] = self.value
        jitem["description"] = self.description
        return jitem

    def to_string(self):
        return self.name + " | " + self.id + " | " + str(self.cost) + " (cost) | " + str(self.value) + " (value)" 
