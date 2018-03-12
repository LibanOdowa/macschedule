from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("raw.html", encoding="utf8"), "html.parser")

courseNumber = soup.select(".class-schedule-course-number")
courseTitle = soup.select(".class-schedule-course-title")
courseData = soup.select(".class-schedule-label")


file = open("data.json", "w")
data = []

#Dirty data right now, not formatted well times/dates/classes
for i in range(len(courseTitle)):
    number = courseNumber[i].getText()
    title = courseTitle[i].getText()
    days = courseData[i*5].getText()
    time = courseData[i*5+1].getText()
    room = courseData[i*5+2].getText()
    instructor = courseData[i*5+3].getText()
    enrollment = courseData[i*5+4].getText()
    data.append({
        "number": number,
        "title": title,
        "days": days,
        "time": time,
        "room": room,
        "instructor": instructor,
        "enrollment": enrollment
    })
json.dump(data,file)
file.close()
