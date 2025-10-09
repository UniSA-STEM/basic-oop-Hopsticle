"""
File: main.py
Description: The module containing the main running of the project.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import time
import random

import Items
import Hacker
import Rig


def main():
    all_hackers = []

    hacker_number = input('How many Hackers will there be? ')
    print()
    for _ in range(int(hacker_number)):
        new_hacker = (Hacker.Hacker(name=random.choice(Hacker.names), inventory=Hacker.Inventory()))
        chosen_name = new_hacker.name
        Hacker.names.remove(chosen_name)
        all_hackers.append(new_hacker)
        print(new_hacker)
        hacker_rig = Rig.Rig(new_hacker.name)
        print(hacker_rig)
        print()

    print(f'Hackers added:\n')
    for hacker in all_hackers:
        print(hacker.name)
    print(f'\nBy Default they start with One {Items.CryptoToken()} and a Trace Level of {hacker.trace_level}')


def battle():
    turns = int(input('How many Days will you simulate? '))


main()