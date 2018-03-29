import uuid
import json
from captain import Captain
from hierophant import Hierophant
from teammember import Teammember
from item import Item
import persistence as ps


class Squad:

    def __init__(self, jsquad):
        # Create new ID if new squad
        if jsquad["uid"] == "":
            self.uid = uuid.uuid4().hex
        else:
            self.uid = jsquad["uid"]

        self.name = jsquad["name"]
        self.owner = jsquad["owner"]
        self.private = jsquad["private"]
        self.credits = jsquad["credits"]
        self.stash = [Item(x) for x in jsquad["stash"]]
        self.roster = [Teammember(x) for x in jsquad["roster"]]
        self.captain = Captain(jsquad["captain"])
        self.hierophant = Hierophant(jsquad["hierophant"])

    def change_name(self, new_name):
        self.name = new_name

    def change_captain(self, new_captain):
        self.captain = new_captain

    def change_hierophant(self, new_hierophant):
        self.hierophant = new_hierophant

    def add_teammember(self, new_teammember_id):
        new_member = ps.get_squad_member(new_teammember_id)
        if new_member["cost"] <= self.credits:
            self.credits -= new_member["cost"]
            self.roster.append(Teammember(new_member, new=True))
            return True
        else:
            return False
        

    def del_teammember(self, teammember_uid):
        self.roster = [
            member for member in self.roster if member.uid == teammember_uid]

    def receive_damage(self, to_uid, amount):
        if self.hierophant.uid == to_uid:
            # Hieropahnt
            self.hierophant.health(-amount)
        elif self.captain.uid == to_uid:
            # Captain
            self.captain.health(-amount)
        else:
            # Teammember
            for mbr in self.roster:
                if mbr.uid == to_uid:
                    mbr.health(-amount)

    def get_stat_fight(self, uid):
        damage = 0
        if self.hierophant.uid == uid:
            # Hieropahnt
            damage = self.hierophant.get_stat_fight()
        elif self.captain.uid == uid:
            # Captain
            damage = self.captain.get_stat_fight()
        else:
            # Teammember
            damage = [x.get_stat_fight() for x in self.roster if x.uid == uid]
            damage = damage[0]
        return damage

    def to_json(self):
        jsqd = {}
        jsqd["uid"] = self.uid
        jsqd["owner"] = self.owner
        jsqd["private"] = self.private
        jsqd["name"] = self.name
        jsqd["credits"] = self.credits
        jsqd["roster"] = [x.to_json() for x in self.roster]
        jsqd["captain"] = self.captain.to_json()
        jsqd["hierophant"] = self.hierophant.to_json()
        jsqd["stash"] = [x.to_json() for x in self.stash]
        return jsqd

    def to_string(self):
        ssquad = "-------------- SQUAD ----------------\n"
        ssquad += "Name:    " + str(self.name) + "\n"
        ssquad += "Owner:   " + str(self.owner) + "\n"
        ssquad += "UID:     " + str(self.uid) + "\n"
        ssquad += "Private: " + str(self.private) + "\n"
        ssquad += "Credits:   " + str(self.credits) + "\n"
        ssquad += "------------ CAPTAIN ---------------\n"
        ssquad += self.captain.to_string() + "\n"
        ssquad += "----------- HIEROPHANT -------------\n"
        ssquad += self.hierophant.to_string() + "\n"
        ssquad += "------------- ROSTER ---------------\n"
        for member in self.roster:
            ssquad += member.to_string() + "\n"
        ssquad += "------------- STASH ----------------\n"
        for item in self.stash:
            ssquad += item.to_string() + "\n"

        return ssquad
