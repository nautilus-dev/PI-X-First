# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:34:36 2017

"""

import numpy as np
from data_import import dataManager


class gameModel :

    dM
    agents = np.array 
    reputation = np.array
    currentAsssignment = np.array
    round = -1


    # TODO :
    # Reputation calculation
    # calculate probability whether task is succ. based on assignment
    # calculate 


    def getWorkerReputation (self) :
        """
        gives back the reputation.
        """
        return self.reputation


    def __init__ (self, numAgents, numRounds) :
        print ("gameModel initialized")
        # make a 2D Array with the WorkerAgents in the columns and the rounds
        # as the rows , initialize all with zero.
        self.agents = np.zeros((numRounds, numAgents), dtype = np.float)
        self.repuation = np.zeros((numAgents), dtype = np.float)
        self.reputation = [0.5 for i in xrange(numAgents)]
        self.currentAssignment = np.zeros((numAgents), dtype = np.int)
        self.round = -1
        self.dM = dataManager()
    
    def importData (self) :
        
        print ("not yet implemented")
        
    
    def caclulcateReputation (self, successfulNessByWA, loadbyWA) :
        # for each WA: use the load (normalized by the amount of total tasks)
        # and the whether it was successful with all tasks,
        # 1.0 reputation would be all tasks of a round got
        # and been able to work on all.
        print ("not implemented yet!")
       
    def executeGame(self, assignments) :
        """
        Does all the game playing based oon the assignments
        """        
        print ("not implemented yet!")
       