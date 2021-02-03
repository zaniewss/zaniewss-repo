import time
import backstory
import sys
from StoryPaths import wizardpath
from StoryPaths import clericpath
from StoryPaths import knightpath
from StoryPaths import noblepath
from StoryPaths import roguepath
from StoryPaths import peasantpath
from Character import Player, Goblin

#Sets default stats
gold = 100
defense = 10
attack = 10
mana = 20
hp = 20


def delay_print(s):
	# Print one character at a time
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)


#WELCOME MESSAGE
print(
    'Welcome to the Fantasy Text Role Playing Game! Made by Samuel Zaniewski and Jack Zaniewski. ©2020'
)

time.sleep(2)

#CHOSE YOUR CHARACTER!
characterchoise = input(
    '\nWho do you want your character to be?\n1: Wizard\n2: Cleric (NOT FINISHED)\n3: Knight (NOT FINISHED)\n4: Noble (NOT FINISHED)\n5: Rogue (NOT FINISHED)\n6: Peasant (NOT FINISHED)\n\n> '
)

#Character Choices
if characterchoise == 'Wizard' or characterchoise == '1':
	charclass = 'Wizard'
elif characterchoise == 'Cleric' or characterchoise == '2':
	charclass = 'Cleric'
elif characterchoise == 'Knight' or characterchoise == '3':
	charclass = 'Knight'
elif characterchoise == 'Noble' or characterchoise == '4':
	charclass = 'Noble'
elif characterchoise == 'Rogue' or characterchoise == '5':
	charclass = 'Rogue'
elif characterchoise == 'Peasant' or characterchoise == '6':
	charclass = 'Peasant'
else:
	charclass = 'Wizard'

print('Your chosen class is', charclass)

time.sleep(1)

#Name the Character:
name = input("\nWhat is your character's name?\n> ")

#Tells the backstory to the character depending on the class they chose.
intromessage = '\nYou are ' + name + ' the ' + charclass + '.'
delay_print(intromessage)
time.sleep(1)

#Asks to skip intro:
delay_print('\n\nDo you want to skip the backstory?\n> ')
askforbeg = input('')

#Story then Pauses for user to read, if skipping then continues:
if askforbeg.lower() != 'yes':
	delay_print(backstory.background(charclass))
	delay_print('\n\nPress enter to continue:')

	yeet = input('')

#### DECLARES THE PLAYER ####
hero = Player(name, charclass, gold, mana, defense, attack, hp)
enemy = Goblin(name, defense, attack, hp)

#Storyline function running depending on paths
if charclass == 'Wizard':
	wizardpath.storyWiz(hero, enemy)
elif charclass == 'Cleric':
	clericpath.storyCleric()
elif charclass == 'Knight':
	knightpath.storyKnight()
elif charclass == 'Noble':
	noblepath.storyNoble()
elif charclass == 'Rogue':
	roguepath.storyRogue()
elif charclass == 'Peasant':
	peasantpath.storyPeasant()
