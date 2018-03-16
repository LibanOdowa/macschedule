# Backend request processor

import json
from datetime import datetime


class Backend:
    def __init__(self, jsonfile):
        self.data = json.load(jsonfile)

    def result_formatter(self, results, i):
        return results.append(i["department"] + " " + i["number"] + "-" + i["section"] + ": " + i["title"] + " (" + i[
            "startTime"] + " - " + i["endTime"] + ")")

    def get_results(self, daylist, dept, startTime, endTime):
        days = ''.join(daylist)
        results = []
        if startTime == '':
            newStartTime = datetime.strptime("0:00", "%H:%M")
        else:
            newStartTime = datetime.strptime(startTime, "%H:%M")
        if endTime == '':
            newEndTime = datetime.strptime("23:59", "%H:%M")
        else:
            newEndTime = datetime.strptime(endTime, "%H:%M")
        print(newStartTime)
        print(endTime)
        for i in self.data:
            if i["startTime"] != "TBA" and i["endTime"] != "TBA":
                if datetime.strptime(i["startTime"], "%I:%M %p") >= newStartTime and datetime.strptime(i["endTime"],
                                                                                                       "%I:%M %p") <= newEndTime:
                    if days == "" and dept == "NONE":
                        self.result_formatter(results, i)
                    elif i["days"] in days and dept == "NONE":
                        self.result_formatter(results, i)
                    elif days == "" and dept != "NONE":
                        if i["department"] == dept:
                            self.result_formatter(results, i)
                    else:
                        if i["days"] in days and i["department"] == dept:
                            self.result_formatter(results, i)
        return results

#
# rawStart = input("Please enter a start time: ")
# timeStart = datetime.strptime(rawStart, '%I:%M%p')
# rawEnd = input("Please enter the end time: ")
# timeEnd = datetime.strptime(rawEnd, "%I:%M%p")
# rawDates = input("Please enter days you would like(MTWRF)")
#
# data = json.load(open("data.json"))
#
#
# #Checks if between times and if on days selected, then returns entry
# for i in data:
#     if i["startTime"] != "TBA":
#         startTime = datetime.strptime(i["startTime"], "%I:%M %p")
#         endTime = datetime.strptime(i["endTime"], "%I:%M %p")
#         if startTime > timeStart and endTime < timeEnd and i["days"] in rawDates.upper():
#             print(i) #TODO: Figure out proper output, currently returns whole dict entry
