import sys, time
from Character import Player, Goblin
from colorama import Fore
import random
from Spell import Spell

#Delay Printer
def delay_print(s):
	# Print one character at a time
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)

def show_places(list_of_places):
	for i in range(0, len(list_of_places)):
		print(list_of_places[i])

#Story:
def storyWiz(player, enemy):

	print('\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== ')
	delay_print('\n\nAs you stumble out of your home you’re met with a traveling trader that will trade you 28 gold for a mana orb. Do you accept?')

	#Asks the user if they want to buy the Mana Orb, if bought, +2 dmg and +3 mp
	choice = input('\n\n(Yes or No) \n> ')

	if choice.lower() == 'yes':
		player.gold = player.gold - 28
		player.attack = player.attack + 2
		player.mana = player.mana + 3
		delay_print('You purchased the mana orb. Displaying new Stats:\n')
		time.sleep(2)
		printnewstats = '\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== '
		print(printnewstats)
		delay_print('As you approach the trader for said orb, you start to feel the mana power flowing through your veins;')

		#Tells user how much their damage and mana power increases
		time.sleep(1)
		addstatsmessage = Fore.GREEN + '\n\n+2 dmg + 3 mp  ' + Fore.RESET
		delay_print(addstatsmessage)
	else:
		delay_print('\nYou decline the offer and continue to the village.')
		time.sleep(1)

	#Places to visit
	places = ['The Holy Church','The Armory','The Forgery', 'The Brewery', 'Leave for the Forest']
	delay_print('\n\nAs you enter the village there are many places you can visit before you go to the Forest. ')
	while True:
		delay_print("Where would you like to go?\n\n")

		#List places
		show_places(places)

		destination = input('\n> ')

		#Destinations before Forest:

		#The Holy Church
		if destination.lower() == 'the holy church' or destination.lower() == '1':
			delay_print('\nYou head into the Holy Church.')
			time.sleep(1)

			delay_print('\n\nYou walk up to the Holy Priest. Do you ask for his blessing?')
			yeet = input('\n\n> ')

			if yeet.lower() == 'yes':
				if player.attack <= 10:
					player.hp = player.hp + 5
					player.mana = player.mana + 3
					delay_print('The Holy Priest offers his blessing on the dangerous path ahead.')
					addstatsmessage = Fore.GREEN + '\n+5 hp and +3 mp' + Fore.RESET
					delay_print(addstatsmessage)
					print('\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== ')
					places.remove('The Holy Church')
				else:
					delay_print('The Holy Priest turns down your request for his blessing... Maybe if your dmg was lower...')

		#The Armory
		elif destination.lower() == 'the armory' or destination.lower() == '2':
			delay_print("\nYou enter the armory and hear the bell ring that's attached to the door behind you. The Armorer welcomes you and asks if you want his newest pair of armor it costs 57 Gold. Do you want to buy the armor?")
			
			yeet = input('\n\n> ')

			if yeet.lower() == 'yes':
				if player.gold >= 57:
					player.gold = player.gold - 57
					player.defense = player.defense + 8
					delay_print('\nYou take the Armorers bargin and purchase the armor set.')
					addstatsmessage = Fore.GREEN + '\n+8 def' + Fore.RESET
					delay_print(addstatsmessage) 
					print('\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== ')
					places.remove('The Armory')
				else:
					delay_print("You don't have enough gold to purchase the armor set.")

		#The Forgery
		elif destination.lower() == 'the forgery' or destination.lower() == '3':
			delay_print('\nAs you enter the Forgery a chemical aroma fills the air. The Forger is working on his next piece of weaponry as you approach him. He is making a blade of sharpness. Do you want to ask to purchase his blade? (42 Gold)\n\n> ')
			yeet = input()
			if yeet.lower() == 'yes':
				if player.gold >= 42:
					delay_print('You purchase the sword. It feels amazing holding it out ready for combat.')
					player.gold = player.gold - 42
					player.attack = player.attack + 6
					player.defense = player.defense + 2
					addstatsmessage = Fore.GREEN + '\n\n+6 dmg and +2 def' + Fore.RESET
					delay_print(addstatsmessage)
					print('\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== ')
					places.remove('The Forgery')
				else:
					delay_print('You do not have enough gold to purchase!')
			else:
				delay_print('You leave the Forgery without saying a word...')

		#The Brewery
		elif destination.lower() == 'the brewery' or destination.lower() == '4':
			delay_print('\nYou enter the Brewery and instantly get the scent of magical potions flowing into your nose. The Chemist sitting behind the counter has a glass cabinet showing off the multicolored potions he has brewed. He has Mana Potions for 15 Gold, Health Potions for 30 Gold, and IronSkin Potions for 20 Gold. What do you want to purchase?')

			yeet = input('\n\n> ')

			if 'mana' in yeet.lower():
				player.gold = player.gold - 15
				player.mana = player.mana + 5
				delay_print('\nYou purchased the Mana Potion.')
				addstatsmessage = Fore.GREEN + '\n+5 mp\n' + Fore.RESET
				delay_print(addstatsmessage)
				print('\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== ')
			if 'health' in yeet.lower():
				player.gold = player.gold - 30
				player.hp = player.hp + 5
				delay_print('\nYou purchased the Health Potion.')
				addstatsmessage = Fore.GREEN + '\n+5 hp\n' + Fore.RESET
				delay_print(addstatsmessage)
				print('\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== ')
			if 'ironskin' in yeet.lower():
				player.gold = player.gold - 20
				player.defense = player.defense + 5
				delay_print('\nYou purchased the Ironskin Potion.')
				addstatsmessage = Fore.GREEN + '\n+5 def\n' + Fore.RESET
				delay_print(addstatsmessage)
				print('\n====================\nName: ' + player.name + Fore.MAGENTA + '\nHP: ' + str(player.hp) + Fore.GREEN + '\nClass: ' + player.race + Fore.YELLOW + '\nGold: ' + str(player.gold) + Fore.LIGHTBLUE_EX + '\nMana: ' + str(player.mana) + Fore.BLUE +'\nDef: ' + str(player.defense) + Fore.RED + '\nDmg: ' + str(player.attack) + Fore.RESET + '\n==================== ')

		else:
			#Leave straight to the forest:
			delay_print('\nYou make your way to the entrance of the gloom seeming forest.')
			time.sleep(1)
			break
	
	#Continuing after approaching the forest
	printgobmsg = '\nAs you follow the path ahead you encounter a goblin, (' + Fore.RED + str(enemy.hp) + ' hp' + Fore.RESET + ') stealing from a young man. Do you fight or flee?'
	delay_print(printgobmsg)
	fof = input('\n\n> ')


#Combat
	if fof.lower() == 'fight':
			while enemy.hp > 0:
				waitToContinue = input('\nWhat do you want to do? \n\nFight \nSpells \nFlee\n\n> ')

			#Battle options:

				#Fighting
				if waitToContinue.lower() == 'fight':
					delay_print('\nYou ready your blade.')
					attack = '\nYou attack the goblin. You dealt ' + Fore.GREEN + str(player.attack) + ' dmg' + Fore.RESET
					delay_print(attack)
					time.sleep(1)
					enemy.hp = enemy.hp - player.attack
					if enemy.hp <= 0:
						player.gold = player.gold + random.randint(100,200)
						victory = '\n\nYou defeated the goblin! \n\nYou now have ' + Fore.YELLOW + str(player.gold) + ' Gold!\n' + Fore.RESET
						time.sleep(2)
						delay_print(victory)
						break
					enemyhealthleft = '\nThe goblin has ' + Fore.RED + str(enemy.hp) + ' hp' + Fore.RESET
					delay_print(enemyhealthleft)
					time.sleep(1)
					player.hp = player.hp - enemy.attack 
					enemydealdamage = '\nThe goblin dealt ' + Fore.RED + str(enemy.attack) + ' dmg' + Fore.RESET
					delay_print(enemydealdamage)
					if player.hp <= 0:
						print(Fore.RED + '\n\nYou Died Game Over. Reload to try again!' + Fore.RESET)
						exit()
					time.sleep(1)
					playerhpmsg = '\nYou have ' + Fore.MAGENTA + str(player.hp) + ' hp' + Fore.RESET
					delay_print(playerhpmsg)
				

				#Spell Casting
				elif waitToContinue.lower() == 'spells':
					delay_print('Spells are not finished yet!')


				#Fleeing
				elif waitToContinue.lower() == 'flee':
					delay_print('\nYou run from the goblin.')
					time.sleep(1)
					break 

				else:
					delay_print('\nYou ready your blade.')
					while enemy.hp > 0:
						attack = '\nYou attack the goblin. You dealt ' + Fore.GREEN + str(player.attack) + ' dmg' + Fore.RESET
						delay_print(attack)
						time.sleep(1)
						enemy.hp = enemy.hp - player.attack
						if enemy.hp <= 0:
							player.gold = player.gold + random.randint(100,200)
							victory = '\n\nYou defeated the goblin! \n\nYou now have ' + Fore.YELLOW + str(player.gold) + ' Gold!\n' + Fore.RESET
							time.sleep(2)
							delay_print(victory)
							break
						enemyhealthleft = '\nThe goblin has ' + Fore.RED + str(enemy.hp) + ' hp' + Fore.RESET
						delay_print(enemyhealthleft)
						time.sleep(1)
						player.hp = player.hp - enemy.attack 
						enemydealdamage = '\nThe goblin dealt ' + Fore.RED + str(enemy.attack) + ' dmg' + Fore.RESET
						delay_print(enemydealdamage)
						if player.hp <= 0:
							print(Fore.RED + '\n\nYou Died Game Over. Reload to try again!' + Fore.RESET)
							exit()
						time.sleep(1)
						playerhpmsg = '\nYou have ' + Fore.MAGENTA + str(player.hp) + ' hp' + Fore.RESET
						delay_print(playerhpmsg)

#If user chose not to fight they slip past the goblin
	else:
		delay_print("You escape past the goblin and enter the forest… let’s hope this man doesn’t remember your face… ")
	
	time.sleep(2)

	delay_print('\n\nYou start walking down the path as the gravel road in front if you starts drawing darker due to the tall trees blocking the sun. A chill runs down your spine.')

	time.sleep(2)

#Fork in the road.
	delay_print('\nYou come to a cross in the path, you can go left, right, or look around at your surroundings. What do you want to do?\n\n')

	crossing = ['Left', 'Right', 'Look around']

	show_places(crossing)

	crosspaths = input('\n> ')