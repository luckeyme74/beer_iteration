def num_beers(n):
    while n > 0:
        print (str(n) + " bottles of beer on the wall")
        print (str(n) + " bottles of beer")
        print ("Take one down pass it around")
        print (str(n - 1)+" bottles of beer on the wall!")
        num_beers(n - 1)
        return
    else:
        print ("No bottles of beer on the wall")
        print ("No bottles of beer")
        print ("Somebody better go back to the mall")
        print ("Cause there's no more bottles of beer on the wall!")
num_beers(99)
