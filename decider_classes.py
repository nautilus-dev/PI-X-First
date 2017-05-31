# -*- coding: utf-8 -*-
"""
Author:
Moritz Hoffmann <moritz.hoffmann@jupiter.uni-freiburg.de>
"""

import math
import numpy

from game_model import gameModel
from data_import import dataManager


class piDecider :
    def __init__(self, pi=1) :
        # switch parameter. defaults to 1
        self.pi = pi

        # assignment distribution of tasks as done by algorithm
        # for current round. Compare this variable to respective
        # WA backlog queue for quick measure of accuracy
        self.assignments = []

    def decide(self, game_model) :
        """
        The switch: Use method according to current state
        """
        self.assignments = [0] * game_model.numAgents
        if game_model.round < self.pi :
            self.search(game_model)
        else :
            self.stand(game_model)

    def search(self, game_model) :
        """
        try to model peoples decisions in the search phase,
        e.g. distribute tasks equally or randomly
        """
        # TODO remove print statements in this function
        # TODO (optional) make distribution respect effort units instead of tasks
        print("Using search phase")
        print("round = " + str(game_model.round) + "\t" +
              "pi = " + str(self.pi))
        # assuming even distribution of tasks (not effort units)
        n = game_model.numAgents  # count workers (should be 10)
        m = game_model.numTasks
        self.assignments = [math.ceil(m/n)] * n
        print("assignments = " + str(self.assignments))
        return self.assignments

    def stand(self, game_model) :
        """
        try to model people's decisions in the stand phase, e.g.
          - distribute tasks among N top-rated workers or
          - fill top-rated ẀAs workload, then go to 2nd rated etc.
        >>> pd = piDecider(0)
        >>> game_model = gameModel(10, 5)
        gameModel initialized
        >>> a = []
        >>> game_model.executeGame(a)
        >>> pd.decide(game_model)

        """
        # TODO : remove prints in this function
        print("Using stand phase")
        print("round = " + str(game_model.round) + "\t" +
              "pi = " + str(self.pi))
        print(game_model.reputation)
        n = game_model.numAgents  #  count WAs
        m = game_model.numTasks  # count tasks to be done
        # calculate avg tasks per WA
        avg_tasks = [math.ceil(m/n)] * n
        open_tasks = m
        game_model.reputation = [i/10. for i in range(1, 11)]
        print(game_model.reputation)
        total_rep = sum(game_model.reputation)
        # iterate through workers and assign open tasks
        i = 0
        for rep in game_model.reputation:
            assign = int(rep/total_rep * m)
            self.assignments[i] = ["job_id"] * assign
            i += 1
        print("assignments = " + str(self.assignments))
        return self.assignments
