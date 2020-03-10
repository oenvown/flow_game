#!/usr/bin/env python3

import matplotlib.pyplot as plt
from flowgame import GameSet
from plothelper import tableau20

global_rounds = 1000
games_list = [
    {'number_of_boxes': 3, 'box_size': 500, 'rounds': global_rounds, 'dice_min': 10, 'dice_max': 50},
    {'number_of_boxes': 5, 'box_size': 500, 'rounds': global_rounds, 'dice_min': 10, 'dice_max': 50},
    {'number_of_boxes': 5, 'box_size': 500, 'rounds': global_rounds, 'dice_min': 20, 'dice_max': 40},
    {'number_of_boxes': 5, 'box_size': 100, 'rounds': global_rounds, 'dice_min': 20, 'dice_max': 40},
    {'number_of_boxes': 3, 'box_size': 500, 'rounds': global_rounds, 'dice_min': 20, 'dice_max': 40},
]


def main():
    """
    Script runs series of games and plots average delivery dynamic graphs for each game in a single plot.

    We can specify multiple games in a global games_list variable. Each can have different parameters.
    """
    legend = []
    for game_index, game in enumerate(games_list):
        game_set = GameSet(**game)
        plt.plot(range(global_rounds), game_set.average_delivery_list, lw=1.5, color=tableau20[game_index])
        legend.append('boxes: {0}, box_size: {1}, dice_min: {2}, dice_max {3}'.format(
            game['number_of_boxes'],
            game['box_size'],
            game['dice_min'],
            game['dice_max'],
            )
        )
    plt.ylabel('Average delivery')
    plt.xlabel('Round')
    plt.legend(legend, loc='lower right')
    plt.title('Average delivery dynamics')
    plt.savefig("Average delivery dynamics.png", bbox_inches="tight", dpi=500)
    plt.show()


if __name__ == '__main__':
    main()
