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
all_hackers = []

def game_info():
    print('Welcome to Cyber-Scape!'
          '\nThis is a Battleground where Hackers are pitted against one another to steal assets and '
          'destroy one another to rise to the top.'
          '\nAre you up the the Challenge?!\n')

def main():

    default_level_instance = Hacker.TraceLevel()
    hacker_success_chance = default_level_instance.get_success_chance()
    hacker_number = input('How many Hackers will there be? ')
    print()

    for _ in range(int(hacker_number)):
        new_hacker = (Hacker.Hacker(name=random.choice(Hacker.names), inventory=Hacker.Inventory()))
        chosen_name = new_hacker.name
        Hacker.names.remove(chosen_name)
        all_hackers.append(new_hacker)
        print(new_hacker)
        print('*' * 50)

    print(f'\nHackers added:\n')
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
        self.turn = 1
        self.current_hacker = None
        self.game_running = True
        self.scanned_hackers = []
        self.trace_info = None
        self.turn_index = 0
        self.global_turn = 0
        self.global_round = 1

        self.menu_items = ('\n---Menu---'
                       '\n1. Hacker Actions'
                       '\n2. Items'
                       '\n3. Hackers'
                       '\n4. View Inventory'
                       '\n5. Menu'
                       '\n9. Pass'
                       '\n10. Exit')

    def get_current_hacker(self):
        hacker_index = self.global_turn % self.num_hackers
        self.current_hacker = self.all_hackers[hacker_index]
        return self.current_hacker

    def get_current_round(self):
        return (self.global_turn // len(self.all_hackers)) + 1

    def next_turn(self):
        self.global_turn += 1

        next_hacker = self.get_current_hacker()
        next_hacker.action_points = 1


    def menu(self, active_hacker):
        print(
            f'*** ROUND {self.global_round} | {active_hacker.name}\'s Turn #{active_hacker.turns_taken + 1}'
            f' | Action Points: {active_hacker.action_points}) ***')

        print()
        print(self.current_hacker.rig)
        print(self.menu_items)

        while self.game_running is True:
            print()
            menu_choice = int(input('What menu would you like to explore? (5 for menu options) '))
            print()
            if menu_choice == 1:
                self.actions_menu(self.get_current_hacker())
            elif menu_choice == 2:
                self.items_menu()
            elif menu_choice == 3:
                Hacker.Scan.found_rigs(self)
            elif menu_choice == 4:
                print(f"--- {active_hacker.name}'s Inventory & Rig Storage ---")
                print(active_hacker.inventory)
                print(active_hacker.rig)
                print("-" * 35)
            elif menu_choice == 5:
                print(self.menu_items)
            elif menu_choice == 6:
                print(Hacker.Hacker.format_item_display(self.current_hacker.name))
                print(f'{self.current_hacker.name}\'s', (Hacker.Inventory()))

            elif menu_choice == 9:
                print(f'{active_hacker.name} is passing their turn.')
                return
            elif menu_choice == 10:
                self.game_running = False

    #TODO change so that encrypted status only shows when hacker is looking at storage or inventory
    def items_menu(self):
        print(*Items.load_items(),sep=', ')
        item_input = input('Which item would you like information on? ')
        found_item_name = None

        try:
            ItemClass = getattr(Items, item_input)
            item_instance = ItemClass()
            print(f'{item_input}: {item_instance.description}')
        except AttributeError:
            print(f'Item {item_input} not found')
        except Exception:
            pass

    def actions_menu(self, active_hacker):
        actions_instance = Hacker.Actions()
        print(actions_instance.get_list_actions(),sep= ', ')
        print()
        print(f'Current Success Chance: {self.current_hacker.trace_info.get_success_chance():.2f}%')
        action_menu_choice = input('What action will you take? ')


        if action_menu_choice == 'attack' or action_menu_choice == '1':
            Hacker.Attack(active_hacker)
            return

        elif action_menu_choice == 'scan' or action_menu_choice == '2':
            Hacker.Scan(active_hacker, all_hackers)
            return

        elif action_menu_choice == 'encrypt' or action_menu_choice == '3':
            Hacker.Encrypt(active_hacker)
            return

        elif action_menu_choice == 'decrypt' or action_menu_choice == '4':
            Hacker.Decrypt(active_hacker)
            return

        elif action_menu_choice == 'lay low' or action_menu_choice == '5':
            Hacker.LayLow(active_hacker)
            return


        elif action_menu_choice == 'exploit' or action_menu_choice == '6':
            scanned_list = active_hacker.scanned_rigs
            target_hacker = None
            selection_complete = False

            if not scanned_list:
                print('Cannot extract: No rigs have been scanned yet.')
                return

            while not selection_complete:

                Hacker.Scan().found_rigs(active_hacker)
                extract_choice = input('Who will you extract from? (Enter number, "x" to cancel): ').lower().strip()
                if extract_choice == 'x':
                    print('Extraction cancelled.')
                    return
                else:
                    try:
                        target_index = int(extract_choice)
                        if 1 <= target_index <= len(scanned_list):
                            target_hacker = scanned_list[target_index - 1]
                            selection_complete = True
                        else:
                            print(f'Invalid selection. Please choose a number between 1 and {len(scanned_list)}.')
                    except ValueError:
                        print('Invalid input. Please enter the number next to the target.')



            if target_hacker:
                Hacker.Exploit(active_hacker, target_hacker)

                return

        elif action_menu_choice == 'upgrade' or action_menu_choice == '7':
            Hacker.Upgrade(active_hacker)
            return

        elif action_menu_choice == 'repair' or action_menu_choice == '8':
            Hacker.Repair(active_hacker)
            return

        else:
            print(f'Action {action_menu_choice} not found')


    def start_game(self):

        while self.game_running:
            active_hacker = self.get_current_hacker()
            current_round = self.get_current_round()

            if current_round > 1:
                active_hacker.rig.generate_new_item()

            self.menu(active_hacker)

            if self.game_running:

                if not hasattr(active_hacker, 'turns_taken'):
                    active_hacker.turns_taken = 0
                active_hacker.turns_taken += 1

                self.next_turn()

if __name__ == '__main__':
    game_info()
    main()


