import tkinter as tk
import tkinter.ttk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
import com_info,serialtest ,threading,serial,toolrest
import datetime, configparser,re,time,queue
from tkinter import messagebox,filedialog
from queue import Queue

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print('Current Directory is : ' + BASE_DIR)
# common tkinter settings
font = ('Arial', 10,)

class start_menus:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400+400+300")
        self.master.iconbitmap("D:\侯博允\實驗室\實驗室\measurment\lib\ico.ico")
        self.master.title('PDAL-{system_name}-{system_type}'.format(system_name='PDAL-RQCS', system_type='CLIENT'))
        self.canvas1 = tk.Canvas(self.master, width=500, height=80)
        self.canvas1.grid(row=0, column=0)
        # for the logo picture part in GUI
        img = Image.open(BASE_DIR+'\\lib\\mp-logo.png')
        img = img.resize((500, 137), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.canvas1.create_image(260, 50, image=img, anchor='center')
        self.canvas1.image = img
        self.title1 = tk.Label(self.master, text='無線量測品管暨雲端可視化系統-量測與品管端', font=('Arial', 17))
        self.title1.grid(row=1, column=0)
        self.title2 = tk.Label(self.master, text='Wireless Measure and quality ''Control System\nwith Cloud Visualization Integration-CLIENT',font=('Arial', 15))
        self.title2.grid(row=2, column=0)
        self.button1 = tk.Button(self.master, text='量測專案設定\nCreate New Measurement Project', width=30,command=self.program_creation)
        self.button1.grid(row=3, column=0, pady=3)
        self.button2 = tk.Button(self.master, text='無線量具測試\nWireless measuring tool test', width=30,command=self.Wireless_measuring_tool_test)
        self.button2.grid(row=4, column=0, pady=3)
        self.button1 = tk.Button(self.master, text="開始量測\nStart measurement", command=self.start_Measure, width=30)
        self.button1.grid(row=5, column=0, pady=3)
        self.button1 = tk.Button(self.master, text='系統設定\nsystem setting', width=30)
        self.button1.grid(row=6, column=0, pady=3)
        self.button1 = tk.Button(self.master, text='離開系統\nExit System', width=30, command=self.exit)
        self.button1.grid(row=7, column=0, pady=3)

    def exit(self):
        print("離開")
        self.master.destroy()

    def program_creation(self):
        self.newwindow = tk.Toplevel(self.master)
        self.newwindow.resizable(0, 0)
        self.newwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.withdraw()
        self.app = Menus_1(self.newwindow)
        self.master.deiconify()

    def on_closing(self):
        self.newwindow.destroy()
        self.master.deiconify()
        return

    def Wireless_measuring_tool_test(self):
        self.newwindow = tk.Toplevel(self.master)
        self.newwindow.resizable(0, 0)
        self.newwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.withdraw()
        self.app = Menus_2(self.newwindow)
        self.master.deiconify()
    def start_Measure(self):
        self.newwindow=tk.Toplevel(self.master)
        self.app = Menu_4(self.master)

class Menus_1:
    def __init__(self,master):
        self.master=master
        self.master.geometry('220x520+300+200')
        self.master.iconbitmap("D:\侯博允\實驗室\實驗室\measurment\lib\ico.ico")
        #---------------------------------------
        self.master.title("量測專案設定")
        self.Lframe1 = tk.LabelFrame(self.master,text='1.量測專案設定\nMeasurement project settings',font = ("Arial",10),width=200,height=160).grid(rowspan=4,row=1,column=1,sticky='we',padx=5,pady=5)
        self.title1 = tk.Label( self.master, text='專案名稱',font = ("Arial",10)).grid(row=2,column=1,sticky="s",padx=20)
        self.entryvar1=tk.StringVar()
        self.entry1 = tk.Entry(self.master, textvariable=self.entryvar1, text='None',font = ("Arial",10)).grid(row=3,column=1, sticky='we',padx=20 )
        self.button1 = tk.Button(self.master, text='專案設定\n Project settings',command=self.project_setting).grid(row=4, column=1, sticky='we',padx=20)
        #---------------------------------------
        self.Lframe1 = tk.LabelFrame(self.master, text='2.量測資料設定\nMeasurement data settings', font=("Arial", 10), width=200, height=100).grid(row=5,rowspan=2, column=1, padx=5, ipadx=5)
        self.button1 = tk.Button(self.master, text='量測資料設定\nMeasurement data settings', command=self.Measurement_name_setting).grid(row=6, column=1, sticky='we', padx=15, columnspan=2)
        #---------------------------------------
        self.Lframe1 = tk.LabelFrame(self.master, text='3.量測量具設定\nMeasuring tool setting', font=("Arial", 10), width=200, height=100).grid(row=8, rowspan=2, column=1, padx=5,ipadx=5)
        self.button1 = tk.Button(self.master, text='量測量具設定\nMeasuring tool setting', command=self.Measurement_name_setting).grid(row=9, column=1, sticky='we', padx=15,columnspan=2)
        #--------------------------------------
        self.Lframe1 = tk.LabelFrame(self.master, text='4.量測設定檢查\nMeasurement setting check',font=("Arial", 10), width=200, height=100).grid(row=10, rowspan=2, column=1, padx=5,ipadx=5)
        self.button1 = tk.Button(self.master, text='量測設定檢查\nMeasurement setting check', command=self.Measurement_name_setting).grid(row=11, column=1, sticky='we', padx=15,columnspan=2)
        # --------------------------------------
        self.texts1_1 = tk.Button(self.master, text='設定完成\ncomplete').grid(row=12, column=1,columnspan=2, sticky='w',padx=15,pady=5)
        self.nextpartbut_1=tk.Button(self.master,text="設定重置\nReset",command=self).grid(row=12, column=1,padx=15,pady=5)
        self.nextpartbut_2=tk.Button(self.master, text="離開\nexit", command=self.exit).grid(row=12, column=1, sticky='e',padx=25,pady=5)
        self.master.wait_window()
    def exit(self):
        print("離開")
        self.master.destroy()
    def Measurement_name_setting(self):
        return
    def project_setting(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Menue_3(self.newWindow)
class Menus_2:
    def __init__(self,master):
        self.allcom_name=str()
        self.comboboxtext  = com_info.com2()
        self.master = master
        self.toolturn=True
        self.toolcount=[]
        self.toolNumber_returned_names = []
        self.master.resizable(0, 0)
        self.master.iconbitmap("D:\侯博允\實驗室\實驗室\measurment\lib\ico.ico")
        self.master.title('量測設定檢查\nMeasurement setting check')
        self.Lframe1 = tk.LabelFrame(self.master, text='1.量具連線\nMeasuring Tool Connection', font=("Arial", 10),width=550, height=150).grid(row=1, rowspan=3, column=1,columnspan=3 ,padx=5,pady=5, ipadx=5)
        self.title=tk.Label(self.master,text="連接埠&裝置名稱\nCOM&Device name",font=("Arail",10)).grid(row=2,column=1 ,padx=5,pady=5,ipadx=5)
        self.combovar_1 = tk.StringVar()
        self.combox_1 = ttk.Combobox(self.master, values=self.comboboxtext, textvariable=self.combovar_1 ,state='readonly').grid(row=2, column=2, padx=5, pady=5, ipadx=5)
        self.title_4=tk.Label(self.master,text="連接埠&裝置名稱\nCOM&Device name",font=("Arail",10)).grid(row=3,column=1 ,padx=5,pady=5,ipadx=5)
        self.combovar_2= tk.StringVar()
        self.combox_2 = ttk.Combobox(self.master, values=[1,2,3,4],  state='readonly',textvariable=self.combovar_2)
        self.combox_2.grid(row=3, column=2, padx=5, pady=5, ipadx=5)
        self.button_3=tk.Button(self.master,text="量具連結\nMeasuring Tool Confirmation",font=("Arail",10) ,width = 20 ,command=lambda:[self.tool_connect(),self.thread_it()]).grid(row=2,column=3,pady=3,ipady=5)
        self.button_4 = tk.Button(self.master, text="量具重新連結\nMeasuring Tool Relink ", font=("Arail", 10), command=self.Tool_Relink ,width = 20).grid(row=3, column=3, pady=3, ipady=5)
        #-----------------------------------------------------------------------------------------------------------------------
        self.Lframe1 = tk.Label(self.master, text='2.量具測試\nMeasuring Tool Connection', font=("Arial", 10)).grid(row=4, column=1, padx=5,pady=5, ipadx=5,ipady=5)
        self.Title_2 = tk.Label(self.master, text="裝置名稱\nDevice name", font=("Arail", 10)).grid(row=5, column=1, padx=5, pady=5, ipadx=5,ipady=5)
        self.TextEntry = tk.StringVar()
        self.Entry_1 = tk.Entry(self.master, textvariable=self.TextEntry, font=("Arial", 10)).grid(row=5 , column=2, padx=5, pady=5, ipadx=5, ipady=5)
        self.Title_3= tk.Label(self.master, text="量測數值\nMeasurement Value", font=("Arail", 10)).grid(row=6 , column=1,padx=5, pady=5,ipadx=5, ipady=5)
        self.TextEtry = tk.StringVar()
        self.Entry_2 = tk.Entry(self.master, textvariable=self.TextEtry, font=("Arial", 10)).grid(row=6 , column=2,padx=5, pady=5, ipadx=5,ipady=5)
        #--------------------------------------------------------------------------------------
        self.Title_4 = tk.Label(self.master, text="裝置名稱\nDevice name", font=("Arail", 10))
        self.Title_4.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.Title_4.grid_forget()
        self.TextEntry_1 = tk.StringVar()
        self.Entry_3 = tk.Entry(self.master, textvariable=self.TextEntry_1, font=("Arial", 10))
        self.Entry_3.grid(row=7, column=2, padx=5, pady=5,ipadx=5, ipady=5)
        self.Entry_3.grid_forget()
        self.Title_5 = tk.Label(self.master, text="量測數值\nMeasurement Value", font=("Arail", 10))
        self.Title_5.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.Title_5.grid_forget()
        self.TextEtry_1 = tk.StringVar()
        self.Entry_4 = tk.Entry(self.master, textvariable=self.TextEtry_1, font=("Arial", 10))
        self.Entry_4.grid(row=8, column=2, padx=5,pady=5, ipadx=5,ipady=5)
        self.Entry_4.grid_forget()
        self.Title_6 = tk.Label(self.master, text="裝置名稱\nDevice name", font=("Arail", 10))
        self.Title_6.grid(row=9, column=1, padx=5,  pady=5, ipadx=5, ipady=5)
        self.Title_6.grid_forget()
        self.TextEntry_2 = tk.StringVar()
        self.Entry_5 = tk.Entry(self.master, textvariable=self.TextEntry_2, font=("Arial", 10))
        self.Entry_5.grid(row=9, column=2,  padx=5, pady=5,  ipadx=5, ipady=5)
        self.Entry_5.grid_forget()
        self.Title_7 = tk.Label(self.master, text="量測數值\nMeasurement Value", font=("Arail", 10))
        self.Title_7.grid(row=10, column=1,  padx=5, pady=5, ipadx=5, ipady=5)
        self.Title_7.grid_forget()
        self.TextEtry_3 = tk.StringVar()
        self.Entry_6 = tk.Entry(self.master, textvariable=self.TextEtry_3, font=("Arial", 10))
        self.Entry_6.grid(row=10, column=2,   padx=5, pady=5, ipadx=5, ipady=5)
        self.Entry_6.grid_forget()
        self.Title_8 = tk.Label(self.master, text="裝置名稱\nDevice name", font=("Arail", 10))
        self.Title_8.grid(row=11, column=1, padx=5,pady=5, ipadx=5,ipady=5)
        self.Title_8.grid_forget()
        self.TextEntry_4 = tk.StringVar()
        self.Entry_8 = tk.Entry(self.master, textvariable=self.TextEntry_4, font=("Arial", 10))
        self.Entry_8.grid(row=11, column=2,padx=5, pady=5,ipadx=5, ipady=5)
        self.Entry_8.grid_forget()
        self.Title_9 = tk.Label(self.master, text="量測數值\nMeasurement Value", font=("Arail", 10))
        self.Title_9.grid(row=12, column=1,padx=5, pady=5,ipadx=5, ipady=5)
        self.Title_9.grid_forget()
        self.TextEtry_5 = tk.StringVar()
        self.Entry_7 = tk.Entry(self.master, textvariable=self.TextEtry_5, font=("Arial", 10))
        self.Entry_7.grid(row=12, column=2,padx=5, pady=5,ipadx=5, ipady=5)
        self.Entry_7.grid_forget()

        # for i in range(1,tool_Quantity):
        #     self.title_2 = tk.Label(self.master, text="連接埠&裝置名稱\nCOM&Device name", font=("Arail", 10)).grid(row=6+i,column=1, padx=5,ipadx=5)
        #---------------------------------------------------------------------------------------------------------------------------
        self.button_5 = tk.Button(self.master, text="量具設定確認\nGage setting confirmation ", font=("Arail", 10),command=self.tool_OK ,width = 20).grid(row=5, column=3, pady=3, ipady=5)
        self.button_6 = tk.Button(self.master, text="離開重設量具\nExit reconnect ", font=("Arail", 10),command=self.exit ,width = 20).grid(row=6, column=3, pady=3, ipady=5)
        self.combox_2.bind('<<ComboboxSelected>>',self.combox_2_set)
        self.master.wait_window()
    def combox_2_set(self,event):
        print(self.combox_2.get())
        if int(self.combox_2.get()) == 1:
            self.Title_4.grid_forget()
            self.Entry_3.grid_forget()
            self.Title_5.grid_forget()
            self.Entry_4.grid_forget()
            self.Title_6.grid_forget()
            self.Entry_5.grid_forget()
            self.Title_7.grid_forget()
            self.Entry_6.grid_forget()
            self.Title_8.grid_forget()
            self.Entry_8.grid_forget()
            self.Title_9.grid_forget()
            self.Entry_7.grid_forget()
        elif int(self.combox_2.get()) == 2:
            self.Title_4.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_3.grid(row=7, column=2, padx=5, pady=5,ipadx=5, ipady=5)
            self.Title_5.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_4.grid(row=8, column=2, padx=5,pady=5, ipadx=5,ipady=5)
            self.Title_6.grid_forget()
            self.Entry_5.grid_forget()
            self.Title_7.grid_forget()
            self.Entry_6.grid_forget()
            self.Title_8.grid_forget()
            self.Entry_8.grid_forget()
            self.Title_9.grid_forget()
            self.Entry_7.grid_forget()
        elif int(self.combox_2.get())== 3:
            self.Title_4.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_3.grid(row=7, column=2, padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_5.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_4.grid(row=8, column=2, padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_6.grid(row=9, column=1,  padx=5, pady=5,  ipadx=5, ipady=5)
            self.Entry_5.grid(row=9, column=2,  padx=5, pady=5,  ipadx=5, ipady=5)
            self.Title_7.grid(row=10, column=1,  padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_6.grid(row=10, column=2,   padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_8.grid_forget()
            self.Entry_8.grid_forget()
            self.Title_9.grid_forget()
            self.Entry_7.grid_forget()
        elif int(self.combox_2.get()) == 4:
            self.Title_4.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_3.grid(row=7, column=2, padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_5.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_4.grid(row=8, column=2, padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_6.grid(row=9, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_5.grid(row=9, column=2, padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_7.grid(row=10, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_6.grid(row=10, column=2, padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_8.grid(row=11, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_8.grid(row=11, column=2, padx=5, pady=5, ipadx=5, ipady=5)
            self.Title_9.grid(row=12, column=1, padx=5, pady=5, ipadx=5, ipady=5)
            self.Entry_7.grid(row=12, column=2, padx=5, pady=5, ipadx=5, ipady=5)
    def Tool_Relink(self)  :
        self.combovar_1.set("")
        self.toolturn=False
        self.TextEntry.set("")
        self.TextEtry.set("")
        self.Title_4.grid_forget()
        self.Entry_3.grid_forget()
        self.Title_5.grid_forget()
        self.Entry_4.grid_forget()
        self.Title_6.grid_forget()
        self.Entry_5.grid_forget()
        self.Title_7.grid_forget()
        self.Entry_6.grid_forget()
        self.Title_8.grid_forget()
        self.Entry_8.grid_forget()
        self.Title_9.grid_forget()
        self.Entry_7.grid_forget()
        self.combox_2.set("")
    def nextpart(self)  :
        self.newWindows = tk.Toplevel(self.master)
        self.root = Menus_2(self.newWindows)
    def exit(self):
        print("離開")
        print("TOOL CONTECT TURN DOWN ")
        self.toolturn=False
        self.master.destroy()
    def tool_connect(self):
        self.tool = re.findall(r"\d", self.combovar_1.get())
        self.toolcount.append(self.tool)
        self.toolNumber_connections=[]
        self.toolNumber_connections.append(self.combox_2.get())
        if len(self.toolcount) >1:
            self.toolturn = False
            time.sleep(0.2)
        self.toolturn = True
        try:
            if self.tool == []:
                print("無選擇連接量具")
                tk.messagebox.showerror('無選擇量具', '請選擇連接量具\nPlease select a measuring tool', parent=self.master)
            if self.toolNumber_connections == ['']:
                print("無選擇量具數量")
                tk.messagebox.showerror('無選擇量具數量', '請選擇量具數量 \nPlease select the number of measuring tools ',
                                        parent=self.master)
            else:
                print("連接COM%s" % self.tool[0])
        except:pass
    def tool_OK(self):
        print("量具連接確認")
        self.toolturn=False
        self.master.destroy()
    def thread_it(self):
        self.tool=re.findall(r"\d",self.combovar_1.get())
        if self.tool == []:
            pass
        else:
            t_1 = threading.Thread(target=self.toolqueue, args=(self.tool[0],))
            t_1.start()
    def toolqueue(self,comnumber):
        while True:
            self.q_2 = Queue()
            t_2 = threading.Thread(target=self.serial_test, args=(self.q_2, comnumber))
            t_2.start()
            t_2.join()
            t_3 = threading.Thread(target=self.insert, args=(self.q_2.get(),))
            t_3.start()
            t_3.join()
    def insert (self,Return_number_id):
        lock = threading.Lock()
        lock.acquire()
        lock.release()
        print("q_2,q_3線程結束回傳%s"%Return_number_id)
        if Return_number_id[1]  in self.toolNumber_returned_names:
            pass
        else:
            self.toolNumber_returned_names.append( Return_number_id[1])
            print(self.toolNumber_returned_names)
        if len(self.toolNumber_returned_names) > int(self.combox_2.get()):
            print("連接量具小於視窗數")
            tk.messagebox.showerror('連接量具小於視窗數', 'Non-selective connection ', parent=self.master)
        try:
            if self.toolNumber_returned_names[0] == Return_number_id[1]:
                self.TextEtry.set(Return_number_id[0])
                self.TextEntry.set(Return_number_id[1])
            elif self.toolNumber_returned_names[1] == Return_number_id[1]:
                self.TextEtry_1.set(Return_number_id[0])
                self.TextEntry_1.set(Return_number_id[1])
            elif self.toolNumber_returned_names[2] == Return_number_id[1]:
                pass
            elif self.toolNumber_returned_names[3] == Return_number_id[1]:
                pass
        except:pass
    def serial_test(self,q_2, comnumber):
        lock = threading.Lock()
        lock.acquire()
        COM_PORT = ("COM%s" % comnumber)  # 指定通訊埠名稱
        BAUD_RATES = 57600  # 設定傳輸速率
        BYTE_SIZE = 8
        PARITY = 'N'
        STOP_BITS = 1
        ser = serial.Serial(COM_PORT, BAUD_RATES, BYTE_SIZE, PARITY, STOP_BITS, timeout=None)
        string_slice_start = 8
        string_slice_period = 12
        try:
            while self.toolturn == True:
                while ser.in_waiting: # 若收到序列資料…
                        data_raw = ser.read_until(b'\r')
                        data = data_raw.decode()  # 用預設的UTF-8解碼
                        equipment_ID = data[:string_slice_start - 1]
                        altered_string = data[string_slice_start:string_slice_start + string_slice_period - 1]
                        altered_int = float(altered_string)
                        # print('接收到的原始資料：', data_raw)
                        # print('接收到的資料：', data)
                        # print('Measurement Data From : ', equipment_ID)
                        # print('Altered Data : ', altered_string)
                        # print('Altered Float : ', altered_int)
                        unit=list(data)
                        I=("I")
                        if unit[-2]==I:
                            altered_int=("%sin"%altered_int)
                        else:
                            altered_int=("%smm"%altered_int)
                        a=[]
                        a.append(altered_int)
                        a.append(equipment_ID)
                        q_2.put(a)
                        ser.close()
                        lock.release()
            else:
                ser.close()
        except:
            print("no")
class Menue_3:
    def __init__(self, master):
        self.master = master
        self.project_name=[]
        self.project_time=[]
        self.project_name.append("project")
        self.project_time.append("20205/27 24:44")
        self.master.title("專案設定 Project settings ")
        print(self.project_name[0])
        self.master.iconbitmap("D:\侯博允\實驗室\實驗室\measurment\lib\ico.ico")
        self.title_1 = tk.Label(self.master, text="量測專案名稱\n Measurement project name ", font=("Arail", 10)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.textEntry_1 = tk.StringVar()
        self.entry1 = tk.Entry(self.master, textvariable=self.textEntry_1,  font=("Arial", 10)).grid(row=1, column=1, padx=10, pady=10, sticky='w')
        # ---------------------------------------------------------
        self.tree = ttk.Treeview(self.master,show="headings")
        self.tree.grid(row=2 ,rowspan=4, columnspan=2, padx=10, pady=10)
        self.tree["column"]=("檔案名稱", "建立日期")
        self.tree.column("檔案名稱", width=150, anchor="center")
        self.tree.column("建立日期", width=150, anchor="center")
        self.tree.heading("檔案名稱",text="檔案名稱 File name")
        self.tree.heading("建立日期", text="建立日期 Creation date")
        for i in range(0,len(self.project_name)):
            self.tree.insert("", 0, values=(self.project_name[0], self.project_time[0]))
        #----------------------------------------------------------
        self.button_1 = tk.Button(self.master, text="建立新檔 \nCreate new file", font=("Arail", 10),height=3, width=15,command=self.Create_new_file).grid(row=1,column=3, padx=10, pady=10)
        self.button_2 = tk.Button(self.master, text="複製檔案\nCopy files ", font=('Arail', 10), height=3, width=15,command=self.Copy_files).grid( row=2, column=3, padx=10, pady=10)
        self.button_3 = tk.Button(self.master, text="刪除檔案\nDelete file", font=('Arail', 10), height=3, width=15,command=self.Delete_file).grid( row=3, column=3, padx=10, pady=10)
        self.button_4 = tk.Button(self.master, text="確認設置檔案\nConfirm settings file", font=('Arail', 10), height=3, width=15,command=self.Confirm_settings_file).grid( row=4, column=3, padx=10, pady=10)
        self.button_5 = tk.Button(self.master, text="離開重設檔案\nLeave reset file", font=('Arail', 10), height=3, width=15,command=self.Leave_reset_file).grid( row=5, column=3, padx=10, pady=10)
        self.tree.bind("<Dounble>",self.position)
    def Leave_reset_file(self):
        print("檔案設置完成式窗關閉")
        self.master.destroy()
    def Confirm_settings_file(self):
        print("檔案重設式窗關閉")
        self.master.destroy()
    def Delete_file(self):
        print("檔案刪除")
        pass
    def Copy_files(self):
        print("檔案複製")
        pass
    def Create_new_file(self):
        print("建立新檔")
        pass
    def position(self, event):
        for item in self.tree.selection():
            # item = I001
            item_text = self.tree.item(item, "values")
        self.column = self.tree.selection()
        print(self.column)
class Menu_4:
    def __init__(self, master):
        self.master = master
        self.master.title("專案設定 Project settings ")
        self.master.iconbitmap("D:\侯博允\實驗室\實驗室\measurment\lib\ico.ico")
        self.master.title("開始量測")
        self.newWindow = tk.Toplevel(self.master)
        self.menubar = tk.Menu(self.newWindow)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label="file")
        self.menubar.add_cascade(label="file" ,menu = self.filemenu)
        self.newWindow.config(menu=self.menubar)

def main():
    root = tk.Tk()
    app = start_menus(root)
    root.resizable(0, 0)
    root.after(250)  # 250單位是毫秒
    root.mainloop()

def create_ini():
    pass
def writein_ini(name):
    DEFAULT = ["a"]
    SYSTEM_DEFAULT = ["com_number", "y", "z"]
    INSTRUMENT_SETTINGS = ["port", "name"]
    if name in DEFAULT:
        pass
    elif name in SYSTEM_DEFAULT:
        file=configparser.ConfigParser
        pass
    elif name in INSTRUMENT_SETTINGS:
        pass
def input_ini(target,name):
    import configparser
    file = configparser.ConfigParser()
    file.read('settings.ini')
    val = file.get(target, name)
    print(val)
def parse_ini(ini_file):
    import configparser
    file = configparser.ConfigParser()
    file.read('settings.ini')
    for item in file:
        print('[%s]' % item)
        for var in file[item]:
            print('%s = %s' % (var, file[item][var]))

def read_ini():
    sys_config = configparser.ConfigParser()
    sys_config.read('settings.ini')
    return sys_config


if __name__ == '__main__':
    try:
        sys_config_file = read_ini()
        sys_config  = parse_ini(sys_config_file)
    except:
        pass

    main()
