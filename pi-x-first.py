# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:32:48 2017

"""

from data_import import dataManager
from decider_classes import piDecider
from game_model import gameModel


def main() :
    # main goes here
    # dM = dataManager()

    # checking if there is a return:
    # dM.printValues("SELECT * FROM Users LIMIT 20")

    # Example of getting the reputation in Round 2 for each Worker
    # for USER ID: 00212664-6c71-4e24-b61d-c7776f7a7d99
    # and the Workers level

    # set the switch parameter
    pi = 1
    # set how many agents
    nagents = 10
    # set how many rounds
    nrounds = 2

    # init everything
    pd = piDecider(pi)
    game_model = gameModel(nagents, nrounds)

    # run
    for r in range(0, nrounds):
        game_model.getWorkerReputation()
        pd.decide(game_model)
        game_model.executeGame(pd.assignments)


if __name__ == "__main__" :
    main()
