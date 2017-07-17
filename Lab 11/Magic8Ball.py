print "Magic 8 Ball"

import random

question = raw_input ("What is your question? ")
answer = random.randint(1,20)
if answer == 1:
    print "Positively Yes."
elif answer == 2:
    print "Positively No."
elif answer == 3:
    print "Positively Maybe."
elif answer == 4:
    print "No need to know now."
elif answer == 5:
    print "Busy. Ask again tomorrow."
elif answer == 6:
    print "Come again?"
elif answer == 7:
    print "The Gods are with you."
elif answer == 8:
    print "The Angels are nodding in agreement."
elif answer == 9:
    print "The Donkeys are braying. Not a good sign."
elif answer == 10:
    print "Amazing, but no."
elif answer == 11:
    print "Maybe good outcome."
elif answer == 12:
    print "Go away and think about it some more."
elif answer == 13:
    print "The outcome is uncertain."
elif answer == 14:
    print "That's the way Ahuh Ahuh."
elif answer == 15:
    print "Nope"
elif answer == 16:
    print "I don't think that is a good idea."
elif answer == 17:
    print "Brava, go with it."
elif answer == 18:
    print "I hate to rain on your parade, but nada."
elif answer == 19:
    print "Sunny days are here again. Go for it."
else:
    print "Five by Five. Straight Ahead."


