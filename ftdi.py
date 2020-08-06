import sys,time,  ftd2xx as ftd
print(ftd.listDevices())
e = None
d = ftd.open(0)    # Open first FTDI device
print(d.getDeviceInfo())
d.setBaudRate(9600)
d.setDataCharacteristics(8,0,0)
d.setFlowControl(0x0000)
i = [0 | 0x10] * 100
# read_event = ftd.FTD2XX.setEventNotification(d,i[0],e)

def ft_read(d, nbytes):
    s = d.read(nbytes)
    print(s)
    return [ord(c) for c in s] if type(s) is str else list(s)

# print(ftd.FTD2XX.read(d, 0))
try:
    while True:
        # read_event = ftd.FTD2XX.setEventNotification(d,i[0],e)
        time.sleep(0.5)
        #print(ftd.FTD2XX.getQueueStatus(d))
        a = ft_read(d, 1)
        print(a)
        #print(a.decode('utf16'))
        print(ftd.FTD2XX.getStatus(d))
        print(ftd.FTD2XX.getEventStatus(d))
except KeyboardInterrupt:

    d = ftd.FTD2XX.close(d)