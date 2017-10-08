def funcTime(hour,minute,second):
    import datetime
    now = datetime.datetime(1970,1,1,hour,minute,second)
    later = now + datetime.timedelta(minutes = 5, seconds = 30)
    laterStr = later.strftime("%H:%M:%S")
    return laterStr
