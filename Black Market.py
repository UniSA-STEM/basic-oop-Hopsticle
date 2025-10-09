"""
File: Asset.py
Description: The Market which holds all of the items for sale for use by hackers.
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
        print('Names file not found.')
        return []

items = load_items()


class Black_Market:
    def __init__(self, offerings=items):
        self.offerings = offerings

    def __str__(self):
        return f'Welcome to Black Market'
        for index, offering in enumerate(items):
            print(f'{index + 1}. {offering}')
            print()


print(Black_Market)