import time
import datetime

def create_epochsec(year, month, day, hour, minute, second):
    """ epochsec
    """
    print year
    print month
    print day
    print hour
    print minute
    print second
    
    return str(int(time.mktime(datetime.datetime(year, month, day, hour, minute, second).timetuple())))

def now_epochsec():
    now = datetime.datetime.now()
    return create_epochsec(now.year,
                           now.month,
                           now.day,
                           now.hour,
                           now.minute,
                           now.second)

def pastday_epochsec():
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(1)
    now_epochsec = create_epochsec(now.year,
                                   now.month,
                                   now.day,
                                   now.hour,
                                   now.minute,
                                   now.second)
    yesterday_epochsec = create_epochsec(yesterday.year,
                                         yesterday.month,
                                         yesterday.day,
                                         yesterday.hour,
                                         yesterday.minute,
                                         yesterday.second)
    return now_epochsec, yesterday_epochsec

    
if __name__ == '__main__':
    print now_epochsec()
    print pastday_epochsec()

