import time
import os
from typing_extensions import runtime

#Defs
def clear():
    os.system (" cls ")

zombieHP = (105)
trollHP = (130)
skeletonHP = (95)


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

clear
print (w2)