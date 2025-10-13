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
import Rig
from Items import Data_Spike


def load_names(filename='Hacker Names'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []


names = load_names()

class Hacker:
    def __init__(self, name=random.choice(names),trace_level_value = 0, inventory=None, ):
        self.name = name
        self.trace_info = Trace_level(trace_level_value)
        self.rig = Rig.Rig(name=self.name)

        if inventory is None:
            self.inventory = Inventory()
        else:
            self.inventory = inventory

    def __str__(self):
        return (f'Hacker: {self.name} | {self.trace_info}'
                f'\n{self.inventory}'
                f'\n{self.rig}')


class Trace_level:
    def __init__(self, trace_level=0):
        self.trace_level = trace_level
        self.rig_level = 0
        self.set_success_chance()

    def set_trace_level(self, trace_level):
        self.trace_level = trace_level
        self.set_success_chance()

    def get_trace_level(self):
        return self.trace_level

    def set_success_chance(self):
        success_mult = 1.0

        if self.trace_level > 0:
            success_mult += self.trace_level * .3

        if success_mult != 0:
            self.success_chance = (1 / success_mult) * 100
        else:
            self.success_chance = 0.0

    def get_success_chance(self):
        return self.success_chance

    def __repr__(self):
        return f'Trace Level {self.trace_level} | Action success rate {self.get_success_chance():.2f}%'


class Inventory:
    def __init__(self):
        self.items = [Items.CryptoToken()]

    def __str__(self):
        return f'Inventory: {self.items}'


class Actions:
    def __init__(self, inventory, items):
        self.inventory = inventory
        self.items = items
        self.actions_list = ['Attack', 'Scan', '(En/De)Crypt', 'Upgrade/Repair', 'Buy', 'Extract']

    def get_list_actions(self):
        return(f'Available Actions: {(self.actions_list)}')



class Attack:
    def __init__(self, items, damage, all_hackers):
        if Items.Data_Spike in Inventory:
            input(f'Which Rig will you attack?'
                f'\n {all_hackers.name}')
            for rig in all_hackers:
                Inventory(self.items).remove(Data_Spike)


class Scan():
    def __init__(self, all_hackers):
        return(all_hackers.name)




#     if Items.CryptoToken in Hacker.name(Inventory):
#         action_upgrade = True
#     if Items.CryptoToken in Hacker.name(Inventory) and hacker_rig.name.damage > 0:
#         action_repair = True
#     if Items.Security_Chip in Hacker.name(Inventory) and:
#         action_encrypt = True
#     if Items.Security_Chip in Hacker.name(Inventory) and:
#         action_decrypt = True
#     action_buy = True
#     if Items.Removable_Drive in Hacker.name(Inventory) and Hacker.name(Rig.name).Asset:
#         action_extract = True

# go = Actions.get_list_actions
# print(go)

# class Scan:
#     def __init__(self):

# Scan Inventory
# print(Inventory)
# #Store and retrieve
# self.inventory = append.item
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
