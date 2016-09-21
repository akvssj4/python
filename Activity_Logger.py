#!/usr/bin/python

import os
import sys
import datetime

#print 'Number of arguments:', len(sys.argv), 'arguments.'
log = str(sys.argv[1])
print 'Log:', log
now = datetime.datetime.now()
today_date = now.date()
year = today_date.year
month = today_date.month
day = today_date.day
#current_time = now.time()
dateTime_formatted = now.strftime("%A, %d. %B %Y %I:%M %p")
print 'Current Time:', dateTime_formatted

# Open a file
if not os.path.exists(str(today_date)):
    os.makedirs(str(today_date))
fo = open(str(today_date)+"/"+str(day)+".txt", "a")
fo.write( str(dateTime_formatted)+"\n"+log+"\n");

# Close opend file
fo.close()
