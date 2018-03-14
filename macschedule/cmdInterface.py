# Backend request processor

import json


class Backend:
    def __init__(self, jsonfile):
        self.data = json.load(jsonfile)

    def get_results(self, daylist):
        days = ''.join(daylist)
        results = []
        for i in self.data:
            if i["days"] in days:
                results.append(i["department"] + " " + i["number"] + "-" + i["section"] + ": " + i["title"])
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
