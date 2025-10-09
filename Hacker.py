"""
File: Hacker.py
Description: This module contains the actions permitable by the Hacker class and it's associated links.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
import Items
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

        if inventory is None:
            self.inventory = Inventory()
        else:
            self.inventory = inventory
        self.trace_level = trace_level

    def __str__(self):
        return (f'Hacker: {self.name} | Trace Level {self.trace_level}'
                f'\n{self.inventory}')

class Inventory:
    def __init__(self):
        self.items = [Items.CryptoToken(),'']

    def __str__(self):
        return f'Inventory: {self.items}'

#Scan Inventory
# print(Inventory)
# #Store and retrieve
# self.inventory = append.item
# #Attack - Requires Data Spike
# Data Spike - Target - Minus from Inventory
# #Extract Asset - Requires Removable Drive
# Check Items for Encrypted - Extract Those
# #Encrypt - Requires Security Chip in inventory
# Check for decrypted and ecrypt items
# #Upgrade Rig - Requires Hardware Patch in Inventory
# Use Hardware Patch to upgrade rig
# #Repair Rig - Requires Crypto Token
# Use cryptoToken to acquire or repair rig damage
# #Buy from black market
# selection = input('What would you like to purchase? (x to exit')
# if selection == 'x':
#     exit()
#     elif selection = 1: