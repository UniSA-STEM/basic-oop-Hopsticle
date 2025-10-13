"""
File: Asset.py
Description: The Module that houses the usable items of the hackers.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
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

class ItemTally():
    def __init__(self, name, description, encrypted=False):
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def __str__(self):
        return f'{self.name} | Encrypted: {self.encrypted} | {self.description}'

class CryptoToken:  # Used to buy Rig or remove Damage
    def __init__(self):
        self.description = 'CryptoToken is used to Buy a new Rig or Repair one Damage point'
    def __repr__(self):
        return 'CryptoToken'

class Data_Spike:  # Required to deal damage to another Rig
    def __init__(self):
        self.description = 'Data Spike is used to deal one instance of Damage to a Rig'
    def __repr__(self):
        return 'Data Spike'

class Removable_Drive:  # Required to store and move Assets
    def __init__(self):
        self.description = "Removable Drive is used to extract Decrypted Assets from a Rig"
    def __repr__(self):
        return 'Removable Drive'

class Security_Chip:  # Required to Encrypt or Decrypt Hacker or Rig Inventory
    def __init__(self):
        self.description = "Security Chip is used to Encrypt Assets held within Rig Inventory"
    def __repr__(self):
        return 'Security Chip'

class Hardware_Patch:  # Required to level up a Rig
    description = "Hardware Patch is used to Upgrade a Rig to the next Level"
    def __init__(self):
        pass
    def __repr__(self):
        return 'Hardware Patch'