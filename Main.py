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

game = 1



def main():

    all_hackers = []
    hacker_number = input('How many Hackers will there be? ')
    default_level_instance = Hacker.Trace_level()

    print()
    for _ in range(int(hacker_number)):
        new_hacker = (Hacker.Hacker(name=random.choice(Hacker.names), inventory=Hacker.Inventory()))
        chosen_name = new_hacker.name
        Hacker.names.remove(chosen_name)
        all_hackers.append(new_hacker)
        print(new_hacker)
        print()

    print(f'Hackers added:\n')
    for hacker in all_hackers:
        print(hacker.name)

    print(
        f'\nBy Default they start with One {Items.CryptoToken()} and a Trace Level of {default_level_instance.get_trace_level()}.')
    print()

    manager = Turn_Manager(all_hackers)

    manager.start_game()

    while game == 1:

        def menu(current_hacker):
            print('--Menu--'
                  '\n1. Actions'
                  '\n2. Scan'
                  '\n10. Exit')
            menu_choice = int(input('What action will you take? '))
            if menu_choice == 1:
                actions_menu()
            if menu_choice == 2:
                print(all_hackers)

        def actions_menu():
            actions_instance = Hacker.Actions('','')
            print(actions_instance.get_list_actions())
            print()
            action_menu_choice = input('What action will you take? ')
            if action_menu_choice == 1:
                Hacker.Attack


        menu()

        def battle():
            turns = int(input('How many Days will you simulate? '))


if __name__ == '__main__':
    main()