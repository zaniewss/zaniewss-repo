import random

#Spells Created (ALL SPELLS MP IS THEIR COST!)
class Spell:
	def __init__(spell, name, mp, dmg=0, heal=0):
		spell.name = name
		spell.mp = mp
		spell.heal = 0
		if name.lower() == "fireball":
			spell.dmg = random.randint(13,21)
			spell.mp = 20
		elif name.lower() == 'electricity':
			spell.dmg = random.randint(20,35)
			spell.mp = 30
		elif name.lower() == 'scald':
			spell.dmg = random.randint(20,30)
			spell.mp = 15
		elif name.lower() == 'healingaura':
			spell.heal = random.randint(10,15)
			spell.mp = 15