# import pandas as pd
import json

with open('Employment_Status.json') as json_file:
    data = json.load(json_file)
    print data[1]

import os
import json
import pandas as pd

#Read one or many files into a pandas dataframe
class DataFrameBuilder(object):
   def __init__(self):
       self.data_frame = None
       self._data_list = []
   def read_to_pandas(self, path):
       with open(path) as data_file:
           if (path.endswith(".csv")):
               data = pd.read_csv(data_file)
           elif path.endswith(".json"):
               data = pd.read_json(data_file)
           else:
               raise ValueError("No parser exists for parsing %s" + path)
           self._data_list.append(data)
       self.data_frame = pd.concat(self._data_list)

#List all the files available in the selected immuta data source
def list_files(data_frame_builder, startpath):
   for root, dirs, files in os.walk(startpath):
       for file in files:
           print file
           path = os.path.join(root, file)
           #print path
           #optionally build the pandas dataframe from the files
           #data_frame_builder.read_to_pandas(path)
startpath = '~\Desktop'
dfb = DataFrameBuilder()
list_files(dfb, startpath)
dfb.read_to_pandas('Employment_Status.json')
vet = dfb.data_frame

import ast
vet['warrior_serve__event_old_value__c'][11]
vet['warrior_serve__event_new_value__c'].value_counts()
vet.columns

dictn = {u'Unemployed':0,u'Employed':1,u'Unable to Work':2,u'Retired':3,u'Full-Time Student':4,u'Disable':5}

#In[]
Old_stat = []; New_stat = []
for i in range(5406):
    emplnt_o = vet['warrior_serve__event_old_value__c'][i]
    if emplnt_o != u'':
        emplnt_n = vet['warrior_serve__event_new_value__c'][i]
        Old_stat.append(dictn[emplnt_o]) ; New_stat.append(dictn[emplnt_n])
vet['warrior_serve__event_old_value__c'][5405]
len(Old_stat)#.count(0)
len(New_stat)

from matplotlib import pyplot as mp;
stat = [Old_stat,New_stat]
[Old_stat[i] for i in New_stat if i==dictn[u'Unable to Work']]
import numpy as np
Old_stat.count(5)
66./387
Old_stat.count()
N = 6
fig, ax = mp.subplots()
