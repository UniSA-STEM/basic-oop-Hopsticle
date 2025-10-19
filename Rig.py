"""
File: Rig.py
Description: This module contains the characteristics and actions that can be performed using the Rig.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# import Asset
import random

import Items


def load_assets(filename='Asset List'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('No Assets Found.')
        return []


items = load_assets()


class Rig:
    def __init__(self, name=None, level=1):
        self.name = name
        self.damage = 2
        self.level = level

        self.rig_storage_items = []

        self.set_default_rig_storage()
        self.rig_storage_capacity = Storage(self.level)
        self.rig_condition = Condition(self.damage)
        self.rig_broken_status = BrokenStatus(self.damage)

    def take_damage(self, amount=1):
        self.damage += amount
        self.update_status()

    def repair_damage(self, amount=1):
        self.damage = max(0, self.damage - amount)
        self.update_status()

    def update_status(self):
        self.rig_condition = Condition(self.damage)
        self.rig_broken_status = BrokenStatus(self.damage)

    def set_default_rig_storage(self):
        self.rig_storage_items = [Items.DataSpike(), Items.DataSpike(), Items.RemovableDrive(), '*', '*']

    def get_current_rig_storage(self):
        return self.rig_storage_items

    def __str__(self):
        return (f'Rig: {self.name} | Level: {self.level} | Damage Taken: {self.damage}'
                f'| Condition: {self.rig_condition}| Broken: {self.rig_broken_status}'
                f'\n{self.get_current_rig_storage()}')


class Storage:
    def __init__(self, level):
        if level == 1:
            self.max_capacity = 5
        elif level == 2:
            self.max_capacity = 7
        elif level == 3:
            self.max_capacity = 9
        else:
            self.max_capacity = 0

    def get_max_capacity(self):
        return self.max_capacity

    def __repr__(self):
        return f'Capacity: {self.get_max_capacity()} slots'


class Condition:
    def __init__(self, damage):

        if damage >= 3:
            self.condition = 'Blue Screen'
        elif damage > 2:
            self.condition = 'Laggy'
        elif damage > 1:
            self.condition = 'OK Performance'
        elif damage > 0:
            self.condition = 'Running Great'
        elif damage == 0:
            self.condition = 'Gem Mint'
        else:
            self.condition = 'Unknown'

    def __str__(self):
        return f'{self.condition}'

#TODO Initialise a way to calculate damage based on current level
class CalculateDamage:
    def __init__(self, damage):
        pass


#TODO ensure damage taken is accurately reflected
class DamageReduction:
    def __init__(self, level):
        self.level = level
        self.damage_taken = 0

        if level == 1:
            self.damage_taken = 1
        if level == 2:
            self.damage_taken = .75
        if level == 3:
            self.damage_taken = .6

    @property
    def damage_multiplier(self):
        return self._damage_multiplier

    @damage_multiplier.setter
    def damage_multiplier(self, value):
        self._damage_multiplier = value


class BrokenStatus:
    def __init__(self, damage):
        if damage >= 3:
            self.broken_status = True
        else:
            self.broken_status = False

    def __str__(self):
        return str(self.broken_status)

'''
# test = Rig()
# print(test)
# test.damage = Damage_Taken(0, 2)
# total_damage = test.damage and test.damage
# print(test.damage)
# print(test.damage)
#
# print(test)
'''