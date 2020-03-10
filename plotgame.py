#!/usr/bin/env python3

from flowgame import Game
import matplotlib.pyplot as plt

game_dict = {'number_of_boxes': 10, 'box_size': 100, 'rounds': 200, 'dice_min': 5, 'dice_max': 15}


def main(number_of_boxes, box_size, rounds, dice_min, dice_max):
    """
    Script runs the game and plots wip and average delivery as the game goes.

    We can observe the interaction of statistical fluctuations and dependent events.
    Global variable game_dict can be modified to customize game parameters.
    """
    my_game = Game(number_of_boxes, box_size)
    average_delivery_list = []
    for i in range(rounds):
        my_game.do_the_round(dice_min, dice_max)
        average_delivery = my_game.status_list[-1]/(i+1)
        print(my_game.status_list)
        print("Round=", i+1, "average delivery=", average_delivery)
        average_delivery_list.append(average_delivery)

        plt.subplot(2, 1, 1)
        plt.axis([0, number_of_boxes - 2, 0, box_size*1.1])
        plt.ion()
        plt.xlabel('Box number')
        plt.ylabel('Marbles in the box')
        plt.bar(range(number_of_boxes), my_game.status_list)

        plt.subplot(2, 1, 2)
        plt.ion()
        plt.xlabel('Round')
        plt.ylabel('Average delivery,\nitems/round')
        plt.plot(range(i + 1), average_delivery_list)

        plt.tight_layout()
        plt.draw()
        plt.pause(0.001)
        plt.clf()


if __name__ == '__main__':
    main(**game_dict)
