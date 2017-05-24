# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:00:46 2017

@author: nautilus
"""

import sqlite3
import pandas

class dataManager : 
    def __init__ (self) :
        self.con = sqlite3.connect(":memory:")
        self.cursor = self.con.cursor()



    def readInCSV(self) :
        # TODO : rewrite this as from Excel?
        df_Users = pandas.read_csv("./data/Users.csv")
        df_Users.to_sql("Users", self.con, if_exists='replace', index=True)
        
        df_Tasks = pandas.read_csv("./data/Tasks.csv")
        df_Tasks.to_sql("Tasks", self.con, if_exists='replace', index=True)
    
        df_WorkerAgents = pandas.read_csv("./data/Worker_Agents.csv")
        df_WorkerAgents.to_sql("WorkerAgents", self.con, if_exists='replace',
                               index=True)
    
        df_GameSessions = pandas.read_csv("./data/Game_Sessions.csv")
        df_GameSessions.to_sql("GameSessions", self.con, if_exists='replace',
                               index=True)
    
        self.con.commit()


    def runCheck(self) :
        print("trying to retrieve tables...")
        self.cursor.execute("SELECT name FROM sqlite_master "
                                + "WHERE type='table';")
        # TODO : Add a check whether the tables are read in 
        #                        correctly instead of printing them
        print(self.cursor.fetchall())
    
    def getValuesAsPandasObject(self, query) :
        return pandas.read_sql_query(query, self.con)
    
    def printValues(self, query) :
        data = self.getValuesAsPandasObject(query)
        print data.values




dM = dataManager()
dM.readInCSV()
dM.runCheck()

dM.printValues("SELECT * FROM WorkerAgents LIMIT 20")
