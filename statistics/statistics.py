#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:04:52 2017

@author: daniel
"""

import numpy as np
#decisions = np.genfromtxt ('Decisions.csv', delimiter=";", dtype=None);
dims = np.shape(decisions);

#meanvalues = np.array("<0,1","0,1-0,2","0,2-0,3","0,3-0,4","0,4-0,5","0,5-0,6","0,6-0,7","0,7-0,8","0,8-0,9","0,9-1");
mean_array = np.zeros([10,3]);

for x in range(1, dims[0]):
   if (float(decisions[x,6].replace(',','.'))>=0.9):
       mean_array[9,0] += float(decisions[x,4]);
       mean_array[9,1] += float(decisions[x,5]);
       mean_array[9,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.8):
       mean_array[8,0] += float(decisions[x,4]);
       mean_array[8,1] += float(decisions[x,5]);
       mean_array[8,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.7):
       mean_array[7,0] += float(decisions[x,4]);
       mean_array[7,1] += float(decisions[x,5]);
       mean_array[7,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.6):
       mean_array[6,0] += float(decisions[x,4]);
       mean_array[6,1] += float(decisions[x,5]);
       mean_array[6,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.5):
       mean_array[5,0] += float(decisions[x,4]);
       mean_array[5,1] += float(decisions[x,5]);
       mean_array[5,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.4):
       mean_array[4,0] += float(decisions[x,4]);
       mean_array[4,1] += float(decisions[x,5]);
       mean_array[4,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.3):
       mean_array[3,0] += float(decisions[x,4]);
       mean_array[3,1] += float(decisions[x,5]);
       mean_array[3,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.2):
       mean_array[2,0] += float(decisions[x,4]);
       mean_array[2,1] += float(decisions[x,5]);
       mean_array[2,2] += 1;
   elif (float(decisions[x,6].replace(',','.'))>=0.1):
       mean_array[1,0] += float(decisions[x,4]);
       mean_array[1,1] += float(decisions[x,5]);
       mean_array[1,2] += 1;
   else:
       mean_array[0,0] += float(decisions[x,4]);
       mean_array[0,1] += float(decisions[x,5]);
       mean_array[0,2] += 1;

mean_tasks = mean_array[:,0]/mean_array[:,2];
mean_effort = mean_array[:,1]/mean_array[:,2]



mean_array_by_rounds = np.zeros([10,10,3]);
mean_tasks_by_rounds = np.zeros([10,10]);
mean_effort_by_rounds = np.zeros([10,10]);


for r in range(0,10):
    for x in range(1, dims[0]):
        if (float(decisions[x,2])==(r+1)):
           if (float(decisions[x,6].replace(',','.'))>=0.9):
               mean_array_by_rounds[r,9,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,9,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,9,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.8):
               mean_array_by_rounds[r,8,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,8,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,8,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.7):
               mean_array_by_rounds[r,7,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,7,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,7,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.6):
               mean_array_by_rounds[r,6,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,6,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,6,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.5):
               mean_array_by_rounds[r,5,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,5,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,5,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.4):
               mean_array_by_rounds[r,4,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,4,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,4,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.3):
               mean_array_by_rounds[r,3,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,3,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,3,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.2):
               mean_array_by_rounds[r,2,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,2,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,2,2] += 1;
           elif (float(decisions[x,6].replace(',','.'))>=0.1):
               mean_array_by_rounds[r,1,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,1,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,1,2] += 1;
           else:
               mean_array_by_rounds[r,0,0] += float(decisions[x,4]);
               mean_array_by_rounds[r,0,1] += float(decisions[x,5]);
               mean_array_by_rounds[r,0,2] += 1;

    mean_tasks_by_rounds[r,:] = mean_array_by_rounds[r,:,0]/mean_array_by_rounds[r,:,2];
    mean_effort_by_rounds[r,:] = mean_array_by_rounds[r,:,1]/mean_array_by_rounds[r,:,2]