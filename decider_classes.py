# -*- coding: utf-8 -*-
"""
Author:
Moritz Hoffmann <moritz.hoffmann@jupiter.uni-freiburg.de>
"""

import math
import numpy

from game_model import gameModel
from data_import import dataManager


class Trial :
    """ depreciated """
    def __init__(self, session_id) :
        self.dM = dataManager()
        self.nrounds = 5
        self.gm = gameModel(len(self.workers), self.nrounds)
        self.tasks = self.dM.getValuesAsPandasObject("SELECT * FROM Tasks")
        self.workers = gm.getWorkerReputation()  # update worker reputation data

        self.sid = session_id  # session ID as in the raw data
        self.day = 1  # day number = round


    def get_worker_reputation(self) :
        """ load worker ratings for current day from database """
        #query = ("SELECT 'Worker Agent Reputation' FROM 'Decisions' \
        #         WHERE 'Session ID'='%s' AND 'Round'='%d'" % (self.sid, self.day))
        query = ("SELECT \"Worker Agent Reputation\" FROM Decisions \
                WHERE \"Session ID\"=\"%s\" AND \"Round\"=\"%d\" ;"
                %  (self.sid, self.day))
        self.workers = self.dM.getValuesAsPandasObject(query)

    def new_day(self) :
        self.day += 1
        self.workers = gm.getWorkerReputation()  # update worker reputation data
        gm.executeGame(assignments)


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
        print("Using search phase")
        print(game_model.round)
        # assuming even distribution
        n = game_model.numAgents  # count workers (should be 10)
        m = game_model.numTasks
        self.assignments = [math.ceil(m/n)] * n

    def stand(self, game_model) :
        """
        try to model people's decisions in the stand phase, e.g.
          - distribute tasks among N top-rated workers or
          - fill top-rated ẀAs workload, then go to 2nd rated etc.
        # Example for generating dataset with algorithm using session id
        >>> sid = "e7e52776-2750-4cde-a5da-093ccb8feaf9"
        >>> pd = piDecider(0)
        >>> game_model = gameModel(10, 5)
        gameModel initialized
        >>> a = []
        >>> game_model.executeGame(a)
        >>> print(game_model.round)
        >>> game_model.executeGame(a)
        >>> print(game_model.round)
        >>> pd.decide(game_model)

        """
        # something like
        # p = fitted_distribution()
        # self.assignments = p
        # TODO : remove prints in this function
        print("Using stand phase")

        n = game_model.numAgents  #  count WAs
        m = game_model.numTasks  # count tasks to be done
        # calculate avg tasks per WA
        avg_tasks = [math.ceil(m/n)] * n
        i = 0
        for wa in game_model.workers * m:
            if open_tasks > 0:
                self.assignments[i] = wa
            i += 1
            print("i = " + str(i))
            print("rep = " + str(wa))
        print("assignments = " + str(self.assignments))
