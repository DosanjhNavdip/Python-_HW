import time

def timestamp(func):
    print(time.ctime())
    func()
