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
        self.damage = 0.0
        self.level = level

        self.rig_storage_items = []

        self.set_default_rig_storage()
        self.rig_storage_capacity = Storage(self.level)
        self.rig_condition = Condition(self.damage)
        self.rig_broken_status = BrokenStatus(self.damage)

    def has_item_in_storage(self, item_class):
        return any(isinstance(item, item_class) for item in self.rig_storage_items)

    def consume_item(self, item_class):
        for used_item, item in enumerate(self.rig_storage_items):

            if isinstance(item, item_class):
                self.rig_storage_items.pop(used_item)
                self.rig_storage_items.append('*')
                return True
        return False

    def take_damage(self, raw_damage=1):
        damage_reduction = DamageReduction(self.level)

        effective_damage = raw_damage * damage_reduction.damage_multiplier
        self.damage += effective_damage

        self.update_status()

    def repair_damage(self, amount=1):
        self.damage = max(0.0, self.damage - amount)
        self.update_status()

    def update_status(self):
        self.rig_condition = Condition(self.damage)
        self.rig_broken_status = BrokenStatus(self.damage)

    def set_default_rig_storage(self):
        self.rig_storage_items = [Items.DataSpike(), Items.DataSpike(), Items.RemovableDrive(), '*', '*']

    def get_current_rig_storage(self):
        return self.rig_storage_items

    def __str__(self):
        return (  f'Rig:     {self.name}\'s | Level: {self.level} | Damage Taken: {self.damage}'
                f'| Condition: {self.rig_condition}| Broken: {self.rig_broken_status}'
                f'\nStorage: {self.get_current_rig_storage()}')


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
        elif damage == 0.0:
            self.condition = 'Gem Mint'
        else:
            self.condition = 'Unknown'

    def __str__(self):
        return f'{self.condition}'

#TODO Initialise a way to calculate damage based on current level


#TODO ensure damage taken is accurately reflected
class DamageReduction:
    def __init__(self, level):
        self.level = level

        if level == 1:
            self.damage_multiplier = 1
        elif level == 2:
            self.damage_multiplier = .75
        elif level == 3:
            self.damage_multiplier = .6


class BrokenStatus:
    def __init__(self, damage):
        if damage >= 3:
            self.broken_status = True
        else:
            self.broken_status = False

    def __str__(self):
        return str(self.broken_status)
