"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self, name, damage, broken_status, storage, level):
        self.name = name
        self.damage = 0
        self.broken_status = False
        self.storage = 1
        self.level = 0

class Storage:
    def __init__(self, level):
        if self.level == 0:
            self.storage = 1
        if self.level == 1:
            self.storage = 2
        elif:
            self.storage = 3

class Damage:
    def __init__(self):
        self.damage = 0

class BrokenStatus:
    def __init__(self, damage):
        damage = self.damage
