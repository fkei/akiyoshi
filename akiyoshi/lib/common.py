import time
import datetime
import string
import random
import tempfile

def mktmp():
    return tempfile.mkstemp()

def epochsec2strftime(epochsec, format):
    """epochsec -> strftime(format) convert.
    """
    #time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(int(time.mktime(datetime.datetime.now().timetuple()))))
    ret = time.strftime(format, time.localtime(epochsec))
    return ret

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

def create_epochsec_datetime(_datetime):
    return create_epochsec(_datetime.year,_datetime.month,_datetime.day,_datetime.hour,_datetime.minute,_datetime.second)

def now_epochsec():
    return create_epochsec_datetime(datetime.datetime.now())

def past_epochsec(pastday):
    """Day inversely
    """
    return create_epochsec_datetime(datetime.datetime.now() - datetime.timedelta(pastday))

#--

def pastany_epochsec(day):
    """any
    """
    now = datetime.datetime.now()
    prev = create_epochsec_datetime(now - datetime.timedelta(day))
    return prev, create_epochsec_datetime(now)


def past1hour_epochsec():
    """-1hour
    """
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(hours=1)
    now_epochsec = create_epochsec_datetime(now)
    yesterday_epochsec = create_epochsec_datetime(yesterday)
    return yesterday_epochsec, now_epochsec

def past12hour_epochsec():
    """-12hour
    """
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(hours=12)
    now_epochsec = create_epochsec_datetime(now)
    yesterday_epochsec = create_epochsec_datetime(yesterday)
    return yesterday_epochsec, now_epochsec


def past1_epochsec():
    """-1day
    """
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(1)
    now_epochsec = create_epochsec_datetime(now)
    yesterday_epochsec = create_epochsec_datetime(yesterday)
    return yesterday_epochsec, now_epochsec

def past7_epochsec():
    """-7 day
    """
    now = datetime.datetime.now()
    prev = create_epochsec_datetime(now - datetime.timedelta(7))
    return prev, create_epochsec_datetime(now)

def past30_epochsec():
    """-30 day
    """
    now = datetime.datetime.now()
    prev = create_epochsec_datetime(now - datetime.timedelta(30))
    return prev, create_epochsec_datetime(now)

def past365_epochsec():
    """-365 day
    """
    now = datetime.datetime.now()
    prev = create_epochsec_datetime(now - datetime.timedelta(365))
    return prev, create_epochsec_datetime(now)

#--
def generate_phrase(len, letters=None):
    if letters is None:
        letters = string.digits + string.letters + '-.'
    random.seed()
    return ''.join(random.choice(letters) for i in xrange(len))

if __name__ == '__main__':
    #print now_epochsec()
    print past1_epochsec()
    print "--"
    print past7_epochsec()
    print "--"
    print past30_epochsec()
    print "--"
    print past365_epochsec()
    print "--"

