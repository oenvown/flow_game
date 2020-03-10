# Goldratt's game of flow

Game is based on the "matchstick game" played during the boy scout hike in Goldratt's book "The Goal". The basic purpose of this script is to help visualise the impact and interaction of statistical fluctuations and dependent events.

## Ruleset

1. The first player rolls the dice to determine how many marbles s/he is able to process and moves that number of marbles in to is't box. Marbles in the box represents available queue for the nex player.
2. The second player rolls the dice and processes/moves to it's "processed" queue either the number of marbles indicated on the dice or all the marbles available from the queue between the first and second operation - whichever is smaller. To simulate limiting WIP, scripts has option to specify box size. It is not allowed to move more marbles then a box size.
3. The round proceeds for each of the following players until the final operation - at which point the marbles processed are "delivered" to customers and the next round may begin

The dice can roll any configured range - not only 1-6. For example dice_min=5 and dice_max=15 can simulate engineer who can process from 5 to 15 tickets per day.

## How to Run

This project is built using Python 3.8 and requires that the user has at least Python 3 installed in order to run the program. Python 3+ can be installed [here](https://www.python.org/downloads/).

The script uses matplotlib module to plot graphs. It is required to install matplotlib to the projects virtual environment.

To run and plot the game please launch plotgame.py. You may modify game_dict variable in the script to alter number of boxes, box size, game rounds, dice_min and dice_max.
To observe how average delivery diverges with different game parameters please launch plotdelivery.py. You may modify games_list variable in the scrip to alter game parameters accordingly.
