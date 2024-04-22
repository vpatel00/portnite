#Marc Fernando, Tody Liang, Vir Patel, Henry Vogel
# 4/16/2024
# Portnite (Python + Fortnite), a text-based Fortnite game that reviews Python and networking
# Add Import Statements Here

# Consider adding colors using colorama: https://www.geeksforgeeks.org/print-colors-python-terminal/
try:
  # Import Statements 
  import random
  from time import sleep
  import Ascii_Art
  #from enemy import Players_In_Lobby
  import guns
  import heals
  import os
  import time
  import questions
  from heals import Heals

  
  #from playsound import playsound
  #Issues installing playsound on replit, uncomment the line above when submitting
  
  #INSERT Global variables HERE
  dropspot_list = [
      "Rebel's Roost", "The Underworld", "Grim Gate", "Pleasant Piazza",
      "Snooty Steppes", "Lavish Lair", "Restored Reels", "Fencing Fields",
      "Classy Courts", "Reckless Railways", "Grand Glacier", "Mount Olympus",
      "Brawler's Battleground"
  ]
  
  Gameplay_Action_List = [
      "Loot Chest", "Heal", "Fight Someone", "Drop Item"
  ]
  
  opponents_list = [
    "The Rock", "Chun-Li", "Marc Fernando", "Tody is washed", "Solid Snake", "Peter Griffin", "Tyler Blevins", "Spider_Man", "Omni-Man", "Lady Gaga", "LeBron James", "Henri Fogel", "Honda/Civic"
  ]
  
  
  
  ############################ LOOT POOL OBJECTS AND LIST ############################
  
  # Guns
  hammer_shotgun = guns.shotgun(name = "Hammer Pump", damage = [23, 53, 103, 146, 179, 190])
  frenzy_auto = guns.shotgun(name = "Frenzy Auto", damage = [25, 50, 75, 105, 132, 150])
  warforge_ar = guns.assault_rifle(name = "Warforged AR", damage = [31, 62, 93, 124, 155, 186, 217])
  nemesis_ar = guns.assault_rifle(name = "Nemesis AR", damage = [35, 70, 105, 140, 175, 210, 245])
  reaper_sniper = guns.sniper(name = "Reaper Sniper", damage = [121, 303])
  thunder_burst_smg = guns.smg(name = "Thunder Burst SMG", damage = [29, 58, 87, 116, 145, 174, 203])
  drum_gun = guns.smg(name = "Drum Gun", damage = [24, 48, 76, 104, 132, 160, 188])
  chains_of_hades = guns.miscellaneous(name = "Chains of Hades", damage = [55, 110, 165, 220])
  
  guns_list = [hammer_shotgun, frenzy_auto, warforge_ar, nemesis_ar, reaper_sniper, thunder_burst_smg, drum_gun, chains_of_hades]
  
  
  # HEALS
  big_pot = heals.Heals(name = "Big Pot", heal_amount = 50)
  minis = heals.Heals(name = "Minis", heal_amount = 25)
  medkit = heals.Heals(name = "Medkit", heal_amount = 100)
  bandages = heals.Heals(name = "Bandages", heal_amount = 15)
  flowberry_fizz = heals.Heals(name = "Flowberry Fizz", heal_amount = 100)
  banana_of_the_gods = heals.Heals(name = "Banana of the Gods", heal_amount = 60)
  flowberry = heals.Heals(name = "Flowberry", heal_amount = 15)
  flopper = heals.Heals(name = "Flopper", heal_amount = 40)
  apple = heals.Heals(name = "Apple", heal_amount = 10)
  cabbage = heals.Heals(name = "Cabbage", heal_amount = 10)
  shield_fish = heals.Heals(name = "Shield Fish", heal_amount = 40)
  small_fry = heals.Heals(name = "Small Fry", heal_amount = 15)
  coconut = heals.Heals(name = "Coconut", heal_amount = 10)
  splashes = heals.Heals(name = "Splashes", heal_amount = 20)
  corn = heals.Heals(name = "Corn", heal_amount = 10)
  mushroom = heals.Heals(name = "Mushroom", heal_amount = 10)
  
  heals_list = [big_pot, minis, medkit, bandages, flowberry_fizz, banana_of_the_gods, flowberry, flopper, apple, cabbage, shield_fish, small_fry, coconut, splashes, corn, mushroom]
  
  
  
  
  # LOOT POOL (GUNS + HEALS)
  '''
  loot_pool = [hammer_shotgun.name, frenzy_auto.name, warforge_ar.name, nemesis_ar.name, reaper_sniper.name, thunder_burst_smg.name, drum_gun.name, chains_of_hades.name, big_pot.name, minis.name, medkit.name, bandages.name, flowberry_fizz.name, banana_of_the_gods.name, flowberry.name, flopper.name, apple.name, cabbage.name, shield_fish.name, small_fry.name, corn.name, mushroom.name, coconut.name, splashes.name, corn.name, mushroom.name]
  '''
  # I had to change the loot pool to a objects because you can't get the information of the objects from strings 
  loot_pool = [hammer_shotgun, frenzy_auto, warforge_ar, nemesis_ar, reaper_sniper, thunder_burst_smg, drum_gun, chains_of_hades, big_pot, minis, medkit, bandages, flowberry_fizz, banana_of_the_gods, flowberry, flopper, apple, cabbage, shield_fish, small_fry, corn, mushroom, coconut, splashes, corn, mushroom]
  #chances of each object to appear in the loot pool
  chance = [75, 75, 75, 75, 75, 75, 75, 75, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25 ,25, 25, 25, 25, 25, 25, 25]
  
  guns = [hammer_shotgun, frenzy_auto, warforge_ar, nemesis_ar, reaper_sniper, thunder_burst_smg, drum_gun, chains_of_hades]
  
  heals = [big_pot, minis, medkit, bandages, flowberry_fizz, banana_of_the_gods, flowberry, flopper, apple, cabbage, shield_fish, small_fry, coconut, splashes, corn, mushroom]
  
  # --------------------------------- Functions --------------------------------------
  def looting(inventory, loot_pool, chance):
      if len(inventory) >= 5:
          print("Inventory is full, please choose another action.")
      else:
          print("You are looting...")
          Ascii_Art.chest()
          sleep(1)
          print()
        #adds to inv a random item from the loot pool
          inventory.append(random.choices(loot_pool, chance))
          print(f"Your inventory right now: {[x.name for i in inventory for x in i]}")
  
      return inventory
  
  # -------------------------- FUNCTION FOR HEALING -----------------------------
  """
  def healing(player_health, inventory, name, heals_list, Heals):
      print([item.name for item in inventory])
      #print([x.name for x in inventory]) # This will print the name of each item in the inventory
      heal_input = int(input(f"What would you like to use to heal? (1-5) {[x.name for x in inventory]}: ")) # Add error handling here
      if heal_input < 1 or heal_input > len(inventory):
          print("Invalid input, please try again.")
          heal_input = int(input(f"What would you like to use to heal? (1-5) {[x.name for x in inventory]}: ")) # Add error handling here
      else:
          heal_input -= 1 # List starts at 0, so subtract hereeeee
      if inventory[heal_input] in heals_list:
      #if inventory[heal_input].name in [x.name for x in heals_list]: # Check if the name of the item is in the list of healing items
          if player_health == 200:
              print("You are already at max health.")
              
          elif (player_health + inventory[heal_input].heal_amount) >= 200:
              player_health = 200
              print(f"You used a(n) {inventory[heal_input].name} and healed {inventory[heal_input].heal_amount}. Your health is now {player_health}")
              inventory.remove(inventory[heal_input])
          elif (player_health + inventory[heal_input].heal_amount) <= 200:
              player_health += inventory[heal_input].heal_amount
              print(f"You used a(n) {inventory[heal_input].name} and healed {inventory[heal_input].heal_amount}. Your health is now {player_health}")
              inventory.remove(inventory[heal_input])
      else:
          print("You don't have any heals in your inventory!")
  
  
      return player_health
      """
  def healing(player_health, inventory):
    clear()
    continue_healing = "y"
    #checks if health is already at max or not
    while player_health < 200 and continue_healing == "y":
      while True:
        try:
          print(f"Your health: {player_health}")
          print(f"Your inventory: {[x.name for i in inventory for x in i]}")
          
          heal_input = int(input("Choose a healing item (1-5): "))
          heal_input -= 1
          heal = inventory[heal_input][0]
          heal_amount = heal.use_heal()
          break
        except:
          print("Invalid slot. Please pick a different slot.")
          return player_health
          
      player_health += heal_amount
      if player_health >= 200:
        player_health = 200
        print("Your health is now full")
        return player_health
      print(f"You healed {heal_amount} for health with a(n) {heal.name} and your health is now at {player_health}")
      inventory.pop(heal_input)
      continue_healing = str(input("Do you want to keep healing? [y/n]: ")).lower()
   
  
    return player_health
  
  # ------------------------- FUNCTION FOR RUNNING AWAY ------------------------
  #if dropspot == "Random" or dropspot == "random":
  #  RandomDropSpot = random.sample(dropspot_list,1)
  #print("You dived off at random. You landed inside of " + (str(leave_input).replace('[', '').replace(']', '').strip("'"))+ ".")
  ''''
  def run_away():
      print(f'\nList of locations: {", ".join(dropspot_list)}\n')
      leave_input = input("Where do you want do want to go? ")
      if leave_input == "Random" or leave_input == "random":
        leave_input = random.sample(dropspot_list, 1)
        
      while leave_input not in dropspot_list or leave_input != "random" or leave_input != "Random":
        print("Invalid escape spot")
        leave_input = input("Where do you want do want to go?: ")
      print(f"You escaped to {leave_input}")
  '''
  # ------------------------ FUNCTION FOR FIGHTING AN OPPONENT ------------------
  
  def fight(inventory, player_health, guns):
    clear()
    #random gen. for opponent
    random_opponent = random.choice(opponents_list)
    print(f"You found {random_opponent}!")
    opponent_health = random.randint(50, 200)

    
     #inventory[gun_input - 1].
      # Once u shoot them, they shoot u back and take a random amount of health
    while opponent_health > 0:
      random_opponent_gun = random.choice(guns)
      #This takes the random opps dmg and subtracts it from the player health using a random gun
      random_opponent_damage = random_opponent_gun.shoot()[0]
      while True:
        try:
          print(f"Your health: {player_health}")
          print(f"Your inventory: {[x.name for i in inventory for x in i]}")
          gun_input = int(input("Choose a gun (1-5): "))
          gun = inventory[gun_input - 1][0]
          gun_damage = gun.shoot()[0]
          break
          
        except: #error handling
          print("Invalid slot. Please pick a different slot.")
          return player_health
          
      time.sleep(2)
      clear()
      print(f"You hit {random_opponent} with a(n) {gun.name} and did {gun_damage} damage")
      opponent_health -= gun_damage
  
  #Evaluation for enemy health
      if opponent_health <= 0:
        print(f"Eliminated {random_opponent}")
        return player_health
      else:
        print(f"Their health now: {opponent_health}")
        player_health -= random_opponent_damage
        if player_health <= 0:
          print("You died!")
          print("Going back to menu...")
          sleep(3)
          game_defeat()
          main_GUI()
        print(f"They hit you back using a(n) {random_opponent_gun.name} and did {random_opponent_damage}! Your health now: {player_health}")
        want_heal = str(input("Do you want to heal? [y/n]: ")).lower()
        if want_heal == "y":
          #Heal? or healing? I changed it to heal cause healing was an error -Marc
          player_health = healing(player_health, inventory)
    if player_health <= 0:
      print("\nOuch...!\n")
      sleep(3)
      print("You died!")
      game_defeat()
      main_GUI()
      #quit()
        
  def drop_item(inventory):
      print(f"Your inventory: {[x.name for i in inventory for x in i]}")
      item = int(input("Choose the item you want to drop (1-5): "))
      try:
        print(f"You dropped {inventory.pop(item - 1).name}")
      except:
        print("There are no items to drop.")

      
      return inventory

  
  #-------------- START FUNCTION, runs when code runs for the first time ----------------------------
  def clear():
    os.system('clear')
  
  def main():
    # Plays the background music
    #playsound.playsound('music.mp3')
  
    # Asks for name and input device -Henry
    Ascii_Art.Game_Name()
    sleep(5)
    global name
    clear()
    print("NOTE: This game is case sensitive! Mind your lower and uppercases, folks!!!\n")
    print("\nAlso remember to turn your audio on!")
    print("Make sure to play in FULL SCREEN!\n")
    name = input("What is your name?: ")
    print(f"Hello {name}!", "Welcome to Portnite!")
    sleep(3)
    clear()
  
    print('Choose between the following input devices, "Keyboard" or "Controller"?')
    controller = str(input("What is your input device?: "))
    print()
  
    #Controller choice debug for wonky ahh code -Marc
    controller_choice_debug = ["Keyboard", "Controller", "keyboard", "controller"]
    while controller != "Keyboard" or controller != "Controller" or controller != "keyboard" or controller != "controller":
      #No way yall added this code for a controller joke only McCuen will ever see -Marc
      if controller == "Joystick" or controller == "Steering Wheel":
        print("Why. Why would you do this?")
        sleep(2)
        print("\nYou know what? No. Wrong. Try again.\n")
        sleep(3)
        clear()
        print("Please enter 'Keyboard' or 'Controller'")
        controller = str(input("What is your input device?: "))
      elif controller in controller_choice_debug:
        print(f"You have chosen the {controller.capitalize()} as your input device.")
        sleep(3)
        clear()
        break
      else:
        print("Error. Input device not found.")
        print()
        print("Please enter 'Keyboard' or 'Controller'")
        controller = str(input("What is your input device?: "))
  
    # Asks for difficulty -Henry
    #Bro this does nothing why add this -Marc
    # nuh uh -Vir
    print("Choose between the following difficulties: Easy, Normal, Hard")
    difficulty = str(input("What is your difficulty?: ")).lower()

    difficulty_choice = ["easy", "normal", "hard"]
    
    while difficulty != "easy" or difficulty != "normal" or difficulty != "hard":
      if difficulty not in difficulty_choice:
        print("No choice found, try again.")
        difficulty = str(input("What is your difficulty?: ")).lower()
      else:
        print(f"\nThe chosen difficulty is: {difficulty.capitalize()} difficulty.\n")
        sleep(3)
        break
    clear()
  
    #The main_GUI IS indented so it runs through main
    #THEN displays the main_GUI after, to call back to other def functions above
    main_GUI()
  
  
  #-----------------------------------------------------------------------------------
  #            sandwiches               up at 3am gang wya??? -Marc
  #----------------------------------- MAIN GUI --------------------------------------
  
    #Marc F drafted the main GUI format and code structure and heheh :)
    #Marcs comments below :PPPP
    #Oh and Vir helped too to route the defs to the oth
  def main_GUI():
    #This displays the menu
    #NOTE FOR EVERYONE ELSE: Add actions + more stuff here, delete this comment when done -Marc
    print(f"\n--------------------------")
    print("ACTIONS: T for Tutorial")
    print("ACTIONS: P for Play Game")
    print("ACTIONS: Q to Quit (WILL END ALL PROGRESS)")
    print("--------------------------")
  
    #ACTION_LIST is what they can CHOOSE to input
    #MAKE SURE THE ACTION LIST IS UPPERCASE!!!
    ACTION_LIST = ["T","P","Q"]
  
    #User input here:
    Player_GUI_Choice = input("What do you wanna do?: ").upper()
  
    #Error Handling, if not in list:
    if Player_GUI_Choice not in ACTION_LIST:
      # TODO: Add tutorial here explaining how to play
      print("ACTION NOT FOUND.")
      sleep(1)
  
      #This returns to main_GUI, like a loop
      return main_GUI()
  
    #Else statements, or the choice redirections
    elif Player_GUI_Choice == "T" or Player_GUI_Choice == "Tutorial":
      print("Ready to learn how to play?")
      sleep(3)
      print()
      print("Get Ready!")
      sleep(2)
      clear()
      print("Tutorial:")
      print()
      print("You are in a Portnite Lobby. You have a choice to either loot, fight, run away, or heal.")
      print()
      print("Looting is when you can get guns, heals, or lootboxes.")
      print("When you fight, you will encounter an opponent.")
      print()
      print("Healing will use a heal item from your inventory. Heals a set amount of HP")
      print("You can only heal if your HP is below 200. You start at 200 HP")
      print()
      print("When you are asked a question, answer it by typing A, B, C, or D.")
      print()
      print("You can also quit the game at any time by typing 'Q'")
      print("You will keep looting, fighting, running, or healing until you are the last one alive, or you are eliminated.")
      print()
      player_choice = input("Ready to play? (Y/N): ")
      while True:
        if player_choice.upper() == "Y":
          print("Okay, let's go!")
          return main_GUI()
        elif Player_GUI_Choice == "N" or player_choice.upper() == "N":
          print(f"Okay, {name}, you can come back when you're ready.")
          sleep(1)
          player_choice = input("Ready to play? (Y/N): ")
        else:
          print("Invalid input, please try again.")
          sleep(1)
          clear()
          player_choice = input("Ready to play? (Y/N): ")
  #---------------------------
    elif Player_GUI_Choice == "P" or Player_GUI_Choice == "Play" or Player_GUI_Choice == "play":
      #Loading_Screen()
      # Open and display the image
      play_game()
      #sleep(3)
  
    #Quit elif, THIS ELIF SHOULD STAY THE LAST ELIF IN CODE HERE!!!
    elif Player_GUI_Choice == "Q" or Player_GUI_Choice == "Quit" or Player_GUI_Choice == "quit":
      Ascii_Art.defeat_art()
      Ascii_Art.defeat()
      print("Quitting... Bye bye!")
      sleep(6)
      clear()
  
    #If unreconizable, error handling again:
    else:
      print("ERROR: Input Handling. Insert A GIVEN Action.")
      return main_GUI()
  
  
  # ------------------------PLAY_GAME_HERE-------------------------------
  # CODE THAT RUNS WHEN USERS CHOOSES TO PLAY
  def play_game():
    player_health = 200
    player_count = 100
    inventory = []
    Ascii_Art.loading_screen_ascii_art()
    sleep(3)
    clear()
    print("\n1 loading screen later...\n")
  
    #Prints all drop spots
    print(f'The List of Drops is: {", ".join(dropspot_list)}')
  
    print("\nTIP: Type Random for a random drop spot. Each drop spot is caps sensitive :(")
    dropspot = input(f'\nWhere we dropping, {name}?: \n')
    print()
  
    #Putting my name for this cause the random function took so longgg to type
    #"forgot the .strip for awhile im so cooked" -Marc
    # No Marc is the chef rn -Henry
    if dropspot == "Random" or dropspot == "random":
      RandomDropSpot = random.sample(dropspot_list,1)
      print("You dived off at random. You landed inside of " + (str(RandomDropSpot).replace('[', '').replace(']', '').strip("'"))+ ".")
      sleep(1)
  
    #Henry's secret win cheat code -Henry
    elif dropspot == "Hill":
      print("You Recived Henry's Blessing \nVictory Royale!")
      Ascii_Art.victory()
      exit()
  
    #Todys secret win cheat code
    elif dropspot == "Reckless Railways":
      print("You just won because this is Tody's dropspot and Tody wins everygame when he lands here. \nVictory Royale!")
      Ascii_Art.victory()
      exit()
  
    #If they type a dropspot that is not in the list
    #Also if random is typed, it will not run random
    while dropspot not in dropspot_list and dropspot != "Random" and dropspot != "random":
      print("Invalid dropspot")
      dropspot = input(f'\nWhere we dropping, {name}?: \n')
  # Henry was here -Henry
  
    print(f"You dropped at {dropspot}")
    print()
  
    # Asks the user what they want to do
    sleep(2)
    clear()
    gameplay_action_input = input("What's your next move? (Moves: "+     
  (str(Gameplay_Action_List).replace('[', '').replace(']', '').replace("'", "")) + "): ")
    print()
    while gameplay_action_input not in Gameplay_Action_List:
      print("\nInvalid option, please try again\n")
      gameplay_action_input = input(f"What's your next move? (Moves: {Gameplay_Action_List}): ")
      print()
      
    while player_health > 0 and player_count > 1:
        if gameplay_action_input == "Loot Chest" or  gameplay_action_input == "loot chest":
          if questions.ask_question(questions.q_and_a):
            inventory = looting(inventory, loot_pool, chance)
          else:
            print("Try again!")
  
          player_count -= random.randint(5, 10)
  
        elif gameplay_action_input == "Heal" or gameplay_action_input == "heal":
          if questions.ask_question(questions.q_and_a):
            player_health = healing(player_health, inventory)
          elif len(inventory) == 0:
            print("You don't have any heals! Go loot a chest first")
          else:
            print("Try again!")
          
          player_count -= random.randint(5, 10)
            
        elif gameplay_action_input == "Fight Someone" or gameplay_action_input == "fight someone":
            if len(inventory) == 0:
              print("You dont have anything in your inventory! Go Loot a Chest first")
            elif questions.ask_question(questions.q_and_a):
              player_health = fight(inventory, player_health, guns)
            player_count -= (random.randint(5, 10))
        elif gameplay_action_input == "Drop Item" or gameplay_action_input == "drop item":
          inventory = drop_item(inventory)
        else:
          clear()
        
        # TODO: Add input validation here and stuff
       
        if player_count <= 1:
          player_health = fight(inventory, player_health, guns)
          game_win()
          #main_GUI()
  
        sleep(2)
        clear()
        print(f"There are {player_count} players left")
        print(f"Your inventory: {[x.name for i in inventory for x in i]}")
        print(f"Your health: {player_health}")
        gameplay_action_input = input(f"What's your next move? (Moves: {Gameplay_Action_List}): ")
  
  
  
  #--------------Game Endings-----------------
  def game_win():
    print("\nVictory Royale! Thanks for playing!\n")
    Ascii_Art.victory()
    print("Going back to menu...")
    sleep(5)
    main_GUI()
    #exit()
  
  def game_defeat():
    print("Skill Issue")
    Ascii_Art.defeat()
    print("Going back to menu...")
    sleep(5)
    #exit()
  
  main()
  
  
  #----------------EXTRA CODE-----------------
  """
  import random
  
  class Enemy:
      def __init__(self, enemy_health=100, enemy_damage=0):
          self.enemy_health = enemy_health
          self.enemy_damage = enemy_damage
  
      def enemy_death(self):
          if self.enemy_health <= 0:
              print("Enemy defeated!")
  
      def enemy_action(self):
          self.enemy_damage += random.randint(5, 20)
  # makes an enemy instance
  enemy_instance = Enemy()
  # Check enemy health
  print("Enemy health:", enemy_instance.enemy_health)
  
  # Perform enemy action
  enemy_instance.enemy_action()
  
  """
  """
  #YO GUYS I WORKED ON THIS AT 3AM CHECK THIS OUT
  #-Marc Fernando
  #sad, we never used this, huh.
  def fight():
    opponent_health = 100
    random_opponent = random.choice(opponents_list)
    print(f"Yo, you stumbled upon {random_opponent}!")
    gun_input = int(input("Pick a gun (1-5): ")) - 1
    if isinstance(inventory[gun_input], guns.Weapon):
        while opponent_health > 0 and player_health > 0:
            print(f"You blasted {random_opponent} with your {inventory[gun_input].name}, dealing {inventory[gun_input].damage} damage!")
            opponent_health -= inventory[gun_input].damage
            player_health -= random.randint(0, 100)
            print(f"{random_opponent}'s health now: {opponent_health}")
            print(f"They hit you back! Your health: {player_health}")
            if player_health <= 0:
                print("You got rekt dang o7")
                game_defeat()
                return
            if opponent_health <= 0:
                print("You...got the enemy!")
                return
            if ask_question(q_and_a):
                opponent_health -= random.randint(5, 20)
                print("You got the question right! Extra damage to the enemy!")
            else:
                print("You got the question wrong! Enemy gets another go at you.")
                player_health -= random.randint(10, 30)
                print(f"They hit you back! Your health: {player_health}")
                continue_input = input("Wanna keep duking it out? (y/n): ")
                if continue_input.lower() != 'y':
                    return
  """
except KeyboardInterrupt:
  print("Why don't you wanna play me? :(")
# For keyboardinterrupt
