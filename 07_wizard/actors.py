import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.name} of level {self.level}'

    def get_defensive_roll(self):
        return random.randint(1, 20) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print(f'Attacking {creature}')

        hero_roll = super().get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f'You roll {hero_roll}')
        print(f'{creature} rolled {creature_roll }')

        if hero_roll >= creature_roll:
            print(f'The Wizard {self.name} conquered {creature}')
            return True
        else:
            print(f'The Wizard {self.name} was defeated by {creature}')
            return False


class Dragon(Creature):
    def __init__(self, name, level, scaliness, fireness):
        super().__init__(name, level)
        self.fireness = fireness
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.fireness else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll/2