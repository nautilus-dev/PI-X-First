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
    def __init__(self, pi=1, verbose=False) :
        # switch parameter. defaults to 1
        self.pi = pi
        self.verbose = verbose

    def decide(self, game_model) :
        """
        The switch: Use method according to current state
        """
        self.assignments = [[] for _ in range(game_model.numAgents)]
        if game_model.round < self.pi :
            if self.verbose:
                print("=" * 70)
                print("Using search phase")
                print("round = " + str(game_model.round) + "\t" +
                      "pi = " + str(self.pi))
            self.search(game_model)
        else :
            if self.verbose:
                print("=" * 70)
                print("Using stand phase")
                print("round = " + str(game_model.round) + "\t" +
                      "pi = " + str(self.pi))
            self.stand(game_model)

    def search(self, game_model) :
        """
        try to model peoples decisions in the search phase,
        e.g. distribute tasks equally or randomly
        """
        # TODO (optional) make distribution respect effort units instead of tasks
        #
        # assuming even distribution of tasks (not effort units)
        n = game_model.numAgents  # count workers (should be 10)
        m = game_model.numTasks
        avg_tasks = int(math.ceil(m/n))
        tasks = game_model.getTasks()
        for wa in range(n):
            for i in range(avg_tasks):
            #for i in range(tasks)):
                self.assignments[wa].append(tasks.pop())

    def stand(self, game_model) :
        """
        try to model people's decisions in the stand phase, e.g.
          - distribute tasks among N top-rated workers
          - fill top-rated ẀAs workload, then go to 2nd rated etc.
        """
        # TODO: remove prints in this function
        # TODO: (optional) fix double data numTasks
        #
        tasks = game_model.getTasks()
        tupel_list = []
        # create list of agents as tupels with (agent_id, reputation)
        for i in range(1, game_model.numAgents + 1):
            tupel_list.append((i, game_model.getWorkerReputation()[i - 1]))
        # sort list by reputation
        tupel_list.sort(key=lambda x: x[1], reverse=True)
        # print("sorted tupel list", tupel_list)
        i = 1
        while len(tasks) > 0:
            # iterate through tasks and assign them
            current_task = tasks.pop()
            if self.verbose:
                print("Task no. " + str(i) + "\tTask ID: " + str(current_task) + "\t" +
                      "Req. effort: " + str(game_model.getEffortPerTask(current_task)))
            self.assignTask(current_task, tupel_list, game_model)
            i += 1
        # print("Assignments: " + str(self.assignments))

    def assignTask(self, task, tupel_list, game_model):
        """ more sophisticated task assigner for stand phase """
        # TODO: Remove print statements in this function
        #
        task_assigned = False
        # prepare agent list
        i = 0
        # iterate over agents and assign task to best one that has free capacity
        while task_assigned is not True and i < game_model.numAgents:
            # get current agent id
            agent_id = tupel_list[i][0]
            # check if WA queue has room for current task
            #  - get effort required for task
            task_effort = game_model.getEffortPerTask(task)
            #  - get WA productivity
            # TODO: fix that this methods still requires the technical id
            #       which is 1 less than the agent_id
            agent_productivity = game_model.agentsProductivity[agent_id - 1]
            #  - get WA queue
            agent_queue = game_model.agentsBacklog[agent_id - 1]
            #  - get free workpower
            agent_workload = 0
            for queued_task in agent_queue:
                agent_workload += game_model.getEffortPerTask(queued_task)
            #  - include current assignments in wload calculation
            for current_queued_task in self.assignments[agent_id - 1]:
                agent_workload += game_model.getEffortPerTask(current_queued_task)
            ########################################
            # debug
            # print("agent_id   = " + str(agent_id) + "/" + str(game_model.numAgents))
            # print("reputation = " + str(tupel_list[i][1]))
            # print("prodctivty = " + str(agent_productivity))
            # print("bqueue     = " + str(agent_queue))
            # print("currenttsk = " + str(self.assignments[agent_id - 1]))
            # print("workload   = " + str(agent_workload))
            # print("-" * 25)
            # /debug
            ########################################
            #  - check if enough workload is free
            if agent_productivity >= agent_workload + task_effort:
            #  - if free workload: assign task to worker
                if self.verbose:
                    print("Assigning Task " + str(task) + " to agent " + str(agent_id))
                self.assignments[agent_id - 1].append(task)
                task_assigned = True
            i += 1
            # print("-"*80)
        if task_assigned is not True and self.verbose:
            print("Assignment of task " + str(task) + " failed")
