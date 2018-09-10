#!/usr/bin/env python

import random
import sys

# Create our Player list from the command-line arugments.
players = sys.argv[1:]

# Check to make sure the list isn't empty.
if not players:
  print("List is empty")
  quit()

# If we have a list, shuffle it 10,000 times (for good measure).
for x in range(10000):
  # Print to the screen so you know it's legit, remembering that we start at 0
  # not 1.
  print "Shuffle number #" + str(x+1)
  random.shuffle(players)

# Print some formatting to the screen to make it look nice.
print '\nNow for the FINAL draft order!'

# List out the players in their Draft Order.
for player in players:
  print player
