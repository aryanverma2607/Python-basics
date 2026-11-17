'''
7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)

'''
n=int(input("Enter number of Player : "))
player=[]
for i in range(n):
	print()
	print(f"Enter Player {i+1} detail")
	id=int(input("Enter Player Id : "))
	name=input("enter player name : ")
	score=int(input("Enter Score : "))
	record=(id,name,score)
	player.append(record)
print()
print("All Player")
for i in player:
	print(i)
lowest=player[0][2]
highest=player[0][2]
sum=0
for i in range(len(player)):
	if player[i][2]>highest:
		highest=player[i][2]
	if player[i][2]<lowest:
		lowest=player[i][2]
	sum=sum+player[i][2]
print()
for i in range(len(player)):
	if player[i][2]==highest:
		print("Highest Scorer:")
		print(player[i])
		print()
	if player[i][2]==lowest:
		print("Lowest Scorer:")
		print(player[i])

avg=sum/n
print()
print("""Total Runs :
{}""".format(sum))
print()
print("""Average Runs :
{}""".format(avg))

print()
print("Player Scoring More than 50")
for i in range(len(player)):
	if player[i][2]>50:
		print(player[i])
	
	
		