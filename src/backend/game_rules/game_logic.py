import sqlite3 # Our database of choice is sqlite
import roles # This imports the roles that are previously defined TODO Finish it!

class game():
	def __init__(self, num_of_players : int) -> None:
		self.player_list = {i: None for i in range(1, num_of_players + 1)}
		self.game_in_progress = False
		self.day = True # Night is represented by False
		self.votes_left = 3
		self.news = [] # Announced at the start of every day TODO figure out how to store new

	def assign_roles(self):
		if self.game_in_progress == False:
			self.game_in_progress = True
			for player in self.player_list:
				self.player_list[player] = roles.Soldier() # TODO Replace with the roles from roles.py

	def begin_game(self):
		self.game_in_progress = True
		self.news.append("The game has begun")
		self.begin_day()
		
	def begin_day(self):
		for item in self.news:
			print(item) # might need to change this part
			self.news.remove(item)
		self.votes_left = 3
		self.day = True
	
	def voting(self, player):
		if self.votes_left <= 0:
			print("Invalid: No more votes are allowed in the day")
		else:
			self.votes_left -= 1
			print("We will wait 30 seconds for the accused to make their case.")
			wait(3000)
			votes = 0 # TODO Get the votes from the frontend
			if votes > 0: # TODO replace 0 with amount of alive players/2
				player.alive = False # TODO figure out if the game should continue in day or go to night after murder

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

	def advance_time(self):
		if self.day == True:
			self.day = False
		else
			self.day = True
			self.votes_left = 3


if __name__ == '__main__':
	print("This file contains methods for other files. Its not meant to be run\n")
	
