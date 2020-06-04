# bounce.py
#
# Exercise 1.5


bounce = 1
height = 100

while bounce < 11:
    height = round( height *  3 / 5, 4)
    print (bounce, height)
    bounce += 1