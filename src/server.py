import sqlite3 # Our database of choice is sqlite
import roles.py # This imports the roles that are previously defined

class Player():
	def __init__(self, player_name : String, role):
		# TODO
		self.alive = True
		self.dead_vote = True
		self.player_name = player_name
		self.role = role

	def kill(self):
		self.alive = False

def day():
	# TODO figure out how to get messages from the front end
	wait_get/post_request from front end

def night():
	# TODO
	killed = Mafia gets to discuss and vote on who to kill
	killed.kill()

def voting():
	# TODO

def check_win(role_killed, method_of_killing):
	# TODO Everytime a player dies, we check to see if that ends the game
	if role_killed == "Virgin" and method_of_killing == "Hanged":
		print("The bad guys win!\n")
		exit()

def setup():
	# Connect to the database and make a cursor
	db = sqlite3.connect('roles.db')
	dbcursor = db.cursor()

	# Get the roles from the DB using the cursor
	dbcursor.execute("SELECT * FROM roles")
	roles = dbcursor.fetchall()

	# Assign the roles
	for role in roles:
		# TODO Finish this part!

	# Close
	db.close()

if __name__ == '__main__':
	setup()
	while True:
		day()
		night()
