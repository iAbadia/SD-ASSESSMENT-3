import json
import persistence as ps

class Fight:

    def __init__(self, squad_a, squad_b):
        self.a_squad = squad_a
        self.b_squad = squad_b
        self.turn = "a"

    def a_attack(self, uid_a, uid_b):
        # Check for turn
        if self.turn != "a":
            return None
        # Get damage from UID
        damage = self.a_squad.get_stat_fight(uid_a)

        # Inflict damage to UID
        self.b_squad.receive_damage(uid_b, damage)

    def b_attack(self, uid_b, uid_a):
        if self.turn != "b":
            return None
        # Get damage from UID
        damage = self.b_squad.get_stat_fight(uid_b)

        # Inflict damage to UID
        self.a_squad.receive_damage(uid_b, damage)

    def end_turn(self):
        if self.turn == "a":
            self.turn = "b"
        elif self.turn == "b":
            self.turn = "a"
    
    def end_game(self):
        # Save both squads
        ps.save_squad(self.a_squad.owner, self.a_squad.to_json())
        ps.save_squad(self.b_squad.owner, self.b_squad.to_json())
