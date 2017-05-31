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
        self.assignments = [[]] * game_model.numAgents
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
        avg_tasks = int(math.ceil(m/n))
        tasks = game_model.getTasks()
        for wa in range(n):
            self.assignments[wa] = []
            for i in range(avg_tasks):
                self.assignments[wa].append(tasks.get())
        print("assignments = " + str(self.assignments))

    def stand(self, game_model) :
        """
        try to model people's decisions in the stand phase, e.g.
          - distribute tasks among N top-rated workers
          - fill top-rated ẀAs workload, then go to 2nd rated etc.
        """
        # TODO: remove prints in this function
        # TODO: (optional) fix double data numTasks
        print("Using stand phase")
        # TODO: This:
        tasks = game_model.getTasks()
        while tasks.qsize() > 0:
            # iterate through tasks and assign them
            current_task = tasks.get()
            self.assignTask(current_task, game_model)
        # n = game_model.numAgents  #  count WAs
        # m = game_model.numTasks  # count tasks to be done
        # calculate avg tasks per WA
        # avg_tasks = [math.ceil(m/n)] * n
        # total_rep = sum(game_model.reputation)
        # fetch tasks from game model
        # tasks = game_model.getTasks()
        # iterate through workers and assign open tasks
        # for i in range(n):
        #    self.assignments[i] = []
        #    rep = game_model.reputation[i]
        #    assigns = int(rep/total_rep * m)
        #    for j in range(assigns):
        #        task = tasks.get()
        #        self.assignments[i].append(task)
        # print("assignments = " + str(self.assignments))

    def assignTask(self, task, game_model):
        """ more sophisticated task assigner for stand phase """
        task_assigned = False
        while task_assigned is not True:
            # 1. get best rated agent
            i = game_model.reputation.index(max(game_model.reputation))
            # 2. check if WA queue has room for current task
            # 2.1 get effort required for task
            task_effort = game_model.getEffortPerTask(task)
            # 2.2 get WA productivity
            agent_productivity = game_model.agentsProductivity[i]
            # 2.3 get WA queue
            agent_queue = [2, 11]
            # agent_queue = game_model.agentsBacklog
            # get free workpower
            for queued_task in agent_queue:
                agent_workload += game_model.getEffortPerTask(queued_task)
            # debug
            print("effort = " + str(task_effort))
            print("produc = " + str(agent_productivity))
            print("bqueue = " + str(agent_queue))
            task_assigned = True
        #   2.1 if true: assign task to worker
        #   2.2 else: proceed to 1 with next agent
        
        
        pass
