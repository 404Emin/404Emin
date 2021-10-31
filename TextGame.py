import time
import os

#Defs
def clear():
    os.system (" cls ")

#HP
zombieHP = (105)
trollHP = (130)
skeletonHP = (95)
humanHP = (70)

# HP processing
zombie = (input("Ammount of zombies... "))

if zombie.isnumeric():
    zombie2 = int(zombie) * zombieHP
else:
    print ("Thats not a number idiot...")
    exit()

troll = (input("Ammount of trolls... "))

if troll.isnumeric():
    troll2 = int(troll) * trollHP
else:
    print ("Thats not a number idiot...")
    exit()

skeleton = (input("Ammount of skeletons... "))

if skeleton.isnumeric():
    skeleton2 = int(skeleton) * skeletonHP
else:
    print ("Thats not a number idiot...")
    exit()

human = input("Ammount of humans... ")

if human.isnumeric():
    human2 = int(human) * humanHP
else:
    print ("Thats not a number idiot...")
    exit()

#fight process..
if int(zombie2) > int(troll2):
    W1 = int(zombie2)
    w1= ("Zombie wins!")
elif int(zombie2) < int(troll2):
    W1 = int(troll2)
    w1 = ("Troll wins!")
else:
    W1 = int(zombie2)
    w1= ("Zombie wins!")

if int(W1) > int(skeleton2):
    W2 = int(W1)
    w2 = (w1)
elif int(W1) < int(skeleton2):
    W2 = int(skeleton2)
    w2 = ("Skeleton wins!")
else:
    W2 = int(skeleton2)
    w2 = ("Skeleton wins!")

if int(W2) > int(human2):
    W3 = int(W2)
    w3 = (w2)
elif int(W2) < int(human2):
    W3 = int(W2)
    w3 = ("Human wins!")
else:
    W3 = int(W2)
    w3 = ("Skeleton wins!")


print (str(w3))