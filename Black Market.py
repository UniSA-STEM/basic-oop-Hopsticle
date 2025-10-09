"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

def load_assets(filename='Usable Assets'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []

Usable_Assets = load_assets()

class Black_Market:
    def __init__(self, offerings=Usable_Assets):
        self.offerings = offerings


print('Welcome to Black Market.',
    *Usable_Assets, sep='\n')
