#Course class

from datetime import datetime

class Course:
    def __init__(self, number, title, days, time, room, instructor, enrollment):
        self.department = number.split()[0]
        self.number = number.split()[1].split('-')[0]
        self.section = number.split()[1][-2:]
        self.title = title
        self.days = days.split()[1]
        if "TBA" in time:
            self.startTime = "TBA"
            self.endTime = "TBA"
        else:
            self.startTime = datetime.strptime(time[6:14],'%H:%M %p').strftime('%H:%M %p')
            self.endTime = datetime.strptime(time[15:],'%H:%M %p').strftime('%H:%M %p')
        self.instructor = ' '.join(instructor.split()[1:])
        if enrollment.split()[1] == "Closed":
            self.closed = True
            self.currentEnrollment = enrollment.split()[2]
            self.maxEnrollment = enrollment.split()[4]
        else:
            self.closed = False
            self.currentEnrollment = enrollment.split()[1]
            self.maxEnrollment = enrollment.split()[3]

    def dump(self):
        return self.__dict__