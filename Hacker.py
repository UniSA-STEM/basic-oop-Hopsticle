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
import Main
import Rig
from Main import all_hackers


def load_names(filename='Hacker Names'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []


names = load_names()
class ActionCounter:
    def __init__(self):
        counter = 0

class Hacker:
    def __init__(self, name=random.choice(names),trace_level_value = 0, inventory=None, ):
        self.name = name
        self.trace_info = TraceLevel(trace_level_value)
        self.rig = Rig.Rig(name=self.name)

        self.scanned_hackers = []

        if inventory is None:
            self.inventory = Inventory()
        else:
            self.inventory = inventory

    def __str__(self):
        return (f'Hacker: {self.name} | {self.trace_info}'
                f'\n{self.inventory}'
                f'\n{self.rig}')


class TraceLevel:
    def __init__(self, trace_level=0):
        self.trace_level = trace_level
        self.rig_level = 0
        self.set_success_chance()

    def set_trace_level(self, trace_level):
        self.trace_level = trace_level
        self.set_success_chance()

    def get_trace_level(self):
        return self.trace_level

    def increase_trace_level(self):
        self.trace_level += 1

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

    def successful_action(self):
        random_chance = random.uniform(0, 100)
        is_successful = random_chance <= self.success_chance

        self.increase_trace_level()

        print(f'Successful Action: {self.success_chance} Trace Level Increased: {self.trace_level}' )

        return is_successful

    def __repr__(self):
        return f'Trace Level {self.trace_level} | Action success rate {self.get_success_chance():.2f}%'

class Inventory:
    def __init__(self):
        self.items = [Items.CryptoToken()]

    def has_item(self, item_class):
        # Checks if any item in the list is an instance of the class provided (item_class)
        return any(isinstance(item, item_class) for item in self.items)

    def remove_item(self, item_class):
        for i, item in enumerate(self.items):
            # Find the first item that matches the class type
            if isinstance(item, item_class):
                self.items.pop(i)
                return True  # Item removed successfully
        return False  # Item not found

    def __str__(self):
        item_names = [item.__class__.__name__ for item in self.items]
        return f'Inventory: {", ".join(item_names)}'

#TODO return the correct actions and include way to exit the menu, implement Lay Low to reduce trace level by 2
class Actions:
    def __init__(self):
        self.hacker_actions_list = ['Attack', 'Scan', 'Encrypt', 'Decrypt', 'Lay Low']
        self.rig_actions_list = ['Extract', 'Upgrade', 'Repair']

    def get_list_actions(self):
        return(f'Hacker Actions: {(self.hacker_actions_list)}\n'
               f'Rig Actions: {(self.rig_actions_list)}')

    #TODO implement actions for held items?
    def available_actions(self):
        return(f'Available Actions: {(self.hacker_actions_list)}')


#TODO Complete attack and damage calculation integration
class Attack:
    def __init__(self, active_hacker, target_hacker):
        hacker = active_hacker
        if not hacker.inventory.has_item(Items.DataSpike):
            print('You need a Data Spike to attack.')
            return

        if hacker.trace_info.successful_action():
            print(f"Attack successful against {target_hacker.name}'s Rig!")
        else:
            print('Attack failed, Data Spike lost.')

        hacker.inventory.remove_item(Items.DataSpike)

class Scan():
    def __init__(self, active_hacker, all_hackers):
        hacker = active_hacker

        not_scanned_hackers = [
            target
            for target in all_hackers
            if target.name != hacker.name  # Exclude self
               and target.name not in [s.name for s in hacker.scanned_hackers]
        ]

        print(f'Scanning for Rigs...')

        if not not_scanned_hackers:
            print('No new Rigs found. Network is fully explored.')
            return

        found_rig = random.choice(not_scanned_hackers)
        hacker.scanned_hackers.append(found_rig)

        print(f'Rig found: {found_rig.name}')
        self.found_hackers(hacker)

    def found_hackers(self, active_hacker):
        scanned_list = active_hacker.scanned_hackers

        if scanned_list:
            print(f'Scanned Hackers Found So Far ({len(scanned_list)}):')
            for hacker in scanned_list:
                print(f'- {hacker.name}')
        else:
            print('No Hackers found yet.')

#TODO Initialise the remainder og the actions
# class Decrypt:
#     def __init__(self):
#         decrypt_menu = True
#         while decrypt_menu is True:
#             if Items.Security_Chip in Inventory:
#                 Inventory.items.remove(Items.SecurityChip)
#                 for items in inventory with Items.ItemTally() Encrypted = True
#                     Encrypted = False

# class Encrypt:
#     def __init__(self):
#         encrypt_menu = True
#         while encrypt_menu is True:
#             if Items.Security_Chip in Inventory:
#                 Inventory.items.remove(Items.SecurityChip)
#                 for items in inventory with Items.ItemTally() Encrypted = False
#                     Encrypted = True

# class Upgrade:
#     def __init__(self):
#         upgrade_menu = True
#         while upgrade_menu is True:
#             if self.rig.level >= 3:
#                 print('You cannot upgrade further')
#             else:
#                 self.rig.level = self.rig.level + 1
#                 self.inventory.remove(Items.HardwarePatch)


# class Repair:
#     def __init__(self, all_hackers):
#         repair_menu = True
#         while repair_menu is True:
#             if self.rig.damage_taken == 0:
#                 print(f'You cannot use this item')
#             else:
#                 self.rig.damage_taken - 1

# class Extract:
#     def __init__(self):
#         extract_menu = True
#         while extract_menu is True:
#             for items in Rig.Storage:
#                 if ItemTally() encrypter = False
#                 items.remove(self.Rig.storage)
#                 items.append(Inventory)


class LayLow:

    def __init__(self, active_hacker):
        hacker = active_hacker

        current_trace = hacker.trace_info.get_trace_level()

        if current_trace <= 0:
            print(f'{hacker.name}')
            return

        print(f'{hacker.name} is successfully laying low')
        new_trace = max(0, current_trace - 2)
        hacker.trace_info.set_trace_level(new_trace)
        print(f'Successfully laid low. Trace Level reduced from {current_trace} to {new_trace}.')

#TODO Potentially implement a Black Market for items
#action_buy = True


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
