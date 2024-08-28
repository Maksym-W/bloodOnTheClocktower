# The purpose of this file is to establish the roles of the game.
# This will be imported in the main file
import sqlite3  # This is to get data for the roles


class Skeleton_role():
	def __init__(self):
		self.alive = True
		self.dead_vote = True
		self.alligence = None # Will be defined when inherited
		self.role_description = ""
		self.number = -1 # Will be modified according to which player gets what; -1 is placeholder

	def __str__(self) -> str:
		return "This player is the: " + self.__class__.__name__ + " role."

	def get_ability(self, role_name):
		# Connect to the SQLite database
		pass
		# conn = sqlite3.connect('game.db')
		# cursor = conn.cursor()

		# # Execute a query to get the ability based on the role name
		# cursor.execute("SELECT ability FROM roles WHERE name = ?", (role_name,)) # TODO FIX THIS QUERY
		# result = cursor.fetchone()

		# # Close the database connection
		# conn.close()

		# if result:
		# 	return result[0]  # Return the ability
		# else:
		# 	return None  # If no ability is found, return None

	def die(self):
		self.alive = False

	def self_voted(self):
		self.dead_vote = False

# Now what is below are the specific town roles. They will inherit the stuff above

class Chef(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.pairs = 0

	def scan_for_pairs(self):
		# TODO FIGURE OUT THE GAME LOGIC THEN IMPLEMENT IT HERE.
		# MAYBE NEEDS A LIST OR TUPLE. ALSO self.pairs += 1
		pass


class Empath(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.evil_neighbor = 0

	def update_neighboors(self):
		# TODO AGAIN, figure out the list thing for this to work.
		pass


class Fortune_Teller(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.false_register = None # TODO figure out which player is a false register!

	def investigate(self, player_1, player_2):
		# TODO implement game logic for players.
		pass


class Investigator(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.minion_role = None # TODO Assign this!
		self.players_suspected = (None, None)


class Librarian(Skeleton_role):
	def __init__(self):
		super().__init()
		self.outsider_role = None # TODO Assign this to a player!
		self.players_suspected = (None, None)


class Mayor(Skeleton_role):
	def __init__(self):
		super().__init__()


class Ravenkeeper(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.learned_role = {None: None} # TODO When coded, {Player: Role}


class Monk(Skeleton_role):
	def __init__(self):
		super().__init__()


class Soldier(Skeleton_role):
	def __init__(self):
		super().__init__()  # Initialize the base class
		self.guarded = True
		self.ability = self.get_ability("Soldier")  # Use the role name "Soldier" to fetch its ability


class Slayer(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.target = None

	def target(self, target):
		self.target = target
		if target.alligence == "Minions":
			target.kill()


class Washerwoman(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.town_role = None # TODO Still do this
		self.players_suspected = (None, None)


class Virgin(Skeleton_role):
	def __init__(self):
		super().__init__()
		self.nominated_person = None # TODO If none, then no one has been nominated yet


class Undertaker(Skeleton_role):
	def __init__(self):
		super().__init__()


class Drunk(Skeleton_role):
	def __init__(self, percieved_role):
		super().__init__()
		self.percieved_role = percieved_role
