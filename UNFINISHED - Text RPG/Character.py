import random

class Player:
	def __init__(self, name, race, gold, mana, defense, attack, hp):
		self.name = name
		self.race = race
		self.gold = 100
		self.mana = 20
		self.defense = 10
		self.attack = 10
		self.hp = 20

class Goblin:
	def __init__(enemy, name, defense, attack, hp):
		enemy.name = Goblin
		enemy.defense = random.randint(10,18)
		enemy.attack = random.randint(2,8)
		enemy.hp = random.randint(13,24)