import json
import uuid
from teammember import Teammember
import persistence as ps
from item import Item

class Hierophant(Teammember):

    def __init__(self, jhpt):
        # Create new ID if new squad
        if jhpt["uid"] == "":
            self.uid = uuid.uuid4().hex
        else:
            self.uid = jhpt["uid"]

        self.id = jhpt["id"]
        self.xp = jhpt["xp"]
        self.skills = jhpt["skills"]
        self.items = [Item(x) for x in jhpt["items"]]
        self.stats = jhpt["stats"]
        self.name = jhpt["name"]

        # Fill cost and tree from resources if valid hierophant
        if self.id != 0:
            cpts = ps.get_captains()

            for cpt in cpts:
                if self.id == cpt["id"]:
                    self.cost = cpt["cost"]
                    self.tree = cpt["tree"]
    
    def to_string(self):
        shpt = ""
        shpt += "Name: " + self.name + "\n"
        shpt += "ID:   " + self.id + "\n"
        shpt += "UID:  " + self.uid + "\n"
        shpt += "XP:   " + str(self.xp) 
        return shpt
    
    def to_json(self):
        jhpt = {}
        jhpt["uid"] = self.uid
        jhpt["id"] = self.id
        jhpt["stats"] = self.stats
        jhpt["xp"] = self.xp
        jhpt["items"] = [x.to_json() for x in self.items]
        jhpt["skills"] = self.skills
        jhpt["name"] = self.name
        return jhpt