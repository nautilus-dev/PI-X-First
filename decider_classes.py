# -*- coding: utf-8 -*-
"""
Author:
Moritz Hoffmann <moritz.hoffmann@jupiter.uni-freiburg.de>
"""

import math
from data_import import dataManager


class Trial :
    def __init__(self, session_id) :
        self.dM = dataManager()
        self.tasks = self.dM.getValuesAsPandasObject("SELECT * FROM 'Tasks'")

        self.sid = session_id  # session ID as in the raw data
        self.day = 0  # day number = round
        self.new_day()

    def get_workers(self) :
        """ load worker ratings for current day from database """
        query = ("SELECT 'Worker Agent Reputation' FROM 'Decisions' \
                 WHERE 'Session ID'='%s' AND 'Round'='%d'" % (self.sid, self.day))
        self.workers = self.dM.getValuesAsPandasObject(query)

    def new_day(self) :
        self.day += 1
        self.get_workers()  # update worker reputation data


class piDecider :
    def __init__(self, pi=1) :
        # switch parameter. defaults to 1
        self.pi = pi

        # assignment distribution of tasks as done by algorithm
        # for current round. Compare this variable to respective
        # WA backlog queue for quick measure of accuracy
        self.assignments = []

    def decide(self, trial) :
        """
        The switch: Use method according to current state
        """
        if trial.day < self.pi :
            self.search(trial)
        else :
            self.stand(trial)

    def search(self, trial) :
        """
        try to model peoples decisions in the search phase,
        e.g. distribute tasks equally or randomly
        """
        # something like this
        # ...
        #
        # assuming even distribution
        n = len(trial.workers)  # count workers (should be 10)
        m = len(trial.tasks)  # count tasks
        self.assignments = [math.ceil(m/n)] * n

    def stand(self, trial) :
        """
        try to model people's decisions in the stand phase, e.g.
          - distribute tasks among N top-rated workers or
          - fill top-rated ẀAs workload, then go to 2nd rated etc.
        """
        # something like
        # p = fitted_distribution()
        # self.assignments = p
        pass
