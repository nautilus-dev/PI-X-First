# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:00:46 2017

@author: nautilus
"""

import sqlite3
import pandas

con = sqlite3.connect(":memory:")

df = pandas.read_csv("./data/Users.csv")
df.to_sql("Users", con, if_exists='replace', index=True)

df = pandas.read_csv("./data/Tasks.csv")
df.to_sql("Tasks", con, if_exists='replace', index=True)

df = pandas.read_csv("./data/Worker_Agents.csv")
df.to_sql("WorkerAgents", con, if_exists='replace', index=True)

df = pandas.read_csv("./data/Game_Sessions.csv")
df.to_sql("GameSessions", con, if_exists='replace', index=True)

con.commit()




print("trying to retrieve tables...")
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())