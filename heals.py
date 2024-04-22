#
# Tody Liang, Vir Patel, Henry Vogel, Marc Fernando
# 4/17/2024
# Contains all the heal classes for the game
#

#Imports modules
import random



# Creates a class for the heals -Henry
class Heals():
  def __init__(self, name, heal_amount):
    self.name = name
    self.heal_amount = heal_amount
  def use_heal(self):
    return self.heal_amount

