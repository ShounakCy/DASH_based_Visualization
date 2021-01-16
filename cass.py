from __future__ import division
from cassandra.cluster import Cluster
from matplotlib import pyplot
import datetime
import pandas as pd
import csv
from random import *
import time

cluster  = Cluster()
keyspace = "temperaturekey"
session  = cluster.connect(keyspace)

part=5000
toollife=50000
while(1):
  try:         
         date1 = datetime.datetime.now()
         temperature = randint(20,40)
         humidity = randint(30,40)
         pressure = randint(40,50)
         machine = randint(1,2)
         
         expectedpartcount = int(8800)
         performance = round((part/expectedpartcount)*100,2)
         part=part+1
         toollife=toollife-1
         
         time.sleep(2)

         
#preparing and executing my INSERT statement
         strCQL = "INSERT INTO temperaturetable1 (date1,temperature,humidity,pressure,machine,expectedpartcount,performance,part,toollife) VALUES (?,?,?,?,?,?,?,?,?)"
         pStatement = session.prepare(strCQL)
         session.execute(pStatement,[date1,temperature,humidity,pressure,machine,expectedpartcount,performance,part,toollife])
  except KeyboardInterrupt:
        print '\nPausing...  (Hit ENTER to continue, type quit to exit.)'
        try:
            response = raw_input()
            if response == 'quit':
                break
            print 'Resuming...'
        except KeyboardInterrupt:
            print 'Resuming...'
            continue


