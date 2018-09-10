#!/usr/bin/env python

import random
import sys

# Create our Player Array from the list of players.
players = sys.argv[1:]

# Shuffle the Array 10000 times
for x in range(10000):
  # Print to the screen so you know it's legit, remembering that we start at 0 not 1.
  print "Shuffle number #" + str(x+1)
  random.shuffle(players)

# Print some formatting to the screen to make it look nice.
print '\nNow for the FINAL draft order!'

# List out the players in their Draft Order
for player in players:
  print player
