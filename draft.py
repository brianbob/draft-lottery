#!/usr/bin/env python

import random

# Create our Player Array
players = ["Brad", "Brian", "Gabe", "Dad (Jim)", "Mark", "Max", "Kevin", "Kyle", "Savannah", "Ted"]

# Shuffle the Array 10000 times
for x in range(10000):
  # Print to the screen so you know it's legit, remembering that we start at 0 not 1.
  print("Shuffle number #" + str(x+1))
  random.shuffle(players)

# Print some formatting to the screen to make it look nice.
print ''
print 'Now for the FINAL draft order!'

# List out the players in their Draft Order
for player in players:
  print player
