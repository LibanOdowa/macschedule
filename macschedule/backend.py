# Backend request processor

import json
from datetime import datetime


# TODO: Rework this so instead of reading from a file, creates a list of course objects and reads traits

class Backend:
    def __init__(self, jsonfile):
        self.data = json.load(jsonfile)

    def result_formatter(self, results, i, showClosed):
        if showClosed:
            if i["closed"]:
                return results.append(
                    i["department"] + " " + i["number"] + "-" + i["section"] + ": " + i["title"] + " (" + i[
                        "startTime"] + " - " + i["endTime"] + ") " + "[" + i["currentEnrollment"] + "/" + i[
                        "maxEnrollment"] + "] CLOSED")
            else:
                return results.append(
                    i["department"] + " " + i["number"] + "-" + i["section"] + ": " + i["title"] + " (" + i[
                        "startTime"] + " - " + i["endTime"] + ") " + "[" + i["currentEnrollment"] + "/" + i[
                        "maxEnrollment"] + "]")
        else:
            if not i["closed"]:
                return results.append(
                    i["department"] + " " + i["number"] + "-" + i["section"] + ": " + i["title"] + " (" + i[
                        "startTime"] + " - " + i["endTime"] + ") " + "[" + i["currentEnrollment"] + "/" + i[
                        "maxEnrollment"] + "]")

    def get_results(self, daylist, dept, startTime, endTime, closed):
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
        if closed == "T":
            closed = True
        else:
            closed = False
        for i in self.data:
            if i["startTime"] != "TBA" and i["endTime"] != "TBA":
                if datetime.strptime(i["startTime"], "%I:%M %p") >= newStartTime and datetime.strptime(i["endTime"],
                                                                                                       "%I:%M %p") <= newEndTime:
                    if days == "" and dept == "NONE":
                        self.result_formatter(results, i, closed)
                    elif i["days"] in days and dept == "NONE":
                        self.result_formatter(results, i, closed)
                    elif days == "" and dept != "NONE":
                        if i["department"] == dept:
                            self.result_formatter(results, i, closed)
                    else:
                        if i["days"] in days and i["department"] == dept:
                            self.result_formatter(results, i, closed)
        if results:
            return results
        else:
            return "NA"
