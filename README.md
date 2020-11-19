# Graham Seamans - HW2 - Monopoles (the satening)

## To Run

```
python3 monosat.py m n >instance.sat
./minisat instance.sat instance.soln
python3 unmonosat.py m n <instance.soln
```
(the shell script does this too)
minisat can be found here: http://minisat.se/MiniSat.html

## Talking About The Assignment

the problem is: there are n rooms and m monopoles and all monopoles must be placed into rooms. But no two monopoles in one room can add to another monopole in the same room (ie 1, 2 and 3 can't be in the same room, and neither can 2, 4, and 6)

This program will find solutions given n and m, but not for really large examples.

So here's the sat solver!
I'm hoping it's all up to spec.

It took me a long time to figure how to phrase the problem, but
once I got it worked out everything went really fast.

there are some messy bits that could be faster, but the minisat (which is amazing) blows up with n much more than my code. So I've left it as is.

I ended up writing a bash script to help with testing which was
really helpful, although probably took more time than it saved.


