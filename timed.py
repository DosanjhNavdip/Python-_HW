import time

def timeme(func):
    t1 = time.time()
    func()
    t2 = time.time() 
    timeForrun = t2 - t1
    print(timeForrun)
