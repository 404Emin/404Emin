import time
import os
from typing_extensions import runtime

#Defs
def clear():
    os.system (" cls ")

a1 = ("""W.. Where am i?.. what happened?... Who's house is this?... Ok what should i do?

Try to open the door (type: door) or look around (type: look)""")
print (str(a1))
answer = (input())

if answer == (answer.lower().strip()) == ("door"):
    print ()
elif answer == (answer.lower().strip()) == ("look"):
    print ()
else:
    print()
