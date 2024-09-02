#rock paper and scissors game
import random
memory=['rock','paper','scissor']
print("Welcome to Rock Paper and Scissors game!\n")
print("""Before playing the game read the rules-\n
      1)First the computer will ask you about your choice then it would throw a completely random choice of its own\n
      2)For every win there would be a +1 point\n
      3)No points would be given or striken off due to loss\n
      4)At the end of 5 tries The computer would show a grand total of points collected by both the computer and player\n
      5)Based upon the grand total points, the one with higher points would be announced winner\n
      6)If both computer and player have same points, Then the match would be called a draw\n""")
user_score=0
comp_score=0
for i in range(5):
    int=input("Enter your move(rock,paper or scissor): ").lower()
    rnd=random.choice(memory)
    print(f"Computer: {rnd}\n")
    if rnd==int:
        print("No points to both user and computer")
    elif (int=="rock" and rnd=="paper") or (int=="paper" and rnd=="scissor") or (int=="scissor" and rnd=="rock"):
        print("Computer gains 1 point")
        comp_score+= 1
    elif (int=="paper" and rnd=="rock") or (int=="scissor" and rnd=="paper") or (int=="rock" and rnd=="scissor"):
        print("Player gains 1 point")
        user_score+=1
t1=print(f"Total score scored by player {user_score}\n")
t2=print(f"Total score scored by computer {comp_score}\n")
if(user_score==comp_score):
    print("The match is draw")
elif(user_score>comp_score):
    print("Player won the match")
elif(comp_score>user_score):
    print("Computer won the match")