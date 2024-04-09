# The purpose of this file is to establish the roles of the game. This will be imported in the main file
# TODO Figure out if you should be importing the database here or in the server
# TODO Figure out if there is a distinction between townsfolk and outsides

class Town():
	def __init__(self):
		self.alligence = "Townsfolk"
		self.guarded = False # Can change if Soldier/guarded by Monk

class Minions():
	def __init__(self):
		self.alligence = "Minions"

# Now what is below are the specific town roles. They will inherit the stuff above

class Soldier(Town):
	def __init__(self):
		self.guarded = True

class Slayer(Town):
	def __init__(self):
		self.target = None

	def target(self, target):
		self.target = target
		if target.alligence = "Minions":
			target.kill()

class Drunk(Town):
	def __init__(self, percieved_role):
		self.percieved_role = percieved_role
