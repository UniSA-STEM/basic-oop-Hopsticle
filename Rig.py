"""
File: Rig.py
Description: This module contains the characteristics and actions that can be performed using the Rig
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""


# import Asset
import random

def load_assets(filename='Asset List'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('No Assets Found.')
        return []

items = load_assets()

class Rig:
    def __init__(self, name=None, storage=random.choice(items)*2, condition=None, damage=0, broken_status=None, level=None):
        self.name = name
        self.damage = damage
        self.broken_status = broken_status
        self.storage = Storage
        self.level = level
        self.condition = Condition

    def __str__(self):
        return (f'Rig: {self.name} | Level: {self.level} | Damage Taken: {self.damage} '
                f'| Condition: {self.condition}| Broken: {self.broken_status}'
                f'\n{self.storage}')


class Storage:
    def __init__(self, level):
        if level == 1:
            self.storage = ['*', '*']
        if level == 2:
            self.storage = ['*', '*', '*', '*']
        else:
            self.storage = ['*', '*', '*', '*', '*', '*']

    def __repr__(self):
        return f'Storage: {self.storage}'


class Condition:
    def __init__(self, damage):
        if self.damage >= 5:
            self.condition = 'FUBAR'
        if self.damage == 4:
            self.condition = 'Blue Screening'
        if self.damage == 3:
            self.condition = ''
        if self.damage == 2:
            self.condition = 'OK'
        if self.damage == 1:
            self.condition = 'PSA 8'
        if self.damage == 0:
            self.condition = 'Gem Mint'

    def __str__(self):
        return f'{self.condition}'


class BrokenStatus:
    def __init__(self, damage):
        damage = self.damage
        if self.damage >= 5:
            self.broken_status = True
        else:
            self.broken_status = False


# class Level:
#     def __init__(self):
#
#     def __str__(self):
#         return f'Level: {self.level}'
