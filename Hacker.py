"""
File: Hacker.py
Description: This module contains the actions permitable by the Hacker class and it's associated links.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
import Asset
# import Rig

def load_names(filename='Hacker Names'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []


names = load_names()

class Hacker:
    def __init__(self, name=random.choice(names), inventory=None, trace_level=0):
        self.name = name
        self.inventory = inventory()
        self.trace_level = trace_level

    def __str__(self):
        return (f'Hacker: {self.name} | Trace Level {self.trace_level},'
                f'\n{self.inventory}')

class Inventory:
    def __init__(self):
        self.inventory = [Asset.CryptoToken(),'']

    def __str__(self):
        return (f'Inventory: {self.inventory}')