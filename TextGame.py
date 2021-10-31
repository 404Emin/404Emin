import time
import os
from typing_extensions import runtime

#Defs
def clear():
    os.system (" cls ")


zombie = int(input("Ammount of zombies... "))
troll = int(input("Ammount of trolls... "))
skeleton = int(input("Ammount of skeletons... "))


zombie2 = zombie * 105
troll2 = troll * 120
skeleton2 = skeleton * 92


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