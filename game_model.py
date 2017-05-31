# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:34:36 2017

"""

import numpy as np
import Queue
import random
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
        self.getAgentsProductivity()
        self.agentsBacklog = [0 for i in xrange(self.numAgents)]
        # constructing the backlog queue
        for i in range(0, self.numAgents) :
            q = []
            self.agentsBacklog[i] = q

    def getAgentsProductivity (self) :
        # Deprecated ascending linear productivity
        # self.agentsProductivity = [(10 + i) for i in xrange(self.numAgents)]
        
        query = "SELECT \"Max Productivity (No. of Effort Units per Round)\"" + "FROM WorkerAgents WHERE ID <= 10 ORDER BY ID ASC;"
        productivity = self.dM.getValuesAsPandasObject(query)
        for wa in range(0, self.numAgents) :
            self.agentsProductivity[wa] = productivity.values[wa][0]
                


    def caclulcateReputation (self) :
        # for each worker calculate
        # ( (((((#succ - #failed)/(#succ + #failed))+1)/2)*(10-round)) + 
        # (prevRep * round )) / 10
    
        for wa in range(0, self.numAgents) :
            previousReputation = self.reputation[wa]
            successfulTasks = self.numSuccessfulEffort[wa]
            failedTasks = self.numFailedEffort[wa]
            numRounds = self.round

            left = ((((successfulTasks - failedTasks) / (successfulTasks + failedTasks)) + 1) / 2 ) * (10 - numRounds)
            right = (previousReputation * numRounds)
            newRep = (left + right) / 10

            self.reputation[wa] = abs(newRep)
            print ("reputation for this guy is ", newRep)

    def getTasks(self) :
        """ returns open tasks for current round as queue """
        # TODO: rewort that  sample from database
        tasks = Queue.Queue()
        for i in range(self.numTasks):
            tasks.put(random.randint(1,30))
        return tasks

    def getEffortPerTask(self, task) :
        query = "SELECT \"Effort Required\" FROM Tasks WHERE \"ID\"=%d" % task
        value = self.dM.getValuesAsPandasObject(query)
        return value.values[0][0]

    def getTaskDifficulty(self, task) :
        return 1
    
    def getAgentCapability(self, agent) :
        return 1
    
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
            # print ("current Round is: " , self.round)
            # print("Previous Backlog length is: " , self.agentsBacklog[i].qsize())            
            backlog = self.agentsBacklog[i]
            newTasks = assignments[i]
            waLeftCapacity = self.agentsProductivity[i]
            # print("Worker Capacity is: " , waLeftCapacity)            
            for b in range(0, len(newTasks)) :
                backlog.append(newTasks[b])
            #print ("working assignments parsed")
            #print ("backlog size is: " , backlog.qsize())
            #print ("agent productivity is: " , waLeftCapacity)
            elem = -1
            # Never fall back into the working mode, when failing once
            Work = True
            leftTasks = []
            # print("backlog Size", backlog.qsize())
            while len(backlog) > 0 :
                elem = backlog[0]
                del backlog[0]
                #print ("Current Element " , elem)
                effort = self.getEffortPerTask(elem)
                # print ("Current Element Effort", effort)
                # print ("Left Capacity", waLeftCapacity)
                Workable = True if self.getAgentCapability(i) >= self.getTaskDifficulty(elem) else False
                if effort <= waLeftCapacity and Workable and Work:                    
                    self.numSuccessfulEffort[i] += effort
                    waLeftCapacity -= effort
                else :
                    Work = False
                    self.numFailedEffort += self.getEffortPerTask(elem)
                    leftTasks.append(elem)
 
            # add back the tasks
            self.agentsBacklog[i] = leftTasks
            # print("New BacklogQueue length is: " , self.agentsBacklog[i].qsize())
            # print("Successfull Effort" , self.numSuccessfulEffort[i])
            # print("Queued Effort", self.numFailedEffort[i])
        
        self.caclulcateReputation()
       

