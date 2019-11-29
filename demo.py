#!/usr/bin/python3

import random


def scenario1():
    """Just random picking"""
    prize_position = random.randint(0, 2)
    first_choice = random.randint(0, 2)

    return first_choice == prize_position

def scenario2():
    """Before checking, eliminate one random non-prize door, then ask to switch"""
    prize_position = random.randint(0, 2)
    #print(f"prize_position:{prize_position}")
    first_choice = random.randint(0, 2)
    #print(f"first_choice:{first_choice}")

    opened_door = random.choice([i for i in range(3) if i not in {prize_position, first_choice}])
    #print(f"opened_door:{opened_door}")
    switched_choice = min({0, 1, 2} - {opened_door, first_choice})
    #print(f"switched_choice:{switched_choice}")

    return switched_choice == prize_position

def scenario3():
    """Switch to another door randomly"""
    prize_position = random.randint(0, 2)
    #print(f"prize_position:{prize_position}")
    first_choice = random.randint(0, 2)
    #print(f"first_choice:{first_choice}")

    opened_door = random.choice({0,1,2} - {prize_position, first_choice})
    #print(f"opened_door:{opened_door}")
    switched_choice = min({0, 1, 2} - {opened_door, first_choice})
    #print(f"switched_choice:{switched_choice}")

    return random.choice([switched_choice, first_choice]) == prize_position

def success_rate(scenario, tries=100000):
    successes = 0
    for i in range(tries):
        if scenario():
            successes += 1
    return successes / tries

def main():
    # we want to simulate monty hall problem and demonstrate the success 
    # rate of the two strategies: switching vs nonswitching

    print(f"Scenario 1 (non-switching) success rate is:      {success_rate(scenario1)}")
    print(f"Scenario 2 (switching) success rate is:          {success_rate(scenario2)}")
    print(f"Scenario 3 (randomly switching) success rate is: {success_rate(scenario3)}")

    

if __name__ == "__main__":
    main()
