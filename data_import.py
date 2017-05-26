# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:00:46 2017

"""

import sqlite3
import pandas

class dataManager : 
    def __init__ (self) :
        #self.con = sqlite3.connect(":memory:")
        self.con = sqlite3.connect('source_datafiles/source_database')
        self.cursor = self.con.cursor()

        if self.checkDBisEmpty() :
            print("Database seems empty/not existing, doing the import")
            self.readInXLSX()
        else : 
            print("Database is not empty, seems to be all there")
            
            

    def checkDBisEmpty(self) :
        tables = self.runCheck()
        return (tables.empty)
        

    def readInXLSX(self) :

        df_Users = pandas.read_excel("./source_datafiles/Users.xlsx")
        df_Users.to_sql("Users", self.con, if_exists='fail', index=True)
        
        df_Tasks = pandas.read_excel("./source_datafiles/Tasks.xlsx")
        df_Tasks.to_sql("Tasks", self.con, if_exists='fail', index=True)
    
        df_WorkerAgents = pandas.read_excel("./source_datafiles/Worker_Agents.xlsx")
        df_WorkerAgents.to_sql("WorkerAgents", self.con, if_exists='fail',
                               index=True)
    
        df_GameSessions = pandas.read_excel("./source_datafiles/Game_Sessions.xlsx")
        df_GameSessions.to_sql("GameSessions", self.con, if_exists='fail',
                               index=True)
    
        df_GameLevels = pandas.read_excel("./source_datafiles/Game_Levels.xlsx")
        df_GameLevels.to_sql("GameLevels", self.con, if_exists='fail',
                               index=True)

        df_Decisions = pandas.read_excel("./source_datafiles/Decisions.xlsx")
        df_Decisions.to_sql("Decisions", self.con, if_exists='fail',
                               index=False)
        self.con.commit()


    def runCheck(self) :
        # print("trying to retrieve tables...")
        tables = self.getValuesAsPandasObject("SELECT name FROM sqlite_master "
                                + "WHERE type='table';")
        return tables
    
    def getValuesAsPandasObject(self, query) :
        return pandas.read_sql_query(query, self.con)
    
    def printValues(self, query) :
        data = self.getValuesAsPandasObject(query)
        print data.values

