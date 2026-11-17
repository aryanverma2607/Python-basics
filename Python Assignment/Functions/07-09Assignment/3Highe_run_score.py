'''
3.
Cricket Tournament – Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit
'''
from functools import reduce

k=int(input("Enter number of players: "))
players=[]
for i in range(k):
    name=input("Enter name: ")
    run=int(input("Enter runs: "))
    t=(name,run)
    players.append(t)

result=reduce(lambda x,y:x if x[1]>y[1] else y,players)
print(result[0])