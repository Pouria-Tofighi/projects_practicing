import random

def monty_hall(switch_door: bool) -> bool:
    """
    Simulate a single Monty Hall game.

    :param bool switch_doors: If True, the contestant will switch their choice after a goat door is revealed.
    :return: True if the contestant won the car, False otherwise.
    :rtype: bool 
    """

    doors = ['car'] + ['goat'] * 2
    random.shuffle(doors)

    initial_door = random.choice(range(3))

    revealed_doors = [i for i in range(3) if i != initial_door and doors[i] == 'goat']
    revealed_door = random.choice(revealed_doors)
    
    if switch_door:
        final_choice = [i for i in range(3) if i != initial_door and i != revealed_door][0]
    else:
        final_choice = initial_door

    return doors[final_choice] == 'car'


def simulate_game(run_game: int = 1000):
    """
    Simulates a number of monty_hall games and returns the statistics. 

    :param run_game int: the number of game which should run. 
    :return: None 
    """

    num_wins_without_switching = sum(monty_hall(switch_door=False) for _ in range(run_game))
    num_wins_with_switching = sum(monty_hall(switch_door=True) for _ in range(run_game))

    return num_wins_without_switching, num_wins_with_switching


if __name__ == "__main__":
    num_game = int(input("Enter the number of games: "))

    num_wins_without_switching, num_wins_with_switching = simulate_game(num_game)

    print(f"The percentage of wins without switching door: {num_wins_without_switching/num_game}")
    print(f"The percentage of wins with switching door: {num_wins_with_switching/num_game}")


