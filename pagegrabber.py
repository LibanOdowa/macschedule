# Pulls class schedule from website and saves to raw.html

import requests

res = requests.get('https://www.macalester.edu/registrar/schedules/2018spring/class-schedule/')
res.raise_for_status()
outputFile = open('raw.html', 'wb')
for chunk in res.iter_content(100000):
    outputFile.write(chunk)
outputFile.close()
