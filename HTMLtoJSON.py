#Processes HTML into Course objects in JSON, data.json


from bs4 import BeautifulSoup
import json
from course import Course



#Soup scrape elements from HTML page
soup = BeautifulSoup(open("raw.html", encoding="utf8"), "html.parser")

courseNumber = soup.select(".class-schedule-course-number")
courseTitle = soup.select(".class-schedule-course-title")
courseData = soup.select(".class-schedule-label")


#Add data to each course and add to list of courses
courses = []

for i in range(len(courseTitle)):
    courses.append(Course(courseNumber[i].getText(), courseTitle[i].getText(), courseData[i * 5].getText(),
                          courseData[i * 5 + 1].getText(), courseData[i * 5 + 2].getText(),
                          courseData[i * 5 + 3].getText(), courseData[i * 5 + 4].getText()))

# for i in courses:
#     print(i.dump())

#Dump all courses into json file
file = open("data.json", "w")
json.dump([o.dump() for o in courses],file)
file.close()


