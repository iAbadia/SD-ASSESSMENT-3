import json


def get_items():
    return json.load(open('resources/items.json'))


def get_captain_items():
    return get_items()["captain"]


def get_hierophant_items():
    return get_items()["hierophant"]


def get_captains():
    return json.load(open('resources/cpt-spec.json'))["list"]


def get_hierophants():
    return json.load(open('resources/hpt-spec.json'))["list"]


def get_squad_members():
    return json.load(open('resources/squad-members.json'))

def get_squad_member(id):
    members = get_squad_members()

    for member in members:
        if member["id"] == id:
            return member


def get_user_squads(owner):
    with open('resources/squads/'+owner+'.json') as squadsFile:
        return json.load(squadsFile)


def get_squad(owner, uid):
    # TODO: Check for file exists
    squads = get_user_squads(owner)
    for squad in squads:
        if squad["uid"] == uid:
            return squad
    # If squad not found, return None
    return None


def save_squad(owner, new_squad):
    squads = get_user_squads(owner)
    # Remove squad if already existent
    squads = [sq for sq in squads if sq["uid"] != new_squad["uid"]]
    squads.append(new_squad)
    # Save squads
    with open('resources/squads/'+owner+'.json', 'w') as squadsFile:
        json.dump(squads, squadsFile)


def get_config():
    return json.load(open('resources/config.json'))


def save_config(new_config):
    with open("resources/config.json", "w") as configFile:
        json.dump(new_config, configFile)


def get_users():
    return json.load(open('resources/users.json'))["list"]


def get_user(username):
    # Check if user exists, if not, create
    usrs = get_users()

    for usr in usrs:
        if username == usr["username"]:
            return usr
    # If not found, return None
    return None


def save_user(new_user):
    users = get_users()
    # Remove squad if already existent
    users = [us for us in users if us["username"] != new_user["username"]]
    users.append(new_user)
    users = {"list": users}
    # Save squads
    with open('resources/users.json', 'w') as usersFile:
        json.dump(users, usersFile)
