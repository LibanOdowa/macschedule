class Course:
    def __init__(self, number, title, days, time, room, instructor, enrollment):
        #Inputs dirty data, clean this up before dumping
        self.number = number
        self.title = title
        self.days = days
        self.time = time
        self.room = room
        self.instructor = instructor
        self.enrollment = enrollment

    def output(self):
        print(self.__dict__)

    #Dump to JSON to be implemented here
    def dump(self):
        pass
