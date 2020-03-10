#!/usr/bin/env python3

import random


class Dice:
    """
    Dice object represents dice roll.

    By instantiating Dice we can refer to Dice.number method to fetch rolled number.
    The dice can roll any configured range - not only 1-6. For example dice_min=5 and dice_max=15 can simulate engineer
    who can process from 5 to 15 tickets per day.
    """
    def __init__(self, dice_min, dice_max):
        self.number = random.randint(dice_min, dice_max)


class Box:
    """
    Box object represents single box.

    Box instantiates having 0 marbles in it.
    The class has all required methods to load and unload it as game rules requires.
    We deliberately use "intention_to_load" keyword to indicate that actual move of the marbles does not always result
    to the same count as roll of the dice as we are restricted to the next box size as well as limited marbles count in
    existing box.
    """
    def __init__(self, max_marbles):
        self.marbles_count = 0
        self.size = max_marbles
        self.marbles_in = 0
        self.marbles_in_overrun = 0
        self.marbles_out = 0

    def load(self, intention_to_load):
        overrun = self.marbles_count + intention_to_load - self.size
        self.marbles_in_overrun = 0 if overrun < 0 else overrun
        self.marbles_in = intention_to_load - self.marbles_in_overrun
        self.marbles_count = self.marbles_count + self.marbles_in

    def deliver(self, intention_to_load):
        self.marbles_in = intention_to_load
        self.marbles_count = self.marbles_count + self.marbles_in

    def unload(self, intention_to_unload):
        overrun = intention_to_unload - self.marbles_count
        overrun = 0 if overrun < 0 else overrun
        self.marbles_out = intention_to_unload - overrun
        self.marbles_count = self.marbles_count - self.marbles_out


class Game:
    """
    Game objects instantiates row of the boxes as well as sets the method to play the round.

    By calling do_the_round method we mek each player roll the dice an move marbles one time
    We can access status_list method to see how much marbles we have in each box after any given round.
    """
    def __init__(self, number_of_boxes, box_size):
        row_of_boxes_list = []
        for box in range(number_of_boxes):
            row_of_boxes_list.append(Box(box_size))
        self.row_of_boxes = row_of_boxes_list
        self.status_list = [b.marbles_count for b in self.row_of_boxes]

    def do_the_round(self, dice_min, dice_max):
        for box_index, box in enumerate(self.row_of_boxes):
            toss = Dice(dice_min, dice_max)
            if box_index == 0:
                box.load(toss.number)
            else:
                self.row_of_boxes[box_index - 1].unload(toss.number)
                if box_index == len(self.row_of_boxes) - 1:
                    box.deliver(self.row_of_boxes[box_index - 1].marbles_out)
                else:
                    box.load(self.row_of_boxes[box_index - 1].marbles_out)
                    self.row_of_boxes[box_index - 1].load(box.marbles_in_overrun)
        self.status_list = [b.marbles_count for b in self.row_of_boxes]


class GameSet:
    """
    GameSet object represents entire game.

    By instantiating this class we play the game from start to finish.
    average_delivery_list method returns list of average delivery after each round.
    """
    def __init__(self, number_of_boxes, box_size, rounds, dice_min, dice_max):
        self.game_set = Game(number_of_boxes, box_size)
        self.average_delivery_list = []
        for i in range(rounds):
            self.game_set.do_the_round(dice_min, dice_max)
            average_delivery = self.game_set.status_list[-1] / (i + 1)
            print(self.game_set.status_list)
            print("Round=", i + 1, "average delivery=", average_delivery)
            self.average_delivery_list.append(average_delivery)
