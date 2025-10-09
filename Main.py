"""
File: main.py
Description: <A brief description of this Python module.>
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import time
import random

import Asset
import Hacker
import Rig


def main():
    all_hackers = []

    hacker_number = input('How many Hackers will there be? ')
    print()
    for _ in range(int(hacker_number)):
        new_hacker = (Hacker.Hacker(name=random.choice(Hacker.names),inventory=Hacker.Inventory))
        all_hackers.append(new_hacker)
        print(new_hacker)
        hacker_rig = Rig.Rig(new_hacker.name)
        print(hacker_rig)
        print()

def battle():
    turns = int(input('How many Days will you simulate? '))


main()

