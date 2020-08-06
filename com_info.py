import serial.tools.list_ports
import re
def com ():
    #port_list = list(serial.tools.list_ports.comports())
    #port_list_1 = []
    #if len(port_list) == 0:
        pass
    #else:
        #for port in serial.tools.list_ports.comports():
           # print(port)
            #port_list_1.append(str(port))
    #try:
        #for i in range(10):
            #tool_com = ("COM%s - Mitutoyo U-WAVE (COM%s)" % (i, i))
            #if tool_com in port_list_1:
               # print("tool_com_name ok")
                #break
    #xcept:
        #pass
   # A = re.findall(r"\d", tool_com)
  #  return ("COM%s - Mitutoyo U-WAVE (COM%s)" % (i, i))
def com2 ():
    port_list = list(serial.tools.list_ports.comports())
    port_list_1 = []
    if len(port_list) == 0:
        pass
    else:
        for port in serial.tools.list_ports.comports():
            print(port)
            port_list_1.append(str(port))
    print("可用連接COM%s"%port_list_1)
    return port_list_1

