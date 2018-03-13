from datetime import datetime

class Course:
    def __init__(self, number, title, days, time, room, instructor, enrollment):
        #TODO: Clean up data for usage

        self.department = number.split()[0]
        self.number = number.split()[1].split('-')[0]
        self.section = number.split()[1][-2:]
        self.title = title
        self.days = days.split()[1]
        if "TBA" in time:
            self.startTime = "TBA"
            self.endTime = "TBA"
        else:
            # self.startTime = datetime.strptime(time[6:14],'%H:%M %p').strftime('%H:%M %p')
            # self.endTime = datetime.strptime(time[15:],'%H:%M %p').strftime('%H:%M %p')
            self.startTime = datetime.strptime(time[6:14],'%H:%M %p')
            self.endTime = datetime.strptime(time[15:],'%H:%M %p')
        self.room = ' '.join(room.split()[1:])
        self.instructor = ' '.join(instructor.split()[1:])


        #TODO: WORK ON ENROLLMENT FORMATTING "CLOSED" IS AN ISSUE
        # self.currentEnrollment = enrollment.split()[1]
        # if enrollment.split()[3] == '/':
        #     self.maxEnrollment = enrollment.split()[4]
        # else:
        #     self.maxEnrollment = enrollment.split()[3]


    def output(self):
        print(self.__dict__)

    #Dump to JSON to be implemented here
    def dump(self):
        pass
