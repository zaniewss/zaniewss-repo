def background(charclass):
	bg = ""

	if charclass == 'Wizard':
		bg = "\n\nYou are a powerful Wizard, training to empower yourself with magic spells and enchantments since you were but a wee lad. On your 5th birthday, you realized you had magical powers when you blew out your candles and then followed up and re lit them with your fingertips. Since then you have mastered the arts of fire spells, electric blade enchantments, defensive iron skin enhancements, and many more spells. However, there is one spell you have yet to learn, resurrection. For your dear brother, Jack, you shall set off into the forest of 1000 shadows, to find the necromancer's spell of resurrection, to bring your brother back who died saving the princess who now commands the very castle walls you inhabit upon."

	elif charclass == 'Cleric':
		bg = "\n\nYou are a Cleric working day in day out at the towns holy church to become one with the gods. One day when praying to the lord for a squires forgiveness for betraying the King, rumor starts to spread that the Void Lord Malice has stolen the church's only supply of holy water to resurrect the bewildered hell hound to feast upon the Villagers of the town. You have to set off on an epic quest to retrieve the stolen holy water before the Void Lord Malice causes the Villagers to be Dog Treats for some bad muts."

	elif charclass == 'Knight':
		bg = '\n\nSince the age of 11 you have been fascinated with being a knight of the royal guard. You have been training since. Fencing and sword fighting at the chance you get. Flash forward about 10 years later at the age of 21. You are now a top tier holy knight, sworn to protect the princess with your life. She has been captured by the evil lord Youssef the Peasant. You shall set off on an epic quest throughout the lands of Eternia, to save Princess Elementria.'

	elif charclass == 'Noble':
		bg = '\n\nE'

	elif charclass == 'Rogue':
		bg = '\n\nYou are a sneaky one. You have been through a lot. Mom juggling addiction after addiction, Dad constantly screaming at you, Step mom always nagging about what you have to do. That is why you ended up so rebellious. You stole your first candy bar at the age of 7, now you are sneaking around in the alleyways waiting for your next big catch for something worth a little more than a candy bar.'

	elif charclass == 'Peasant':
		bg = "\n\nYou have never been one to be lucky. Lost your parents in a freak car accident at the age of 9, been roaming the streets, not thinking about where you will be sleeping tonight. You follow life day by day, dealing with the obstacles that come your way as they come. And as they come they go. You just live in the moment. You only get money by asking those kind enough to give to the poor, maybe a meal or two from a homeless shelter, but then it's back onto the streets for you."

	return bg
