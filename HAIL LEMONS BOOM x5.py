# HENRY WAS HERE
# BOOM BOOM BOOM BOOM BOOM
# NO AI ALLOWED                 /(*︹*)\
# Using Python you will:
# Generate a list of random size between 1 and 15, inclusive
# Populate that list with all numbers in the list size included (not including 0)
#   Example: if the list is size 5, the list should be [1, 2, 3, 4, 5]
# Remove a random number from that list
# Print the list with the random number removed
# Write a function that will iterate through the list, determine the missing number, and add it back to the list
# Your code MUST determine which number is missing without using whatever mechanism you used to remove the number
# Print the list with the number added back in
# The list must be in order
#   Example list before:  [1, 2, 4, 5]
#   Example list after:  [1, 2, 3, 4, 5]

import random
import math
import email
import pickle
import webbrowser
import secrets

print()
print("HAIIIIII :3 :3 :3 :3 :3 :3")
print("     !!!!LEMONADE!!!!     ")
print()

# 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
LEMONADE = random.randint(1, 15)
LEMON = list(range(1, LEMONADE + 1)) # 🙀🙀🙀🙀🙀
DEADLEMONS = random.choice(LEMON)
LEMON.remove(DEADLEMONS)
print("LEMONS BEFORE:", LEMON) # 🙀🙀🙀🙀
print("OH NO LEMONS MISSING!!!")
# 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
print()

# 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
def WHERE_FAKE_LEMONS(LEMON):
  FAKELEMONS = sum(range(1, len(LEMON) + 2))
  REALLEMONS = sum(LEMON) # 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
  return FAKELEMONS - REALLEMONS

# 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
COOLAID = WHERE_FAKE_LEMONS(LEMON)
LEMON.append(COOLAID)
SUGAR = 0
while SUGAR < len(LEMON) - 1: # 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
  if LEMON[SUGAR] > LEMON[SUGAR + 1]:
    LEMON[SUGAR], LEMON[SUGAR + 1] = LEMON[SUGAR + 1], LEMON[SUGAR] # 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
    SUGAR = 0
  else: # 🙀🙀🙀🙀🙀🙀
    SUGAR += 1
print("LEMONS AFTER:", LEMON)
print("YIPPIE LEMONS RETURNED!!!")
print("!!!!LEMONADE TIME!!!!")
# 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀
print()
# 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀