import csv
import datetime
from dateutil.relativedelta import relativedelta
from time import sleep

Logs = []

#Valid log tags
#Order[Normal/Forced] - Related to drink orders (Normal vs forced order), after | show arduino message
#Mech - Related to the mechanical functionality
#Drinks[CREATE/EDIT] - Related to Drink modifications
#       [CREATE]     - {New object}
#       [DELETE]     - {Deleted Object}
#       [EDIT]       - {element_name=change|object (original)}
#Ingredients[CREATE/EDIT] - Related to ingredient library modifications
#       [CREATE]     - {New object}
#       [DELETE]     - {Deleted Object}
#       [EDIT]       - {element_name=change|object (original)}
#Stations - Related to station modifications
#Info - General information

class Log():
    time = None
    tag = None
    comment = None

    def __init__(self,tag,comment):
        self.time = datetime.datetime.now()
        self.tag = tag
        self.comment = comment

    def __str__(self):
        return self.time.strftime('%Y-%m-%d %H:%M:%S')+'|'+str(self.tag)+'|'+str(self.comment)

    def getTime(self):
        return self.time

    def setTime(self,time):
        self.time = time

    def getTag(self):
        return self.tag

    def getComment(self):
        return self.comment

#Create log entry
def log(tag,comment):
    log = Log(tag,comment)
    Logs.append(log)
    SaveLog(log)

#Write into log file
def SaveLog(log):

    to_write = log.getTime().strftime('%Y-%m-%d %H:%M:%S')+'|'+str(log.getTag())+'|'+str(log.getComment())+'\n'
    file = open('Logs.csv','a')
    file.write(to_write)
    file.close()

#Import logs
def ImportLogs():

    file = open('Logs.csv','r')
    for line in file:
        elements = line.split('|')
        #Create Log
        if(len(elements) == 3):
            log = Log(elements[1],elements[2])
            log.setTime(datetime.datetime.strptime(elements[0], '%Y-%m-%d %H:%M:%S'))
            Logs.append(log)

#Search logs by tag
def SearchLogTag(log_list,tag):
    list = []
    #If no log list was provided
    if(log_list is None):
        for log in Logs:
            if(log.getTag() == tag):
                list.append(log)
    else:
        for log in log_list:
            if(log.getTag() == tag):
                list.append(log)
    return list


#Search logs by time period
def SearchLogTime(log_list,start_time,period_in_days):
    list = []
    #If no log list was provided
    if(log_list is None):
        for log in Logs:
            if(log.getTime() >= start_time and log.getTime() <= log.getTime() + relativedelta(days=+period_in_days)):
                list.append(log)
    else:
        for log in log_list:
            if(log.getTime() >= start_time and log.getTime() <= log.getTime() + relativedelta(days=+period_in_days)):
                list.append(log)
    return list