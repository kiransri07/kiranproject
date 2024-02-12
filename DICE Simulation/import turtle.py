"""
1.users roll the dice by pressing enter key
2.validating the dice value and announcing the winners for each round
3.Announcing the final battle winner
"""
import random
player1_score = 0
player2_score = 0
for i in range(1,11):
    print("=====ROUND -{} =====".format(i))
    player1_input = input("Press Enter Key to roll the Dice")
    player1_value = random.randint(1,6)
    player2_input = input("Press Enter Key to roll the Dice")
    player2_value = random.randint(1,6)

    if player1_value > player2_value:
        print("Player -1 Wins this Round")
        player1_score += 1
    elif player2_score > player1_score:
        print("Player -2 Wins this Round")
    else:
        print("This Round is Drawn")

if player1_score > player2_score:
    print("player-1 Wins the Battle:",player1_score)
else:
    print("player-2 Wins the Battle:",player2_score)

print("*** BATTLE OVER - THANKS ***")
