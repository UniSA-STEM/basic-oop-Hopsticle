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

    def __repr__(self):
        return f'Trace Level {self.trace_level} | Action success rate {self.get_success_chance():.2f}%'

    def  successful_action(self):
        self.action_success = False

        random_chance = random.uniform(0, 100)
        if random_chance <= self.success_chance:
            print('Successful Action')
            self.action_success = True
            self.increase_trace_level()
        else:
            print('Failed Action')

class Inventory:
    def __init__(self):
        self.items = [Items.CryptoToken()]

    def __str__(self):
        return f'Inventory: {self.items}'

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
    def __init__(self, items,attacker, all_hackers):
        attack_menu = True
        self.attacker = attacker
        self.scanned_hackers = Scan.scanned_hackers
        Scan(self.scanned_hackers)

        while attack_menu is True:
            if Items.DataSpike in self.attacker.inventory.items:
                Scan.scanned_hackers()
                attack_choice = input(f'Which Rig will you attack? (x to cancel)')
                if attack_choice == 'x':
                    print('Cancelled by user')
                    attack_menu = False

                # elif attack_choice in Scan.scanned_hackers():
                #     Rig.calculate_damage for attack_choice

            else:
                print('You need a Data Spike to attack.')


                for rig in all_hackers:
                    Inventory.remove(Items.DataSpike)


#TODO Ensure scan accurately returns only one rig found per scan
class Scan():
    def __init__(self):
        self.scanned_hackers = []
        self.not_scanned_hackers = all_hackers.copy()
        print(Main.all_hackers)

        print(f'Scanning for Rigs')
        while self.not_scanned_hackers:
            found_rig = random.choice(self.not_scanned_hackers)
            self.scanned_hackers.append(found_rig)
            self.not_scanned_hackers.remove(found_rig)
        else:
            print(f'No Rigs found')

            for hacker in self.scanned_hackers:
                print(f'- {hacker.name}')

        #TODO implement turn ender and counter

    def found_hackers(self):
        if self.scanned_hackers:
            print(f'Scanned Hackers: {self.scanned_hackers}')
        else:
            print(f'No Hackers found')

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
