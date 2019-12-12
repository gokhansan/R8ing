from trueskill import Rating, quality_1vs1, rate_1vs1, TrueSkill, rate


def printWelcomeMessage():
	print "          |\_______________ (_____\ \______________"
	print "HH========#H###############H#######################"
	print "          ' ~'''''''''''`##(_))#H|''''''''Y########"
	print "                            ))    \#H\       `'Y###"
	print "                            \"\"      }#H)\n"

def printHelp():
	print ""
	print "## LIST OF CLASSES AND COMMANDS ##:\n"
	print "change_map \033[4mMAP\033[0m -- Change current map"
	print "scoreboard -- Show scoreboard (not available in match)"
	print "exit -- Write changes on ratings and exit the program"
	print "help -- Display help"
	print "start_match -- Start match in current map"
	print "      \033[4m1\033[0m -- for each time team1 win a round"
	print "      \033[4m2\033[0m -- for each time team2 win a round"
	print "      \033[4m0\033[0m -- for finishing the map\n"



dict = {}
map_list = ["backlot", "bog", "crossfire", "wetwork"]
with open("ratings.txt","rw") as f:
	# Read ratings and std deviations to put in dictionary
	for line in f:
		list = line.split(" ")
		# Create rating of player based on parameters
		dict[str(list[0])] = Rating( float(list[1]), float(list[2]) )
    	line = f.readline()

	# Create teams (keeps only player names)
	team1 = []
	team2 = []
	
	# Team1
	size1 = input("team1_size: ")
	for i in range (0,size1):
		name = raw_input("(" + str(i+1) + "): ")
		team1.append(name)

	# Team2
	size2 = input("team2_size: ")
	for i in range (0,size2):
		name = raw_input("(" + str(i+1) + "): ")
		team2.append(name)

	# Create team ratings to pass in rate function
	team1_ratings = []
	for playerName in team1:
		team1_ratings.append(dict[playerName])
	team2_ratings = []
	for playerName in team2:
		team2_ratings.append(dict[playerName])
	
	print "Welcome to cod4ceng, type 'help' to reach command list. \n"
	printWelcomeMessage()


	# Get command, "exit" means exit.

	current_map = ""

	while(1):
		command = raw_input("(c4c) ")
		command_split = command.split(" ")
		
		if command_split[0] == 'change_map' or command_split[0] == 'c':
			if command_split[1].lower() not in map_list:
				print "Map is not in map list, try again"
				continue
			current_map = command_split[1]
			# Get result of each round
			print "Map changed to " + current_map 
		

		elif command == 'start_match' or command == "s":
			print "Match started at " + current_map + ", enter results (0 to finish map)"
			while(1):
				res = raw_input("(c4c" + "-" + current_map + ") ")

				if res == '1': 		# Team1 won
					team1_ratings, team2_ratings = rate([team1_ratings, team2_ratings])
				elif res == '2': 	# Team2 won
					team2_ratings, team1_ratings = rate([team2_ratings, team1_ratings]) 	
				elif res == '0':	# Finish match
					print "Match is finished, waiting for command"
					break
				elif res == 'scoreboard':
					print "Scoreboard can't be shown while a match is ongoing"
		

		elif command == 'help':
			printHelp()

		elif command == 'exit':
			break

	# Update rating values in dictionary
	index = 0
	for playerName in team1:
		dict[playerName] = team1_ratings[index]
		index = index+1
	index = 0
	for playerName in team2:
		dict[playerName] = team2_ratings[index]
		index = index+1

	for key in dict:
		print key + ": " + str(dict[key])





	
       



