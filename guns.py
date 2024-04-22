#
# Tody Liang
# 4/16/2024
# Contains all the gun classes for the game
# Yeah bro idk what the guns dmg numbers are lol he got it all -Everyone else
#

#Imports the random module
import random


#This is the class for the guns
class Weapon:

  def __init__(self, name, damage):
    self.name = name
    self.damage = damage


#This is the subclass for the smgs
class smg(Weapon):

  def __init__(self, name, damage):
    super().__init__(name, damage)

  def shoot(self):
    self.bloom = [50, 25, 11, 7, 5, 3, 1]
    self.selected_damage = random.choices(self.damage, self.bloom)
    #OKAY THIS TOOK FOREVER TO TROUBLE SHOOT but k=1 is bashically the   
    #pouplation the "The number of weights does not match 
    #the population" error was about. THIS TOOK THE ENTIRE WEEKEND TO RESEARCH
    #shoutouts to quora for the help
    #Marking the time, 4/21/2024 at 2:09 Am this is a moment in history
    #-Marc
    return self.selected_damage


#This is the subclass for the shotguns
class shotgun(Weapon):

  def __init__(self, name, damage):
    super().__init__(name, damage)

  #Calculates the damage and returns it

  def shoot(self):
    self.bloom = [12, 12, 25, 12, 8, 6]
    self.selected_damage = random.choices(self.damage, self.bloom)
    return self.selected_damage


#This is the subclass for the snipers
class sniper(Weapon):

  def __init__(self, name, damage):
    super().__init__(name, damage)

  #Calculates the damage and returns it
  def shoot(self):
    self.bloom = [80, 20]
    self.selected_damage = random.choices(self.damage, self.bloom)
    return self.selected_damage


#This is the subclass for the assault_rifles
class assault_rifle(Weapon):

  def __init__(self, name, damage):
    super().__init__(name, damage)

  #Calculates the damage and returns it
  def shoot(self):
    self.bloom = [50, 25, 15, 9, 5, 3, 2]
    self.selected_damage = random.choices(self.damage, self.bloom)
    return self.selected_damage


#This is the subclass for miscellaneous weapons
class miscellaneous(Weapon):

  def __init__(self, name, damage):
    super().__init__(name, damage)

  #Calculates the damage and returns it
  def shoot(self):
    self.name = "Chains of Hades"
    self.chance = [75, 12, 4, 1]
    self.selected_damage = random.choices(self.damage, self.chance)
    return self.selected_damage
