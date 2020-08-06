import tkinter as tk
import tkinter.ttk
from PIL import Image, ImageTk
import os
import datetime

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print('Current Directory is : ' + BASE_DIR)
# common tkinter settings
font = ('Arial', 10,)


class start_menus:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x400')
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
        self.title2 = tk.Label(self.master, text='Wireless Measure and quality '
                                                 'Control System\nwith Cloud Visualization Integration-CLIENT',
                               font=('Arial', 15))
        self.title2.grid(row=2, column=0)
        self.button1 = tk.Button(self.master, text='新增量測專案\nCreate New Measurement Project', width=30,command=self.program_creation)
        self.button1.grid(row=3, column=0, pady=3)
        self.button2 = tk.Button(self.master, text='無線量具測試\nWireless measuring tool test', width=30,command=self.Wireless_measuring_tool_test)
        self.button2.grid(row=4, column=0, pady=3)
        self.button1 = tk.Button(self.master, text='客戶端設定\nClient Settings', width=30)
        self.button1.grid(row=5, column=0, pady=3)
        self.button1 = tk.Button(self.master, text='離開系統\nExit System', width=30,command=self.exit)
        self.button1.grid(row=6, column=0, pady=3)
    def exit(self):
        print("離開")
        self.master.destroy()
    def program_creation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.root =Menus_1(self.newWindow)
        print("檔案建立")
    def Wireless_measuring_tool_test(self):
        self.newWindow=tk.Toplevel(self.master)
        self.root=Menus_2(self.newWindow)
class Menus_1:
    def __init__(self,master):
        self.master=master
        self.master.resizable(0,0)
        self.master.title("檔案建立")
        self.frames1 = tk.Frame(self.master).grid(sticky='nswe')
        self.title1 = tk.Label(self.master, text='檔案名稱').grid(row=1,column=0,pady=20)
        self.texts1_1 = tk.Label(self.master, text='確認').grid(row=2,column=0,pady=20)
        self.nextpartbut_1=tk.Button(self.master,text="下一頁",command=self.nextpart).grid(row=3,column=0,pady=20)
    def nextpart(self):
        self.newWindows=tk.Toplevel(self.master)
        self.root=Menus_2(self.newWindows)
        self.master.root.withdraw()
class Menus_2:
    def __init__(self,master):
        self.master = master
        self.master.resizable(0, 0)
        self.master.title("檔案建立")
        self.frames1 = tk.Frame(self.master).grid(sticky='nswe')
        self.title1 = tk.Label(self.master, text='檔案名稱').grid(row=1, column=0, pady=20)
        self.texts1_1 = tk.Label(self.master, text='確認').grid(row=2, column=0, pady=20)
        self.nextpartbut_1 = tk.Button(self.master, text="下一頁",).grid(row=3, column=0, pady=20)
def main():
    root = tk.Tk()
    app = start_menus(root)
    root.resizable(0, 0)
    root.mainloop()

if __name__ == '__main__':
    main()
