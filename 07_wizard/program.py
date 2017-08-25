import random
import time
import actors

def print_header():
    print('---------------------------')
    print('  WIZARD GAME APP')
    print('---------------------------')
    print()


def game_loop():

    creatures = [
        actors.SmallAnimal('Toad', 1),
        actors.Creature('Tiger', 12),
        actors.SmallAnimal('Bat', 3),
        actors.Dragon('Dragon', 50, scaliness=20, fireness=True),
        actors.Wizard('Evil Wizard', 1000),
    ]

    hero = actors.Wizard('Gandalf', 100)

    while True:
        active_creature = random.choice(creatures)
        print()
        print(f'A {active_creature} has appear from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('runawy')
        elif cmd == 'l':
            print(f' A wizard {hero.name} takes in surroundings and sees:')
            for creature in creatures:
                print(f' * {creature}')
        else:
            print('exiting')
            break

        if not creatures:
            print('Ha! Another mighty victory!')
            break


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()