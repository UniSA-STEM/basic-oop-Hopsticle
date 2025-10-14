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

def game_info():
    print('Welcome to Cyber-Scape!'
          '\nThis is a Battleground where Hackers are pitted against one another to steal assets and'
          'destroy one another to rise to the top.'
          '\nAre you up the the Challenge?!\n')

def main():
    all_hackers = []
    default_level_instance = Hacker.TraceLevel()
    hacker_number = input('How many Hackers will there be? ')
    print()

    for _ in range(int(hacker_number)):
        new_hacker = (Hacker.Hacker(name=random.choice(Hacker.names), inventory=Hacker.Inventory()))
        chosen_name = new_hacker.name
        Hacker.names.remove(chosen_name)
        all_hackers.append(new_hacker)
        print(new_hacker)
        print()

    print(f'Hackers added:')
    for hacker in all_hackers:
        print(hacker.name)
    print(
        f'** By Default they start with One {Items.CryptoToken()}'
        f' and a Trace Level of {default_level_instance.get_trace_level()} **')
    print()
    game_manager = GameManager(all_hackers)
    game_manager.start_game()

class GameManager():
    def __init__(self, all_hackers):
        self.all_hackers = all_hackers
        self.num_hackers = len(self.all_hackers)
        self.turn = 0
        self.current_hacker = None
        self.game_running = True

    def get_current_hacker(self):
        self.current_hacker = self.all_hackers[self.turn % self.num_hackers]
        return self.current_hacker

    #TODO ensure that for next hackers turn their Rig is displayed
    def next_turn(self):
        self.turn += 1

    def menu(self, active_hacker):
        print(f'** It is currently {active_hacker.name}\'s turn **')
        print('---Menu---'
              '\n1. Actions'
              '\n2. Items'
              #TODO implement tig actions alongside normal actions
              '\n3. Hackers'
              '\n10. Exit')

        while self.game_running is True:
            menu_choice = int(input('What menu would you like to explore? '))
            if menu_choice == 1:
                self.actions_menu(self.current_hacker)
            elif menu_choice == 2:
                self.items_menu()
            elif menu_choice == 10:
                self.game_running = False

    #TODO change so that encrypted status only shows when hacker is looking at storage or inventory
    def items_menu(self):
        print(*Items.load_items(),sep=', ')
        item_input = input('Which item would you like information on? ').lower()
        found_item_name = None

        try:
            ItemClass = getattr(Items, item_input)
            item_instance = ItemClass()
            print(f'{item_input}: {item_instance.description}')
        except AttributeError:
            print(f'Item {item_input} not found')
        except Exception:
            pass

    #TODO potentially implement a way of only showing actions based on current inventory
    def actions_menu(self, active_hacker):
        actions_instance = Hacker.Actions('', '')
        print(actions_instance.get_list_actions(),sep= ', ')
        print()
        action_menu_choice = input('What action will you take? ')
        if action_menu_choice == 'attack' or '1':
            #TODO Print list of attack targets based on found rigs from scan, have user select rig to deal damage
            Hacker.Attack(active_hacker)
        if action_menu_choice == 'Scan' or '2':
            Hacker.Scan(active_hacker)
        #TODO ensure that each hacker can only take one action per turn on completion


    def start_game(self):

        while self.game_running:
            active_hacker = self.get_current_hacker()

            self.menu(active_hacker)

            if self.game_running:
                self.next_turn()


if __name__ == '__main__':
    game_info()
    main()


