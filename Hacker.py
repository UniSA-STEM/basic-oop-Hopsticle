'''
File: Hacker.py
Description: This module contains the actions permittable by the Hacker class and it's associated links.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
'''

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

def format_item_display(item):
    if isinstance(item, str) and item == '*':
        return item

    is_encrypted = getattr(item, 'encrypted', False)
    item_name = type(item).__name__

    if is_encrypted:
        return f'{item_name} (*)'
    else:
        return item_name

class Hacker:
    def __init__(self, name=random.choice(names),trace_level_value = 1, inventory=None, ):
        self.name = name
        self.trace_info = TraceLevel(trace_level_value)
        self.rig = Rig.Rig(name=self.name)
        self.turns_taken = 0
        self.scanned_rigs = []
        self.action_points = 1

        if inventory is None:
            self.inventory = Inventory()
        else:
            self.inventory = inventory

    def consume_item(self, item_class):
        if self.inventory.remove_item(item_class):
            return True

        if self.rig.consume_item(item_class):
            return True

        return False

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
        self.items = [Items.CryptoToken(), Items.CryptoToken(), Items.CryptoToken(), Items.SecurityChip(), Items.SecurityChip(), Items.RemovableDrive()]

    def has_item(self, item_class):
        return any(isinstance(item, item_class) for item in self.items)

    def remove_item(self, item_class):
        for index, item in enumerate(self.items):
            if isinstance(item, item_class):
                self.items.pop(index)
                return True
        return False

    def __str__(self):
        display_items = [format_item_display(item) for item in self.items]

        return f'Inventory: {", ".join(display_items)}'

#TODO return the correct actions and include way to exit the menu, implement Lay Low to reduce trace level by 2
class Actions:
    def __init__(self):
        self.hacker_actions_list = ['1. Attack', '2. Scan', '3. Encrypt', '4. Decrypt', '5. Lay Low']
        self.rig_actions_list = ['6. Extract', '7. Upgrade', '8. Repair']

    def get_list_actions(self):
        return(f'Hacker Actions: {(self.hacker_actions_list)}\n'
               f'Rig Actions: {(self.rig_actions_list)}')

class Attack:
    def __init__(self, active_hacker):
        self.hacker = active_hacker
        scanned_list = self.hacker.scanned_rigs
        item_class = Items.DataSpike

        selection_complete = False
        target_hacker = None

        has_item = self.hacker.inventory.has_item(item_class) or self.hacker.rig.has_item_in_storage(item_class)

        if not has_item:
            print('You need a Data Spike to attack.')
            selection_complete = True
        elif not scanned_list:
            print('Cannot attack: No rigs have been scanned yet. Use the "Scan" action first.')
            selection_complete = True

        while not selection_complete:
            Scan().found_rigs(self.hacker)
            attack_choice = input('Who will you attack? (Enter number, "x" to cancel): ').lower().strip()

            if attack_choice == 'x':
                print('Attack cancelled.')
                selection_complete = True
            else:
                try:
                    target_index = int(attack_choice)
                    if 1 <= target_index <= len(scanned_list):
                        target_hacker = scanned_list[target_index - 1]
                        selection_complete = True
                    else:
                        print(f'Invalid selection. Please choose a number between 1 and {len(scanned_list)}.')
                except ValueError:
                    print('Invalid input. Please enter the number next to the target.')

        if target_hacker:
            print(f'{self.hacker.name} is attacking {target_hacker.name}...')

            if self.hacker.trace_info.successful_action():
                raw_damage = 1
                target_hacker.rig.take_damage(raw_damage)
                print(f'Attack successful against {target_hacker.name}\'s Rig! Damage applied. Item consumed.')
            else:
                print('Attack failed, Data Spike lost.')

            self.hacker.consume_item(item_class)


class Scan:
    def __init__(self, active_hacker=None, all_hackers=None):
        if active_hacker and all_hackers:
            hacker = active_hacker

            not_scanned_rigs = [
                target
                for target in all_hackers
                if target.name != hacker.name
                   and target.name not in [r.name for r in hacker.scanned_rigs]
            ]

            print('Scanning for Rigs...')

            if not not_scanned_rigs:
                print('No new Rigs found. Network is fully explored.')
                return

            found_rig = random.choice(not_scanned_rigs)
            hacker.scanned_rigs.append(found_rig)

            print(f'Rig found: {found_rig.name}')
            self.found_rigs(hacker)

    def found_rigs(self, active_hacker):
        scanned_list = active_hacker.scanned_rigs

        if scanned_list:
            print(f'--- Scanned Rigs Found So Far ({len(scanned_list)}) ---')
            for index, hacker in enumerate(scanned_list, 1):
                print(f'{index}. {hacker.name}')
        else:
            print('No Rigs found yet.')


class Decrypt:
    def __init__(self, active_hacker):
        hacker = active_hacker
        item_class = Items.SecurityChip
        if hacker.inventory.remove_item(item_class):
            decrypted_count = 0
            for item in hacker.inventory.items:
                if getattr(item, 'encrypted', False):
                    setattr(item, 'encrypted', False)
                    decrypted_count += 1

            if decrypted_count > 0:
                print(f'Decrypt Successful: {decrypted_count} items in Inventory are now Decrypted.')
            else:
                print('Decrypt Failed: All items in Inventory are already Decrypted.')
                hacker.inventory.items.append(Items.SecurityChip())
        else:
            print('Decrypt Failed: You need a Security Chip in your Inventory.')


class Encrypt:
    def __init__(self, active_hacker):
        hacker = active_hacker
        item_class = Items.SecurityChip
        if hacker.inventory.remove_item(item_class):
            encrypted_count = 0
            for item in hacker.inventory.items:
                if not getattr(item, 'encrypted', False):
                    setattr(item, 'encrypted', True)
                    encrypted_count += 1

            if encrypted_count > 0:
                print(f'Encrypt Successful: {encrypted_count} items in Inventory are now Encrypted.')
            else:
                print('Encrypt Failed: All items in Inventory are already Encrypted.')
                hacker.inventory.items.append(Items.SecurityChip())
        else:
            print('Encrypt Failed: You need a Security Chip in your Inventory.')


class Upgrade:
    def __init__(self, active_hacker):
        hacker = active_hacker
        item_class = Items.HardwarePatch

        upgrade_menu = True

        if hacker.rig.level >= 3:
            print(f'Upgrade Failed: {hacker.name}\'s Rig is already at maximum level (Level 3).')
            upgrade_menu = False

        if upgrade_menu:
            if hacker.inventory.remove_item(item_class):
                hacker.rig.level += 1
                print(f'Upgrade Successful: {hacker.name}\'s Rig is now Level {hacker.rig.level}!')
            else:
                print('Upgrade Failed: You need a Hardware Patch in your Inventory.')


class Repair:
    def __init__(self, active_hacker):
        hacker = active_hacker
        action_complete = False
        repair_needed = True

        if hacker.rig.damage == 0:
            print('Rig has no damage to repair.')
            repair_needed = False
            action_complete = True
        elif not hacker.inventory.has_item(Items.CryptoToken):
            print('You need a CryptoToken to repair your Rig.')
            repair_needed = False
            action_complete = True

        while not action_complete and repair_needed:
            print(f'{hacker.name} is repairing Rig...')

            if hacker.trace_info.successful_action():

                repair_amount = 1
                hacker.rig.repair_damage(repair_amount)

                print(f'Repair successful! Damage reduced by {repair_amount}. New damage is {hacker.rig.damage}.')
            else:
                print('Repair attempted. Trace Level increased.')

            hacker.inventory.remove_item(Items.CryptoToken)

            action_complete = True


class Extract:
    def __init__(self, active_hacker):
        hacker = active_hacker
        item_class = Items.RemovableDrive

        extracted_count = 0

        if not hacker.inventory.remove_item(item_class):
            print('Extract Failed: You need a Removable Drive in your Inventory.')
            return

        rig_items = hacker.rig.rig_storage_items
        items_to_move = []
        indices_to_replace = []

        for index, item in enumerate(rig_items):
            if not isinstance(item, str) and not getattr(item, 'encrypted', False):
                items_to_move.append(item)
                indices_to_replace.append(index)

        if items_to_move:
            for item in items_to_move:
                hacker.inventory.items.append(item)
                extracted_count += 1

            for index in sorted(indices_to_replace, reverse=True):
                rig_items.pop(index)
                rig_items.append('*')

            print(f'Extract Successful: Moved {extracted_count} decrypted asset(s) from Rig Storage to Inventory.')
        else:
            print('Extract Failed: No decrypted items found in Rig Storage to extract.')
            hacker.inventory.items.append(Items.RemovableDrive())


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