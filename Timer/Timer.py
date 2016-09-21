#This is a program to track start and end times
#!/usr/bin/python

import os
import sys
import datetime

#print 'Number of arguments:', len(sys.argv), 'arguments.'
action = str(sys.argv[1])
now = datetime.datetime.now()
today_date = now.date()
year = today_date.year
month = today_date.month
day = today_date.day
current_time = now.time()

def writeTimeToFile(time):
	return True;

def timerLog(action, time):
	if(action == "start"):
		print "Started Timer at: " + str(time)
	elif(action == "stop"):
		print "Stopped Timer at: " + str(time)
	else:
		print "Unknown command"

timerLog(action, current_time)
