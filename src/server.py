import sqlite3 # Our database of choice is sqlite
import roles.py # This imports the roles that are previously defined

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

def setup(players):
	# TODO Assign roles to each player
	# Do POST requests to send the roles to each relevant player


def collect_player_info():
	# TODO Get information from the javascript side with get requests
	return None # SWITCH TO A LIST OF PLAYER NAMES, WITH EACH POSITION IN THE LIST CORRESPONDING TO THEIR NUMBER

if __name__ == '__main__':
	players = collect_player_info()
	setup(players)
	while True:
		day()
		night()
