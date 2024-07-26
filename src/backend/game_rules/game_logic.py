import sqlite3 # Our database of choice is sqlite
#import roles # This imports the roles that are previously defined TODO Finish it!

class game():
	def __init__(self, num_of_players : int) -> None:
		self.player_list = {i: None for i in range(1, num_of_players + 1)}
		self.game_in_progress = False
		self.day = True # Night is represented by False

	def assign_roles(self):
		if self.game_in_progress == False:
			self.game_in_progress = True
			for player in self.player_list:
				self.player_list[player] = None # TODO Replace with the roles from roles.py
		
	def day(self):
		# TODO Announce the news from last night
		# TODO Set up voting
		pass
	
	def night(self):
		# TODO Set up murders
		# TODO Set up investigation
		pass

	def check_win(role_killed, method_of_killing):
		# TODO Everytime a player dies, we check to see if that ends the game
		if role_killed == "Virgin" and method_of_killing == "Hanged":
			print("The bad guys win!\n")
			exit()
		pass


if __name__ == '__main__':
	print("This file contains methods for other files. Its not meant to be run\n")
	
