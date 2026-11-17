print("Cricket Run Rate")
runs=int(input("Total runs = "))
overs=float(input("Enter overs = "))
over=(overs*10)//10
over1=(overs*10)%6
balls=over*6
total_ball=over1 + balls
print(total_ball)
print("Total Balls = ",int(total_ball))
print("Run Rate =",(runs/(total_ball/6)))
