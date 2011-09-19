import time
import datetime
import string
import random
import tempfile

def mktmp():
    return tempfile.mkstemp()

def create_epochsec(year, month, day, hour, minute, second):
    """ epochsec
    """
    #print year
    #print month
    #print day
    #print hour
    #print minute
    #print second

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


def generate_phrase(len, letters=None):
    if letters is None:
        letters = string.digits + string.letters + '-.'
    random.seed()
    return ''.join(random.choice(letters) for i in xrange(len))

if __name__ == '__main__':
    print now_epochsec()
    print pastday_epochsec()

