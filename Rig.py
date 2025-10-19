"""
File: Rig.py
Description: This module contains the characteristics and actions that can be performed using the Rig.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
import Items


def load_assets(filename='Usable Items'):
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
        self.rig_storage_capacity_instance = Storage(self.level)
        self.rig_storage_capacity = self.rig_storage_capacity_instance.get_max_capacity()
        self.rig_condition = Condition(self.damage)
        self.rig_broken_status = BrokenStatus(self.damage)

    def generate_new_item(self):
        if not items:
            print(f"[{self.name}'s Rig] cannot generate item: Asset list is empty.")
            return False

        if '*' in self.rig_storage_items:
            random_asset_name = random.choice(items)

            try:
                ItemClass = getattr(Items, random_asset_name)
                new_item = ItemClass()
            except AttributeError:
                print(
                    f"[{self.name}'s Rig] failed to generate item: Class '{random_asset_name}' not found in Items module.")
                return False

            try:
                empty_index = self.rig_storage_items.index('*')
                self.rig_storage_items[empty_index] = new_item
                print(f"[{self.name}'s Rig] generated a new asset: {random_asset_name}.")
                return True
            except ValueError:
                return False
        else:
            print(f"[{self.name}'s Rig] storage is full. No item generated.")
            return False

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

    def upgrade_storage(self):
        old_capacity = self.rig_storage_capacity

        self.rig_storage_capacity_instance = Storage(self.level)
        self.rig_storage_capacity = self.rig_storage_capacity_instance.get_max_capacity()

        new_slots = self.rig_storage_capacity - old_capacity

        if new_slots > 0:
            self.rig_storage_items.extend(['*'] * new_slots)
            print(
                f"Rig storage increased from {old_capacity} to {self.rig_storage_capacity} slots. Gained {new_slots} new slots.")
        else:
            print("Rig storage capacity did not change (or is maxed).")

    def __str__(self):
        storage_display = self.format_storage_display()
        return (  f'Rig:     {self.name}\'s | Level: {self.level} | Damage Taken: {self.damage}'
                f' | Condition: {self.rig_condition}| Broken: {self.rig_broken_status}'
                f'\nStorage: {storage_display}')

    def is_broken(self):
        return self.rig_broken_status.broken_status

    def format_storage_display(self):
        display_list = []
        for item in self.rig_storage_items:

            if isinstance(item, str) and item == '*':
                display_list.append('*')
                continue

            item_name = type(item).__name__

            is_encrypted = getattr(item, 'encrypted', False)

            if is_encrypted:
                display_list.append(f'{item_name} (*)')
            else:
                display_list.append(item_name)

        return ', '.join(display_list)

#TODO ensure max storage is increased and appended when level increases
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
