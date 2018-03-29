import json
import uuid
import persistence as ps


class Teammember:

    def __init__(self, jtmb, new=True):
        # Create new ID if new squad
        if new is True:
            self.uid = uuid.uuid4().hex
        elif jtmb["uid"] == "":
            self.uid = uuid.uuid4().hex
        else:
            self.uid = jtmb["uid"]

        self.id = jtmb["id"]
        if new is True:
            self.main = False
        else:
            self.main = jtmb["main"]
        self.stats = jtmb["stats"]
        self.name = jtmb["name"]

    def to_json(self):
        jmbr = {}
        jmbr["name"] = self.name
        jmbr["uid"] = self.uid
        jmbr["id"] = self.id
        jmbr["main"] = self.main
        jmbr["stats"] = self.stats
        return jmbr
    
    def to_string(self):
        return self.name + " | " + self.id + " | Main: " + str(self.main) 

    # Use this functions to increase/decrease stats (or hurt the member)
    def health(self, hlth):
        self.stats["health"] += hlth

    def move(self, mv):
        self.stats["move"] += mv

    def fight(self, fg):
        self.stats["fight"] += fg

    def shoot(self, sh):
        self.stats["shoot"] += sh

    def armour(self, arm):
        self.stats["armour"] += arm

    def morale(self, ml):
        self.stats["morale"] += ml

    def get_stat_health(self):
        return self.stats["health"]

    def get_stat_fight(self):
        return self.stats["fight"]
