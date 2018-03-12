from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("raw.html", encoding="utf8"), "html.parser")


courseTitle = soup.find_all("td", {"class": "class-schedule-course-title"})
courseNumber = soup.select(".class-schedule-course-number")

file = open("data.json", "w")
data = []
for i in range(len(courseTitle) - 1):
    title = courseTitle[i].getText()
    number = courseNumber[i].getText()
    data.append({
        "title": title,
        "number": number
    })
json.dump(data,file)
file.close()
