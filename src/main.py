from captain import Captain
from hierophant import Hierophant
import config as cfg
from item import Item
import persistence as ps
from squad import Squad
import teammember as tm
from user import User
from fight import Fight
import hashlib as hb
import random as rng


def simulate():
    # Initialize random
    rng.seed()

    # Try two user logins
    user_login()

    # Modify user
    edit_user()

    # Edit config
    edit_config()

    # Edit Squad
    edit_squad()

    # Simulate battle
    simulate_fight()


def edit_user():
    # Edit user about section
    print
    print("############################################")
    print("################ EDIT USER #################")
    print("############################################")

    username_one = "user1"
    password_one = "user1"

    # user1 logins successfuly
    user_one = User(username_one, password_one)
    if not user_one.valid:
        print("User1 did not authenticate!!")
        exit()
    else:
        print("User1 authenticated!")

    # Show current user1 about
    print("Old user1 about: "+user_one.about)

    # Update user1 about
    user_one.about = "This is the new user1 about [" + \
        str(rng.randint(0, 1000))+"]"

    # Save user state
    ps.save_user(user_one.to_json())

    # Delete user and re-login
    del user_one

    user_one = User(username_one, password_one)
    if not user_one.valid:
        print("User1 did not authenticate!!")
        exit()
    else:
        print("User1 authenticated!")

    # Show new user1 about
    print("New user1 about: "+user_one.about)

    # Logout
    del user_one


def edit_config():
    # Edit configuration
    print
    print("############################################")
    print("############### EDIT CONFIG ################")
    print("############################################")

    # Print current config
    configuration = cfg.Config()

    print("INITIAL CONFIGURATION")
    print("---------------------")
    print("Colorblind:    " + str(configuration.get_colorblind()))
    print("Lowres:        " + str(configuration.get_colorblind()))
    print("Reduceflicker: " + str(configuration.get_colorblind()))

    # Update (invert)
    configuration.set_colorblind(not configuration.get_colorblind())
    configuration.set_lowres(not configuration.get_lowres())
    configuration.set_reduceclicker(not configuration.get_reduceflicker())

    # Delete configuration object
    del configuration

    # Create again and check
    configuration = cfg.Config()
    print
    print("FINAL CONFIGURATION")
    print("---------------------")
    print("Colorblind:    " + str(configuration.get_colorblind()))
    print("Lowres:        " + str(configuration.get_colorblind()))
    print("Reduceflicker: " + str(configuration.get_colorblind()))

    # Delete config object
    del configuration

def edit_squad():
    # Two users login, one of them fails and retries
    print
    print("############################################")
    print("################ EDIT SQUAD ################")
    print("############################################")

    # Load Squad
    username = "user1"
    squad_uid = "1f3b187ca90344d383b486a7ebdb355c"
    test_squad = create_squad(username, squad_uid)

    # List members
    print
    print(test_squad.to_string())
    print

    # Edit members (add one teammember) that costs too much
    too_expensive_member = "005-00004"
    if test_squad.add_teammember(too_expensive_member):
        print("Member " + too_expensive_member + " added!")
    else:
        print("Member " + too_expensive_member + " not added!")

    # Check if it was added
    print
    print(test_squad.to_string())
    print

    # Add a in-budget member
    reasonably_expensive_member = "005-00003"
    if test_squad.add_teammember(reasonably_expensive_member):
        print("Member " + reasonably_expensive_member + " added!")
    else:
        print("Member " + reasonably_expensive_member + " not added!")

    # Save squad
    ps.save_squad(test_squad.owner, test_squad.to_json())

    # Create again and check if teammember is saved
    del test_squad
    test_squad = create_squad(username, squad_uid)
    print(test_squad.to_string())


def simulate_fight():
    # Two users login, one of them fails and retries
    print
    print("############################################")
    print("############## SIMULATE FIGHT ##############")
    print("############################################")

    # Login both users
    username_one = "user1"
    password_one = "user1"
    username_two = "user2"
    password_two = "user2"
    user_one = User(username_one, password_one)
    if not user_one.valid:
        print("User1 did not authenticate!!")
        exit()
    else:
        print("User1 authenticated!")
    user_two = User(username_two, password_two)
    if not user_two.valid:
        print("User2 did not authenticate!!")
        exit()
    else:
        print("User2 authenticated!")

    # Get their squads
    squad_one = create_squad(
        user_one.username, "7911ceb9f0f546c2b49bff6a8bd7044d")
    squad_two = create_squad(
        user_two.username, "b3f175ec05564cdbbb8545bf6f26b469")

    print("User1 will use Squad <" + str(squad_one.uid)+">")
    print("User2 will use Squad <" + str(squad_two.uid)+">")
    # Create Fight

    test_fight = Fight(squad_one, squad_two)

    # Attack
    b_hpt_prev_health = squad_two.hierophant.get_stat_health()
    a_cpt_dmg = squad_one.captain.get_stat_fight()
    print("Squad B Hierophant health pre-fight: " + str(b_hpt_prev_health))
    print("Squad A Captain attacks with " + str(a_cpt_dmg) + " damage")
    test_fight.a_attack(squad_one.captain.uid, squad_two.hierophant.uid)
    
    # End fight and save squads
    test_fight.end_game()

    # Get Squad b again an check Hierophant health
    del squad_two
    squad_two = create_squad(
        user_two.username, "b3f175ec05564cdbbb8545bf6f26b469")
    
    b_hpt_post_health = squad_two.hierophant.get_stat_health()
    
    print("Squad B Hierophant health post-fight: " + str(b_hpt_post_health))


def create_squad(owner, squad_uid):
    # Retreive data from persistance and parse to Objects
    jsquad = ps.get_squad(owner, squad_uid)
    if jsquad is None:
        print("Squad does not exist!")
        exit()

    return Squad(jsquad)


def user_login():
    # Two users login, one of them fails and retries
    print
    print("############################################")
    print("################ USER LOGIN ################")
    print("############################################")

    # User1 got it right
    username_one = "user1"
    password_one = "user1"

    # User2 wrote the password wrong (the right one is user2)
    username_two = "user2"
    password_two = "user3"

    # User1 logins successfuly (Notice we store hashes, not plain passwords)
    user_one = User(username_one, password_one)
    if not user_one.valid:
        print("User1 did not authenticate!!")
        exit()
    else:
        print("User1 authenticated!")

    # User2 fails the first time
    user_two = User(username_two, password_two)
    if not user_two.valid:
        print("User2 failed login!")
        # User2 corrects its password and tries again
        password_two = "user2"
        user_two = User(username_two, password_two)
        if not user_two.valid:
            print("User2 did not authenticate!!")
            exit()
        else:
            print("User2 authenticated!")

    # Logout
    del user_one
    del user_two


if __name__ == "__main__":
    """If run as main program, start simulation
    """
    simulate()
