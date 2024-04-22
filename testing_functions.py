import random




def fight(inventory, player_health, guns):
  opponent_health = 100
  random_opponent = random.choice(opponents_list)
  random_opponent_gun = random.choice(guns)
  random_opponent_shoot = random_opponent_gun.shoot()
  print(f"You found {random_opponent}!")
  gun_input = int(input("Choose a gun (1-5): "))
  gun_input -= 1
  if isinstance(inventory[gun_input], guns.Weapon):
    # Once u shoot them, they shoot u back and take a random amount of health from u between 0-100
    while opponent_health > 0:
      print(f"You shot {random_opponent} with a(n) {inventory[gun_input].name} and did {inventory[gun_input].shoot()} damage")
      opponent_health -= inventory[gun_input]
      player_health -= random_opponent_shoot

      print(f"Their health now: {opponent_health}")
      print(f"They hit you back using a(n){random_opponent_gun}! Your health now: {player_health}")
      continue_input = input("Do you want to coninue fighting? (y/n): ")
      while continue_input == 'y':
        opponent_health -= inventory[gun_input].damage
        player_health -= random.randint(0, 100)
        continue_input = input("Do you want to coninue fighting? (y/n): ")
