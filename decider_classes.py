# -*- coding: utf-8 -*-
"""
Author:
Moritz Hoffmann <moritz.hoffmann@jupiter.uni-freiburg.de>
"""

import math
import numpy
import random
import Queue

from game_model import gameModel
from data_import import dataManager


class piDecider :
    def __init__(self, pi=1) :
        # switch parameter. defaults to 1
        self.pi = pi

        # assignment distribution of tasks as done by algorithm
        # for current round. Compare this variable to respective
        # WA backlog queue for quick measure of accuracy

    def decide(self, game_model) :
        """
        The switch: Use method according to current state
        """
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
        self.assignments = [[random.randint(1,30) \
                for i in range(int(math.ceil(m/n)))] for i in range(n)]
        print("assignments = " + str(self.assignments))

    def stand(self, game_model) :
        """
        try to model people's decisions in the stand phase, e.g.
          - distribute tasks among N top-rated workers or
          - fill top-rated ẀAs workload, then go to 2nd rated etc.
        """
        # TODO: remove prints in this function
        # TODO: une effort units instead of tasks
        # TODO: (optional) fix double data numTasks
        print("Using stand phase")
        n = game_model.numAgents  #  count WAs
        m = game_model.numTasks  # count tasks to be done
        # calculate avg tasks per WA
        avg_tasks = [math.ceil(m/n)] * n
        # fetch tasks for current round
        tasks = Queue.Queue(m)
        # TODO: This
        for i in range(m):
            tasks.put(random.randint(1,30))
        total_rep = sum(game_model.reputation)
        # iterate through workers and assign open tasks
        i = 0
        self.assignments = [[]] * n
        for i in range(n):
            self.assignments[i] = []
            rep = game_model.reputation[i]
            assigns = int(rep/total_rep * m)
            for j in range(assigns):
                task = tasks.get()
                self.assignments[i].append(task)
        print("assignments = " + str(self.assignments))
