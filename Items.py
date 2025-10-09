"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


def load_items(filename='Usable Items'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('No Items File Found.')
        return []

items = load_items()


class CryptoToken:  # Used to buy Rig or remove Damage
    def __str__(self):
        return 'CryptoToken'


class Data_Spike:  # Required to deal damage to another Rig
    def __str__(self):
        return 'Data Spike'


class Removable_Drive:  # Required to store and move Assets
    def __repr__(self):
        return 'Removable Drive'


class Security_Chip:  # Required to Encrypt or Decrypt Hacker or Rig Inventory
    def __repr__(self):
        return 'Security Chip'


class Hardware_Patch:  # Required to level up a Rig
    def __repr__(self):
        return 'Hardware Patch'
