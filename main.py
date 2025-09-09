import time
# get the starting time and initialize the current time
starting_time = time.time()
current_time = time.time()
# create a variable to keep track of our jumping multiplier
mult = 0


# main game loop
while(True):
    #get the new time
    current_time = time.time()
    if(current_time - starting_time) % 10:
        mult += 0.1
    
