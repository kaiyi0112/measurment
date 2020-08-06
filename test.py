import threading
import queue
import time,serial

def read_kbd_input(inputQueue):
    com_name = ('COM4')
    print(com_name)
    COM_PORT = com_name  # 指定通訊埠名稱
    BAUD_RATES = 57600  # 設定傳輸速率
    BYTE_SIZE = 8
    PARITY = 'N'
    STOP_BITS = 1
    ser = serial.Serial(COM_PORT, BAUD_RATES, BYTE_SIZE, PARITY, STOP_BITS, timeout=None)  # 初始化序列通訊埠
    string_slice_start = 8
    string_slice_period = 12
    print('Ready for keyboard input:')
    while (True):
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
def tool():
    EXIT_COMMAND = "exit"
    inputQueue = queue.Queue()
    inputThread = threading.Thread(target=read_kbd_input, args=(inputQueue,), daemon=True)
    inputThread.start()
    while (True):
        if (inputQueue.qsize() > 0):
            input_str = inputQueue.get()
            print("input_str = {}".format(input_str))

            if (input_str == EXIT_COMMAND):
                print("Exiting serial terminal.")
                break
        time.sleep(0.01)
    print("End.")
tool()