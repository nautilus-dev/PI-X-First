# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:00:46 2017

"""

import sqlite3
import pandas

class dataManager : 
    def __init__ (self) :
        self.con = sqlite3.connect(":memory:")
        self.cursor = self.con.cursor()



    def readInCSV(self) :
        df_Users = pandas.read_excel("./source_datafiles/Users.xlsx")
        df_Users.to_sql("Users", self.con, if_exists='replace', index=True)
        
        df_Tasks = pandas.read_excel("./source_datafiles/Tasks.xlsx")
        df_Tasks.to_sql("Tasks", self.con, if_exists='replace', index=True)
    
        df_WorkerAgents = pandas.read_excel("./source_datafiles/Worker_Agents.xlsx")
        df_WorkerAgents.to_sql("WorkerAgents", self.con, if_exists='replace',
                               index=True)
    
        df_GameSessions = pandas.read_excel("./source_datafiles/Game_Sessions.xlsx")
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

