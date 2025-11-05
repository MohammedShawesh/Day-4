from Character import Warrior, Mage
import time

enemies = [
    {'name': 'Goblin Scout', 'class': Warrior, 'level': 1, 'power': 9},
    {'name': 'Gutter Rat', 'class': Warrior, 'level': 2, 'power': 11},
    {'name': 'Shadowy Acolyte', 'class': Mage, 'level': 3, 'power': 10},
    {'name': 'Orc Grunt', 'class': Warrior, 'level': 4, 'power': 16},
    {'name': 'Enraged Golem', 'class': Warrior, 'level': 5, 'power': 19},
    {'name': 'Dark Sorceress', 'class': Mage, 'level': 6, 'power': 15},
    {'name': 'Minotaur', 'class': Warrior, 'level': 7, 'power': 24},
    {'name': 'Young Chimera', 'class': Mage, 'level': 8, 'power': 21},
    {'name': 'Arena Champion', 'class': Warrior, 'level': 9, 'power': 28},
    {'name': 'Dragon Hatchling', 'class': Mage, 'level': 10, 'power': 25}
]

print("=" * 30)
print("  Welcome to the Gauntlet Challenge!  ")
print("=" * 30)

player = None
while player is None:
    choice = input("Choose your character:\n1. Warrior\n2. Mage\n> ")
    if choice == "1":
        player_name = input("Enter your Warrior's name: ")
        player = Warrior(player_name)
    elif choice == "2":
        player_name = input("Enter your Mage's name: ")
        player = Mage(player_name)
    else:
        print("Invalid choice! Please enter 1 or 2.")


game_over = False
for i, enemy_data in enumerate(enemies):

    enemy = enemy_data['class'](
        name=enemy_data['name'],
        level=enemy_data['level'],
        power=enemy_data['power']
    )

    print("\n" + "#" * 40)
    print(f"    BATTLE {i + 1} / {len(enemies)}: {player.name} vs. {enemy.name}")
    print("#" * 40)
    time.sleep(1)

    turn = 1
    while player.health > 0 and enemy.health > 0:
        print("\n" + "-" * 10 + f" Round {turn} " + "-" * 10)
        player.get_status()
        enemy.get_status()


        print(f"\nIt's {player.name}'s turn!")
        action = ""
        if isinstance(player, Warrior):
            action = input("Choose your action:\n1. Attack\n2. Power Smash\n> ")
            if action == "1":
                player.attack(enemy)
            elif action == "2":
                player.power_smash(enemy)
            else:
                print("Invalid action! You hesitate and do nothing.")
        elif isinstance(player, Mage):
            action = input("Choose your action:\n1. Attack (with staff)\n2. Cast Fireball\n3. Meditate\n> ")
            if action == "1":
                player.attack(enemy)
            elif action == "2":
                player.cast_spell(enemy)
            elif action == "3":
                player.meditate()
            else:
                print("Invalid action! You hesitate and do nothing.")

        if enemy.health <= 0:
            break

        print(f"\nIt's the {enemy.name}'s turn!")
        time.sleep(1)
        enemy.attack(player)

        if player.health <= 0:
            game_over = True
            break

        turn += 1
        time.sleep(1)

    if game_over:
        print("\n" + "=" * 30)
        print(f"GAME OVER! {player.name} was slain by the {enemy.name}...")
        print("=" * 30)
        break

    else:
        print("\n" + "=" * 30)
        print(f"🎉 VICTORY! {player.name} defeated the {enemy.name}! 🎉")
        print("=" * 30)
        player.level_up()

        if i == len(enemies) - 1:
            print("\n" + "#" * 40)
            print(f"CONGRATULATIONS, {player.name}! You have defeated all opponents and conquered the Gauntlet!")
            print("#" * 40)
            break

        continue_choice = input("\nAre you ready for the next opponent? (yes/no): ")
        if continue_choice.lower() != 'yes':
            break

print("\nThanks for playing! Goodbye.")