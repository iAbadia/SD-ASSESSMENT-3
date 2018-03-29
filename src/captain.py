import json
import uuid
from teammember import Teammember
import persistence as ps
from item import Item

class Captain(Teammember):

    def __init__(self, jcpt):
        # Create new ID if new squad
        if jcpt["uid"] == "":
            self.uid = uuid.uuid4().hex
        else:
            self.uid = jcpt["uid"]

        self.id = jcpt["id"]
        self.xp = jcpt["xp"]
        self.skills = jcpt["skills"]
        self.items = [Item(x) for x in jcpt["items"]]
        self.stats = jcpt["stats"]
        self.name = jcpt["name"]

        # Fill cost and tree from resources if valid captain
        if self.id != 0:
            cpts = ps.get_captains()

            for cpt in cpts:
                if self.id == cpt["id"]:
                    self.cost = cpt["cost"]
                    self.tree = cpt["tree"]

    def to_string(self):
        scpt = ""
        scpt += "Name: " + self.name + "\n"
        scpt += "ID:   " + self.id + "\n"
        scpt += "UID:  " + self.uid + "\n"
        scpt += "XP:   " + str(self.xp) 
        return scpt
    
    def to_json(self):
        jcpt = {}
        jcpt["uid"] = self.uid
        jcpt["id"] = self.id
        jcpt["stats"] = self.stats
        jcpt["xp"] = self.xp
        jcpt["items"] = [x.to_json() for x in self.items]
        jcpt["skills"] = self.skills
        jcpt["name"] = self.name
        return jcpt