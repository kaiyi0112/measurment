import com_info, serialtest, threading, serial
import datetime, configparser, re, time,queue
from queue import Queue
import multiprocessing as mp
def toolqueue(comnumber) :
    q_2=Queue()
    t_2=mp.Process(target=serial_test,args=(q_2,comnumber))
    t_2.start()
    print(q_2.get())
    print("q_2")
    t_2.join()
def number ():
    pass
def serial_test(q_2,comnumber):
    COM_PORT =("COM%s"%comnumber)   # 指定通訊埠名稱
    BAUD_RATES = 57600  # 設定傳輸速率
    BYTE_SIZE = 8
    PARITY = 'N'
    STOP_BITS = 1
    ser = serial.Serial(COM_PORT, BAUD_RATES, BYTE_SIZE, PARITY, STOP_BITS, timeout=None)
    string_slice_start = 8
    string_slice_period = 12
    try:
        while True:
            while ser.in_waiting:  # 若收到序列資料…
                data_raw = ser.read_until(b'\r')
                data = data_raw.decode()  # 用預設的UTF-8解碼
                equipment_ID = data[:string_slice_start - 1]
                altered_string = data[string_slice_start:string_slice_start + string_slice_period - 1]
                altered_int = float(altered_string)
                print('接收到的原始資料：', data_raw)
                print('接收到的資料：', data)
                print('Measurement Data From : ', equipment_ID)
                print('Altered Data : ', altered_string)
                print('Altered Float : ', altered_int)
                q_2.put(altered_int)
                ser.close()
                break
    except:pass
if __name__ == '__main__':
 toolqueue(4)