#Graham Seamans - HW2 - Monopoles (the satening)

##to run:

'''
python3 monosat.py m n >instance.sat
./minisat instance.sat instance.soln
python3 unmonosat.py m n <instance.soln
'''

##Talking about the assignment:

So here's the sat solver!
I'm hoping it's all up to spec.

It took me a long time to figure how to phrase the problem, but
once I got it worked out everything went really fast.

there are some messy bits that could be faster, but the minisat (which is amazing) blows up with time much more than my code. So I've left it as is.

I ended up writing a bash script to help with testing which was
really helpful, alhough probably took more time than it saved,
but that's programming.


