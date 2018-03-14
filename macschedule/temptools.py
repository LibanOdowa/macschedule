# import json
#
# data = json.load(open('data.json'))
#
# d = set()
#
# for i in data:
#     d.add(i["department"])
#
# for i in sorted(d):
#     print("<option value=\"" + i + "\">" + i + "</option>")
import datetime

export = datetime.datetime.strftime(datetime.datetime.strptime("18:04", "%H:%M"), "%I:%M %p")

print(export)
