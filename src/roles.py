# The purpose of this file is to establish the roles of the game.
# This will be imported in the main file
import sqlite3  # This is to get data for the roles


class Skeleton_role():
	def __init__(self):
		pass

	def get_ability(self, role_name):
		# Connect to the SQLite database
		conn = sqlite3.connect('game.db')
		cursor = conn.cursor()

		# Execute a query to get the ability based on the role name
		cursor.execute("SELECT ability FROM roles WHERE name = ?", (role_name,)) # TODO FIX THIS QUERY
		result = cursor.fetchone()

		# Close the database connection
		conn.close()

		if result:
			return result[0]  # Return the ability
		else:
			return None  # If no ability is found, return None

# Now what is below are the specific town roles. They will inherit the stuff above


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


class Drunk(Skeleton_role):
	def __init__(self, percieved_role):
		super().__init__()
		self.percieved_role = percieved_role
