#Temporary user interface
import json
from pprint import pprint
from datetime import datetime

rawStart = input("Please enter a start time: ")
timeStart = datetime.strptime(rawStart, '%I:%M%p')
# rawEnd = input("Please enter an end time: ")
# timeEnd = datetime.strptime(rawEnd, "%I:%M%p")


#print(timeStart)
# print(timeEnd)
data = json.load(open("data.json"))

for i in data:
    if i["startTime"] != "TBA":
        startTime = datetime.strptime(i["startTime"], "%I:%M %p")
        if startTime == timeStart:
            print(i)