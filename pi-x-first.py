# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:32:48 2017

"""

from data_import import dataManager
from decider_classes import piDecider
from game_model import gameModel
import sys

def main() :
    usage = "Please invoke this command with python2 pi-x-first.py <pi> <nAgents> <numRounds> <alternativeReputation>"

    if (len(sys.argv) < 4) :
        print(usage)
        return(1)
    else:
        pi = int(sys.argv[1])
        nagents = int(sys.argv[2])
        nrounds = int(sys.argv[3])
        alternativeReputation = bool(sys.argv[4]) if (len(sys.argv) == 5) else False

    print("Running pi-x-first with the parameter", pi, nagents, nrounds, alternativeReputation)
    # main goes here
    # dM = dataManager()

    # checking if there is a return:
    # dM.printValues("SELECT * FROM Users LIMIT 20")

    # Example of getting the reputation in Round 2 for each Worker
    # for USER ID: 00212664-6c71-4e24-b61d-c7776f7a7d99
    # and the Workers level

    # set the switch parameter
    #pi = 1
    # set how many agents
    #nagents = 10
    # set how many rounds
    #nrounds = 5

    # init everything
    pd = piDecider(pi)
    game_model = gameModel(nagents, nrounds, alternativeReputation)

    # run
    for r in range(0, nrounds):
        # play the agile manager game in day r
        print("=" * 70)
        print("Playing round " + str(r + 1))

        # current visible worker reputation can now be accessed using
        reputation = game_model.getWorkerReputation()

        # Run the decider on current task/reputation set
        pd.decide(game_model)

        # assignments can now be accessed using
        assigns = pd.assignments

        # print dada for current round
        for i in range(nagents):
            print("-" * 70)
            print("Agent:\t" + str(i + 1))
            print("Reputation:\t" + str(reputation[i]))
            print("New Assigned:\t" + str(assigns[i]))

        # advance one day using previously generated assignments
        game_model.executeGame(pd.assignments)


if __name__ == "__main__" :
    main()
