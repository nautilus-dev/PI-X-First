# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:34:36 2017

"""

import numpy as np
import Queue
from data_import import dataManager


class gameModel :

    dM = dataManager()
    numAgents = 0
    agentsProductivity = np.array
    agentsBacklog = []
    reputation = np.array
    currentAsssignment = np.array
    round = 0
    numTasks = 20
    taskEffortUnits = np.array
    numSuccessfulEffort = np.array
    numFailedEffort = np.array



    # TODO :
    # Reputation calculation
    # calculate probability whether task is succ. based on assignment



    def getWorkerReputation (self) :
        """
        gives back the reputation.
        """
        return self.reputation


    def __init__ (self, numAgents, numRounds, numTasks = 20) :
        """
        Makes a Game Model and initializes it
        """
        # make a 2D Array with the WorkerAgents in the columns and the rounds
        # as the rows , initialize all with zero.
        self.numAgents = numAgents
        self.agentsProductivity = np.zeros((numAgents), dtype = np.int)
        self.repuation = np.zeros((numAgents), dtype = np.float)
        self.reputation = [0.5 for i in xrange(numAgents)]
        self.currentAssignment = np.zeros((numAgents), dtype = np.int)
        self.numSuccessfulEffort = np.zeros((numAgents), dtype = np.int)
        self.numFailedEffort = np.zeros((numAgents), dtype = np.int)
        self.taskEffortUnits = np.zeros((numTasks), dtype = np.int)
        self.round = 0
        self.numTasks = numTasks
        self.getTaskEffortUnits()
        self.getAgentsProductivity() 
        self.agentsBacklog = [0 for i in xrange(self.numAgents)]
        # constructing the backlog queue
        for i in range(0, self.numAgents) :
            q = Queue.Queue()
            self.agentsBacklog[i] = q

    def getTaskEffortUnits (self) :
        # TODO : rework that it samples from the database:
        # self.dM.getValuesAsPandasObject("SELECT * FROM Tasks")
        self.taskEffortUnits = [1 for i in xrange(self.numTasks)]
    
    def getAgentsProductivity (self) :
        # TODO : rework that it samples from the database:
        self.agentsProductivity = [(10 + i) for i in xrange(self.numAgents)]


    def caclulcateReputation (self, successfulNessByWA, loadbyWA) :
        # TODO:         
        # for each WA: use the load (normalized by the amount of total tasks)
        # and the whether it was successful with all tasks,
        # 1.0 reputation would be all tasks of a round got
        # and been able to work on all.
        pass

    def getEffortPerTask(self, task) :
        # TODO : get the effort from the database  
        print ("constant 1 effort")
        return 100

    def executeGame(self, assignments) :
        """
        Does all the game playing based oon the assignments
        """
        # TODO: calulculate whether the tasts are successfully finished
        
        # we have all the assignments ans the effort units, just do scalar substraction?
        
        # assignments is an list of lists of the tasks for each worker. 
        
        # TODO: ONLY FOR TESTING!!!!
        # for i in range(0, self.numAgents) :
        #    q = Queue.Queue()
        #    assignments[i] = q
        
        # for each worker 
            # load its backlog queue
            # fill this backlog queue with the new tasks
            # work in the backlog queue until the there is no more task fitting in the productivity
            # for each task number lookup the individual Task effort unit
        # start the new round (as 0 is the first round)
        self.round += 1

        for i in range(0, self.numAgents) :
            print ("current Round is: " , self.round)
            backlog = self.agentsBacklog[i]
            newTasks = assignments[i]
            waLeftCapacity = self.agentsProductivity[i]
            for b in range(0, len(newTasks)) :
                backlog.put(newTasks[b])
            print ("working assignments parsed")
            print ("backlog size is: " , backlog.qsize())
            print ("agent productivity is: " , waLeftCapacity)
            elem = -1
            while backlog.qsize() > 0 :
                elem = backlog.get()
                print ("Current Element " , elem)
                effort = self.getEffortPerTask(elem)
                if effort <= waLeftCapacity :
                    self.numSuccessfulEffort[i] += effort
                else :
                    break
            print ("working done")
            # now the failed elements and add them back to some queue
            # TODO: Rework here. looks super ugly
            leftTasks = Queue.Queue()
            leftTasks.put(elem)
            self.numFailedEffort += self.getEffortPerTask(elem)
            while (backlog.qsize() > 0) :
                elem = backlog.get()
                self.numFailedEffort += self.getEffortPerTask(elem)
                leftTasks.put(elem)
            # add back the tasks
            self.agentsBacklog[i] = leftTasks
            

        
