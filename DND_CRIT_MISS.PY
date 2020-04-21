"""
( . Y . )

A MAXIMUM EFFORT PRODUCTION!!!!!!!!!!!!!!!!!!!!!!
Critical Miss Calculator
[1-10]

---------------------------------SCALE OF DAMAGE---------------------------------------

1-5 No Damage               No issues

6-9 Minor Damage            Blunt: -1 HIT / -1 DMG
							Edged/Piercing: -2 DMG
							Bow/Xbow: -2 HIT

10  Weapon Breaks           Can club somebody with the broken remains (-4 HIT / d4 no mod. Dmg)  

---------------AT THE END OF EVERY LOOP DISPLAY **WEAPON REPAIR COST**-------------------
TYPE                        COST

SLASH/PIERCE/BLUNT*         > Remove Minor Damage:  50% of new / 3d8 Hours
							> Repair Broken: 80% of new / 2d4 Days
							* S/P/B - If the weapon is a Martial weapon, requires a [Smithy with Martial Training] to repair.

BOW**                       > Remove Minor Damage:   20% of new / 2d6 Hours
							> Repair Broken: Not possible
							** Bow - Any [bowyer fletcher] can repair minor damage. Bows (due to flex nature of wood) can't be fixed if broken.

CROSSBOW***                 > Remove Minor Damage:   70% of new / 1d4 Hours
							> Repair Broken: 90% of new / 2d4 Hours
							*** Only a trained [War Engineer] can repair a Crossbow

---------------------------------ARMOR DAMAGE REPAIR--------------------------------------

* Every 100 damage taken degrades player's armor, causing it to lose 1 point of AC protection
* Once a suit of armor loses all of it's AC protection points, it is destroyed
ARMOR TYPE              REPAIR COST

LEATHER                 40% of New + 10% per AC point lost / 1d4 Hours
METAL                   50% of New + 10% per AC point lost / 2d6 Hours
SCALE                   60% of New + 10% per AC point lost / 1d4 Days
PLATE                   80% of New + 10% per AC point lost / 2d4 Days

Heavily damaged expensive armor (Plate) it could be more expensive to repair than to order a new suit.
It would take far less time then having a new suit custom built though (1d6 Weeks)

------------------------------------------------------------------------------------------
"""

#Critical hits calculator
#1-6 Target is stunned for their next round
#   No special effect
#---------------------------------------------
#7-10 Savage Arm Strike
#   Roll any dice, EVENS means (primary arm) / ODDS (weak arm)
#   Roll Arm Strike Table
#   1-5	Muscle/Joint damage
#       M/R/S: (-4ATK), DC15CON for active concentration spells
#   6	Hand amputation	Melee: Off-hand gets (-8ATK)/(-4DMG)
#       Range: Unable to use bows, (-8ATK)/(-4DMG), 3 round load on Xbows
#       Spell: Any spells that have somatic components have 50% fail rate
#           	* Muscle/Joint damage effect can be removed if 20 points of divine healing are spent.Note, this
#                doesn't also give the 20 health back as the points are used to repair the deep damage only
#               * See Amputation rules below
#---------------------------------------------
#11-14 Brutal Leg Strike
#   Muscle damage to leg cuts movement in half for 3 days
#   Roll on Leg Strike Table
#   6	    Foot Amputation
#           Movement is down to 1/4 if a crutch is used, otherwise target must crawl
#           Melee: (-8ATK)/(-4DMG)
#           Range: (-10ATK) on bows only (not xbows)
#               * Muscle/Joint damage effect can be removed if 20 points of divine healing are spent.Note, this
#               doesn't also give the 20 health back as the points are used to repair the deep damage only
#               * See amputation rules below
#---------------------------------------------
#15-19	Vicious Chest Strike
#   Winded: (-6) on initiative rest of combat
#   Roll on Chest Strike Table
#   1-2 Cracked Rib: M/R/S:     (-4ATK), Crit zone opens to 17-20   
#   3-5 Internal Bleeding:      Taget loses 1d4 HP each round for 8 rounds
#   6   Punctured Lung:         Melee: (-4ATK)/(-4DMG), Range: Unable to use bows, (-4ATK) on Xbows
#                               Spell: Any spells that have somantic components have 50% fail rate
#                               Movement: Reduced down to 25%
#                               CON Check: DC12 if move at all, every time DC goes up by 2. Failure
#                               starts target choking on own blood, will pass out in 4 rounds, die 2
#                               after that.
#                                   * Cracked Rib - 10 points healing needed to knit bone
#                                   * Internal Bleeding - 15 points healing needed to stop bleeding
#                                   * Punctured Lung - 20 points healing needed to stop bleeding
#                                   > For all 3, target cannot receive healing if they are moving or exerting themselves in any way
#---------------------------------------------
#20 Head Strike
#   Roll d10, consult Head Strike Table
#   1-4 Eye Damage:	    M/R/S: (-4 ATK/DEX), unable to use acrobatic skill, R/S range halved
#   5-8 Ear removed:	    Target has (-4 PER/CHA), cannot benefit from alertness
#   9-10 Strike to Throat:  Target hemorrhaging blood, DC 15 CON save each round or bleeds for 8 damage (4 on save).
#                           Bleeding can only be stopped by somebody else making successful healing check
#                           and spending two rounds applying bandages while target remains still.
#                           spending two rounds applying bandages while target remains still.
#
#                               * Eye/Ear Damage - 20 points divine healing needed to repair eye
#                               > For all 3, target cannot receive healing if they are moving or exerting themselves in any way
#---------------------------------------------
#An does more than harm the body, it damages the essence of the person. A person who loses a hand can be divinely healed back to
#full but that doesn’t mean the hand regrows. If a divine healer doesn’t have a spell that regenerates the body, there is one
#other option: Mending Amputation (Foot/Hand): The body part missing must be intact and retrieved within ten minutes of being
#amputated. A healer must make a DC 16 Healing check and use three healing kits to bandage it back onto the body.
#The healer then must spend 40 points worth of a healing a day for a week to encourage the appendage to join the body.
#A DC 12 healing check must succeed each day as well (if the patient is in a clean environment and resting all day,
#the healer gets ADV on the check).
#---------------------------------------------
"""Begin Program"""
import random
import math
r = 1
#THERE WILL BE A WHILE LOOP LATER STARTING HERE
while r >= 1 == True:
	print("\n_____________________________Round: " + str(r) + "_______________________________")
	
	#print("********************************************************************")
	MISS = False
	HIT = False
	#print("Type QUIT at the top of the round to EXIT program.")
	query = input("H for Critical Hit, M for Critical Miss:\t")
	if query == 'h':
		HIT = True
	elif query == 'm':
		MISS = True
	elif query == "quit":
		print("Have Fun And Good Luck!")
		r = 0
	while HIT == True:   
		#print("********************************************************************")
		amputation = False
		#print("Round: " + str(r))
		roll = random.randint(1,20)
		#roll = 20
		print("1D20: " + str(roll))

		#####################
		if 1 <= roll <= 6:
			print("\n\t\t\t<><><> - SAFE - <><><>")
			print("\nTarget is stunned for their next round.\nNo other effects.")
		#####################
		elif 7 <= roll <= 10:
			#print("roll evens or odds")
			coin = random.randint(1,2)
			#print("Flip a coin: " + str(coin))
			if coin % 2 == 0:
				dominant_arm = True
				DA = "Dominant Arm"
				#print(DA)
			if coin % 2 != 0:
				dominant_arm = False
				DA = "Non-dominant Arm"
				#print(NDA)
			#test_fate = random.randint(1,6)
			test_fate = 6
			if 1 <= test_fate <= 5:
				print("\n1D6: " + str(test_fate))
				print("\t\t\t<><><> - Hand Injury - <><><>")
				print("\nMuscle/Joint damage: \t\t" + DA)
				print("Melee/Ranged/Spell: \t\t(-4ATK).")
				print("\nDC 15 CON for active concentration spells.")
					
			else:
				print("\n1D6: " + str(test_fate))
				print("\t\t\t<><><> - Hand amputation (" + DA + ")- <><><>")
				print("\nMelee:\t\t\tOff-hand gets (-8ATK)/(-4DMG.)")
				print("Range:\t\t\tUnable to use bows, (-8ATK)/(-4DMG) 3 round load on Xbows.")
				print("Spell: \t\t\tAny spells that have somatic components have 50% fail rate.")
				amputation = True    
		#####################
		elif 11 <= roll <= 14:
			test_fate = random.randint(1,6)
			#test_fate = 1
			print("1D6:" + str(test_fate))
			if 1 <= test_fate <= 5:
				print("\t\t\t<><><> - Leg Injury - <><><>\n")
				print("Muscle/Joint damage effect can be removed if 20 points of divine healing are spent.")
				print("\n***This 20 health is absorbed to repair the deep damage only, player HP does not change***")
			else:
				print("\t\t\t<><><> - Foot Amputation - <><><>\n")
				print("Melee: \t\t\t-8ATK / -4DMG.")
				print("Range: \t\t\t-10ATK on bows only not xbows.")
				print("\nMovement reduced to 1/4 if crutch is used or target must CRAWL.")
				amputation = True
		#####################
		elif 15 <= roll <= 19:
			#test_fate = random.randint(1,6)
			test_fate = 6
			print("1D6: " + str(test_fate))
			if 1<= test_fate <= 2:
				print("\n\t\t\t<><><> - Cracked Rib - <><><>\n")
				print("Melee/Ranged/Spell: \t\t\t(-4ATK), Crit zone opens to 17-20.")
			elif 3<= test_fate <= 5:
				print("\n\t\t\t<><><> - Internal Bleeding - <><><>\n")
				print("\nTarget loses 1d4 HP each round for 8 rounds.")
			else:
				print("\n\t\t\t<><><> - Punctured Lung - <><><>\n")
				print("Melee: \t\t\t(-4ATK)/(-4DMG).")
				print("Range: \t\t\tUnable to use bows, (-4ATK) on Xbows.")
				print("Spell: \t\t\tAny spells that have somantic components have 50% fail rate.")
				print("Movement: \t\tReduced to 25%.")
				print("\nCON Check: DC12 if you move at all. Every next movement increases DC by 2.")
				print("Failure: Starts choking on own blood, will pass out in 4 rounds, die 2 after that.")
		#####################
		elif roll == 20:
			test_fate = random.randint(1,10)
			#test_fate = 10
			print("1D6: " + str(test_fate))
			if 1 <= test_fate<= 4:
				print("\n\t\t\t<><><> - Eye Damage - <><><>\n")
				print("\nMelee/Ranged/Spell: \t\t(-4 ATK/DEX)")
				print("Ranged/Spell: \t\t\tRange halved")
				print("Unable to use acrobatic skill")
				print("\n*Eye Damage - 20 points divine healing needed to repair eye\n>")
			elif 5 <= test_fate <= 8:
				print("\n\t\t\t<><><> - Ear Amputation - <><><>\n")
				print("Target has (-4 PER/CHA).")
				print("Can not benefit from alertness")
				print("\n*Ear Damage - 20 points divine healing needed to repair ear\n>")
				amputation = True
			else:
				print("\n\t\t\t<><><> - Throat Strike - <><><>\n")
				print("\t\t\tTarget hemorrhaging blood")
				print("\nDC 15 CON save each round or bleeds for 8 damage (4 on save).")
				print("Bleeding can only be stopped by somebody else making successful healing check and spending two rounds applying bandages while target remains still.")

			print("\nTarget cannot receive healing if they are moving or exerting themselves in any way")

		if amputation == True:
			print("\n\n--------------------------------------------------------------------")
			print("A critical strike does more than harm the body, it damages the essence of the person. A person who loses a hand can be divinely healed back to full but that doesn’t mean the hand regrows. If a divine healer doesn’t have a spell that regenerates the body, there is one other option:")
			print("\nMending Amputation (Foot/Hand):")
			print("\nThe body part missing must be intact and retrieved within ten minutes of being amputated. A healer must make a DC 16 HEALING CHECK and use three healing kits to bandage it back onto the body. \nThe healer then must spend 40 points worth of healing a day for a week to encourage the appendage to join the body.")
			print("\nA DC 12 healing check must succeed each day as well. (If the patient is in a clean environment and resting all day, the healer gets ADV on the check")
		r += 1
		#print("************************************************************************")
		break
	while MISS == True:
		#print("MISS")
		roll = random.randint(1,10)
		if 1 <= roll <= 5:
			print("1D10 = " + str(roll))
			print("No Damage\t\t\tNo Issue with gear")
		elif 6 <= roll <= 9:
			print("1D10 = " + str(roll))
			print("\t\t\t\t\tMinor Damage")
			print("\t\t\t\t\tBlunt: -1 HIT / -1 DMG")
			print("\t\t\t\t\tEdged/Piercing: -2 DMG")
			print("\t\t\t\t\tBow/Xbow: -2 HIT")
		else:
			print("1D10 = " + str(roll))
			print("Weapon Breaks")
			print("Can club somebody with the broken remains \t\t(-4 HIT / d4 no mod. Dmg)")
		r += 1
		break
	#print("********************************************************************")
