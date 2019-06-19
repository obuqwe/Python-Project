import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    header()
    game_loop()


def header():
    print('------------------------')
    print('      WIZARD GAME ')
    print('------------------------')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)

    ]

    hero = Wizard('Gandolf', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hodes taking time recover')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees: ')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print('Exit')
            break

        if not creatures:
            print('You\'ve defeated all the creatures, well done!')
            break


if __name__ == "__main__":
    main()
