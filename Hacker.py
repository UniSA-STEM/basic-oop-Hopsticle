"""
File: Hacker.py
Description: This module contains the actions permittable by the Hacker class along with it's associated links.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
import Items
import Rig


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
    def __init__(self, name=random.choice(names),trace_level_value = 0, inventory=None, ):
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
        self.set_success_chance()

    def decrease_trace_level(self):
        self.trace_level = max(0, self.trace_level - 1)
        self.set_success_chance()

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
        print(f'Successful Action: {self.success_chance:.2f}% Trace Level Increased: {self.trace_level}' )
        return is_successful

    def __repr__(self):
        return f'Trace Level {self.trace_level} | Action success rate {self.get_success_chance():.2f}%'

class Inventory:
    def __init__(self):
        self.items = [Items.CryptoToken(), Items.CryptoToken(), Items.CryptoToken(), Items.SecurityChip(), Items.SecurityChip(), Items.RemovableDrive(), Items.HardwarePatch()]

    def has_item(self, item_class):
        return any(isinstance(item, item_class) for item in self.items)

    def add_item(self, item_instance):
        self.items.append(item_instance)

    def remove_item(self, item_class):
        for index, item in enumerate(self.items):
            if isinstance(item, item_class):
                self.items.pop(index)
                return True
        return False

    def __str__(self):
        display_items = [format_item_display(item) for item in self.items]

        return f'Inventory: {", ".join(display_items)}'

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
            print()
            print(f'{self.hacker.name} is attacking {target_hacker.name}...')

            if self.hacker.trace_info.successful_action():
                raw_damage = 1
                target_hacker.rig.take_damage(raw_damage)
                print(f'Attack successful against {target_hacker.name}\'s Rig! Damage applied. Item consumed.')
                if target_hacker.rig.is_broken():
                    print(
                        f"\n!!! NETWORK ALERT !!! {target_hacker.name}'s Rig has been CRITICALLY DAMAGED and is VULNERABLE to EXTRACTION!")
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
                print('No new Rigs found. Maybe there aren\'t any more..')
                return

            found_rig = random.choice(not_scanned_rigs)
            hacker.scanned_rigs.append(found_rig)

            print(f'Rig found: {found_rig.name}')
            self.found_rigs(hacker)

    def found_rigs(self, active_hacker):
        scanned_list = active_hacker.scanned_rigs

        if scanned_list:
            print(f'\n--- Scanned Rigs Found So Far ({len(scanned_list)}) ---')
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
            for item in hacker.rig.rig_storage_items:
                if not isinstance(item, str) and item != '*':
                    if getattr(item, 'encrypted', False):
                        setattr(item, 'encrypted', False)
                        decrypted_count += 1

            if decrypted_count > 0:
                print(f'Decrypt Successful: {decrypted_count} assets in Rig Storage are now Decrypted.')
            else:
                print('Decrypt Failed: All assets in Rig Storage are already Decrypted or Rig Storage is empty.')
                hacker.inventory.add_item(Items.SecurityChip())
        else:
            print('Decrypt Failed: You need a Security Chip in your Inventory.')


class Encrypt:
    def __init__(self, active_hacker):
        hacker = active_hacker
        item_class = Items.SecurityChip

        if hacker.inventory.remove_item(item_class):
            encrypted_count = 0
            for item in hacker.rig.rig_storage_items:
                if not isinstance(item, str) and item != '*':
                    if not getattr(item, 'encrypted', False):
                        setattr(item, 'encrypted', True)
                        encrypted_count += 1

            if encrypted_count > 0:
                print(f'Encrypt Successful: {encrypted_count} assets in Rig Storage are now Encrypted.')
            else:
                print('Encrypt Failed: All assets in Rig Storage are already Encrypted or Rig Storage is empty.')
                hacker.inventory.add_item(Items.SecurityChip())
        else:
            print('Encrypt Failed: You need a Security Chip in your Inventory.')


class Upgrade:
    def __init__(self, active_hacker):
        hacker = active_hacker
        item_class = Items.HardwarePatch

        if hacker.rig.level >= 3:
            print(f'Upgrade Failed: {hacker.name}\'s Rig is already at maximum level (Level 3).')
            return

        if not hacker.inventory.remove_item(item_class):
            print('Upgrade Failed: You need a Hardware Patch in your Inventory.')
            return

        hacker.rig.level += 1

        hacker.rig.upgrade_storage()

        print(f'Upgrade Successful: {hacker.name}\'s Rig is now Level {hacker.rig.level}!')


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

        has_item = hacker.inventory.has_item(item_class) or hacker.rig.has_item_in_storage(item_class)
        if not has_item:
            print('Extraction Failed: Requires a Removable Drive in your Inventory or Rig Storage.')
            return

        if not (hacker.inventory.remove_item(item_class) or hacker.rig.consume_item(item_class)):
            print("Error consuming Removable Drive. Extraction cancelled.")
            return

        moved_count = 0
        moved_items_names = []

        indices_to_clear = []

        for i, item in enumerate(hacker.rig.rig_storage_items):
            if not isinstance(item, str) and item != '*':
                hacker.inventory.add_item(item)
                moved_items_names.append(type(item).__name__)
                indices_to_clear.append(i)
                moved_count += 1

        for index in indices_to_clear:
            hacker.rig.rig_storage_items[index] = '*'

        if moved_count > 0:
            print(f'Extraction Successful: Moved {moved_count} asset(s) from Rig Storage to Inventory.')
            print(f'Assets Moved: {", ".join(moved_items_names)}.')
        else:
            print('Extraction Complete: No assets were found in Rig Storage to move.')

class Exploit:
    def __init__(self, active_hacker, target_hacker):
        item_class = Items.RemovableDrive

        has_item = active_hacker.inventory.has_item(item_class) or active_hacker.rig.has_item_in_storage(item_class)
        if not has_item:
            print('Extraction Failed: Requires a Removable Drive in your Inventory or Rig Storage.')
            return

        if not target_hacker.rig.is_broken():
            print(
                f'Extraction Failed: {target_hacker.name}\'s Rig is not BROKEN (Condition: {target_hacker.rig.rig_condition}).')
            return

        if not (active_hacker.inventory.remove_item(item_class) or active_hacker.rig.consume_item(item_class)):
            print("Error consuming Removable Drive.")
            return

        extracted_count = 0
        extracted_items = []

        for i in range(len(target_hacker.rig.rig_storage_items)):
            item = target_hacker.rig.rig_storage_items[i]

            if not isinstance(item, str) and item != '*':
                active_hacker.inventory.add_item(item)
                extracted_items.append(type(item).__name__)
                extracted_count += 1

                target_hacker.rig.rig_storage_items[i] = '*'

        if extracted_count > 0:
            print(
                f'Extraction Successful! {active_hacker.name} stole {extracted_count} asset(s): {", ".join(extracted_items)} from {target_hacker.name}.')

        else:
            print(f'Extraction Successful, but {target_hacker.name}\'s Rig had no assets to steal.')


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