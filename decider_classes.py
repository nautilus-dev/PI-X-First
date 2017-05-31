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
            #for i in range(tasks)):
                self.assignments[wa].append(tasks.pop())
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
        while len(tasks) > 0:
            # iterate through tasks and assign them
            current_task = tasks.pop()
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
            # get best rated agent
            i = 0
            agents = {}
            # create list of tupels with (old_pos, reputation)
            # TODO ~~ List ~~
            # check if WA queue has room for current task
            #  - get effort required for task
            task_effort = game_model.getEffortPerTask(task)
            #  - get WA productivity
            agent_productivity = game_model.agentsProductivity[i]
            #  - get WA queue
            agent_queue = game_model.agentsBacklog[i]
            #  - get free workpower
            agent_workload = 0
            for queued_task in agent_queue:
                agent_workload += game_model.getEffortPerTask(queued_task)
            ########################################
            # debug
            print("iagent = " + str(i))
            print("effort = " + str(task_effort))
            print("produc = " + str(agent_productivity))
            print("bqueue = " + str(agent_queue))
            print("workld = " + str(agent_workload))
            ########################################
            #  - check if enough workload is free
            if agent_productivity >= agent_workload + task_effort:
            #  - if free workload: assign task to worker
                # self.assignments[i].append(task)
                pass
            task_assigned = True
            # TODO: proceed to next agent
            print("-"*80)
