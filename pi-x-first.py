# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:32:48 2017

"""

from data_import import dataManager
from decider_classes import piDecider, Trial


def main() :
    # main goes here
    # dM = dataManager()

    # checking if there is a return:
    # dM.printValues("SELECT * FROM Users LIMIT 20")

    # Example of getting the reputation in Round 2 for each Worker
    # for USER ID: 00212664-6c71-4e24-b61d-c7776f7a7d99
    # and the Workers level

    # Example for generating dataset with algorithm using session id
    sid = "e7e52776-2750-4cde-a5da-093ccb8feaf9"
    # set the pi-switch parameter
    pi = 1

    pd = piDecider(pi)
    trial = Trial(sid)

    # iterate over days and return algorithm assignment for each day
    print(str("-"*80))
    print("Generating Assignments")
    print("SID=%s\tPI=%d" % (sid, pi))
    print(str("-"*80))
    for d in range(1, 6) :

        pd.decide(trial)
        print("Round: %d\t%s" % (d, pd.assignments))
        trial.new_day()

if __name__ == "__main__" :
    main()
