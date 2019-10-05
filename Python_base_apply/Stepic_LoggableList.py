import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(list, Loggable):
    def append(self, a):
        list.append(self, a)
        Loggable.log(self, a)
