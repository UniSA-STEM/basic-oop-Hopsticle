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
    def __init__(self, name=None,damage=0, level=1):
        self.name = name
        self.damage = damage
        self.level = level

        self.rig_storage_items = []

        self.set_default_rig_storage()
        self.rig_storage_capacity = Storage(self.level)
        self.rig_condition = Condition(self.damage)
        self.rig_broken_status = Broken_Status(self.damage)

    def set_default_rig_storage(self):
        self.rig_storage_items = [Items.Data_Spike(), Items.Data_Spike(), Items.Removable_Drive(), '*', '*']

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

    def get_max_capacity(self, level):
        return self.max_capacity

    def __repr__(self):
        return f'Capacity: {self.get_max_capacity()} slots'


class Condition:
    def __init__(self, damage):
        if damage >= 5:
            self.condition = 'FUBAR'
        elif damage == 4:
            self.condition = 'Blue Screening'
        elif damage == 3:
            self.condition = 'Laggy'
        elif damage == 2:
            self.condition = 'OK'
        elif damage == 1:
            self.condition = 'PSA 8'
        elif damage == 0:
            self.condition = 'Gem Mint'
        else:
            self.condition = 'Unknown'

    def __str__(self):
        return f'{self.condition}'


class Broken_Status:
    def __init__(self, damage):
        if damage >= 5:
            self.broken_status = True
        else:
            self.broken_status = False

    def __str__(self):
        return str(self.broken_status)