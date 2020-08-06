# import critical module
import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk
import os, sys, psutil, re, subprocess, re
from subprocess import CREATE_NEW_CONSOLE

# import associated python file
import get_file_parameter, gen_method, start_gen_sample
from msgbox_msg import info_msg, warning_msg, error_msg, yesno_msg

# GUI object parameter
font = ('Arial', 10)
width = 300
lf_height = 100
b_width = 100
# global variable
bg='white'



class Mainframe:
    def __init__(self, master):
        # variable settings
        self.parameter_settings = {}
        self.master = master
        self.master.title('PDAL CATIA實驗樣本產生器')
        self.master.configure(background='white')
        # GUI variables
        self.file_dir = ''
        # Main Title
        self.title = tk.Label(self.master, text='歡迎使用實驗樣本產生器，請依照步驟進行\n'
                                                'Welcome to Experiment Sample Generator, please use it step by step.',
                              font=font, anchor='center', bg=bg).grid(row=0, column=0, columnspan=6, sticky='we')
        # SubFrame 0
        self.Lframe0 = tk.LabelFrame(self.master, text='步驟零:開啟CATIA\nStep0: Start CATIA', font=font, width=width,
                                     height=lf_height, labelanchor='n', bg=bg).grid(
            row=1, column=0, columnspan=6, sticky='we', ipady=10, padx=10)
        self.indicator0 = tk.Label(self.Lframe0, text='未檢查\n(Not checked)', bg='red')
        self.indicator0.grid(row=1, column=0)
        self.button0 = tk.Button(self.Lframe0, text='開啟CATIA\n(Start CATIA)', font=font, command=self.start_CATIA
                                 ).grid(row=1, column=1, columnspan=4, sticky='we')
        # SubFrame 1
        self.Lframe1 = tk.LabelFrame(self.master, text='步驟一:設定初始樣本\nStep1:Set initial design sample file',
                                     font=font, width=width, height=lf_height, labelanchor='n', bg=bg).grid(
            row=2, column=0, columnspan=6, sticky='we', ipady=10, padx=10)
        self.indicator1 = tk.Label(self.Lframe1, text='未設定\n(Not Set)', bg='red')
        self.indicator1.grid(row=2, column=0)
        self.button1 = tk.Button(self.Lframe1, text='瀏覽檔案\n(Browse file)', font=font, command=self.load_file
                                 ).grid(row=2, column=1, columnspan=4, sticky='we')
        # SubFrame 2
        self.Lframe2 = tk.LabelFrame(self.master, text='步驟二:設定參數變異\nStep2:Set Each parameter"s level',
                                     font=font, width=width, height=lf_height, labelanchor='n', bg=bg).grid(
            row=3, column=0, columnspan=6, sticky='we', ipady=10, padx=10)
        self.indicator2 = tk.Label(self.Lframe2, text='未設定\n(Not Set)', bg='red')
        self.indicator2.grid(row=3, column=0)
        self.button2 = tk.Button(self.Lframe2, text='設定參數\n(Set Parameter)', font=font, command=self.param_setting
                                 ).grid(row=3, column=1, columnspan=4, sticky='we')
        # SubFrame 3
        self.Lframe3 = tk.LabelFrame(self.master, text='步驟三:確認設定參數\nStep3:Check summary of parameter settings',
                                     font=font, width=width, height=lf_height, labelanchor='n', bg=bg).grid(
            row=4, column=0, columnspan=6, sticky='we', ipady=10, padx=10)
        self.indicator3 = tk.Label(self.Lframe3, text='未設定\n(Not Set)', bg='red')
        self.indicator3.grid(row=4, column=0)
        self.button3 = tk.Button(self.Lframe3, text='確認設定\n(Confirm Settings)', font=font,
                                 command=self.param_confirm).grid(row=4, column=1, columnspan=4, sticky='we')
        # SubFrame 4
        self.Lframe4 = tk.LabelFrame(self.master, text='步驟四:開始生成\nStep4:Start sample output process',
                                     font=font, width=width, height=lf_height, labelanchor='n', bg=bg).grid(
            row=5, column=0, columnspan=6, sticky='we', ipady=10, padx=10)
        self.indicator4 = tk.Label(self.Lframe4, text='不可輸出\n(Cannot Output)', bg='red')
        self.indicator4.grid(row=5, column=0)
        self.button4 = tk.Button(self.Lframe4, text='開始生成\n(Start Output)', font=font, command=self.output_sample
                                 ).grid(row=5, column=1, columnspan=4, sticky='we')
        # Utility
        self.clear_setting = tk.Button(self.master, text='清空所有設定\n(Clear all settings)', command=self.clear_all
                                       ).grid(row=6, column=0, columnspan=3, sticky='we', padx=5, pady=5)
        self.exit_button = tk.Button(self.master, text='離開系統\n(Exit System)', command=self.exit
                                     ).grid(row=6, column=3, columnspan=3, sticky='we', padx=5, pady=5)

    def start_CATIA(self):
        # try to CATIA enviorment file
        env_dir = 'C:\ProgramData\DassaultSystemes\CATEnv'
        list_dir = os.listdir(env_dir)
        print(list_dir)
        if any('V5-6R' in file for file in list_dir):
            for file in list_dir:
                if 'V5-6R' in file:
                    env_file = open(env_dir + '\\' + file, 'rt')
                    env_line = env_file.read().splitlines()
                    for line in env_line:
                        if 'CATInstallPath' in line:
                            CATIA_dir = re.sub('CATInstallPath=', '', line)
                            env_name = re.sub('.txt', '', file)
                            print('get CATIA dir and env is %s , %s' % (CATIA_dir, env_name))

        else:
            tk.messagebox.showwarning('WARNING', 'No Suitable V5-6R Version CATIA installation found on this machine',
                                      parent=self.master)

        chk = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'CNEXT' in p.info['name']]
        print(chk)
        if chk == []:
            args = [r"%s\code\bin\CATSTART.exe" % CATIA_dir, "-run", "CNEXT.exe", "-env %s -direnv" % env_name,
                    "C:\ProgramData\DassaultSystemes\CATEnv", "-nowindow"]
            print(args)
            request = subprocess.Popen(args, shell=False, creationflags=CREATE_NEW_CONSOLE)
            print(str(request))
            print(os.getpid())
            # tk.messagebox.showinfo('ATTENTION', 'CATIA now Starting...')
            tk.messagebox.showinfo(info.CATStart_go()[0], info.CATStart_go()[1])
            self.indicator0.config(bg='green', text='已檢查\n(Checked)')
        else:
            # tk.messagebox.showinfo('ATTENTION', 'CATIA already started, skipped starting process...')
            tk.messagebox.showinfo(info.CATStart_ignore()[0], info.CATStart_ignore()[1])
            self.indicator0.config(bg='green', text='已檢查\n(Checked)')

    def load_file(self):
        if self.indicator0['bg'] == 'green':
            self.file_dir = ''
            dir_temp = filedialog.askopenfilename(title='選擇檔案', filetypes=(('CATIA Part', '*.CATPart'),))
            print(dir_temp, type(dir_temp))
            if dir_temp != '':
                self.file_dir = dir_temp
                self.indicator1.config(bg='green', text='已設定\n(Set)')
        else:
            tk.messagebox.showwarning('WARNING', '未檢查CATIA是否開啟或啟動!!')


    def param_setting(self):
        if self.indicator1['bg'] == 'green':
            print('Step 1 check passed')
            get_CAT_data = get_file_parameter.get_paramter_info()
            if get_CAT_data.open_file(self.file_dir) == 'ok':
                pass
            else:
                return
            parameter_data = get_CAT_data.read_parameter()
            if parameter_data == 'no param':
                tk.messagebox.showwarning('WARNING', '所選樣本檔案無設定參數')
                return
            elif parameter_data == 'fail':
                tk.messagebox.showerror('ERROR', '讀取參數失敗')
                return
            get_CAT_data.close_file()
            self.newwindow = tk.Toplevel(self.master)
            self.newwindow.resizable(0,0)
            self.newwindow.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.master.withdraw()
            # self.newwindow.bind('<Destroy>', self.on_destroy)
            self.app = Parameter_Setting(self.newwindow, parameter_data)
            self.master.deiconify()
            if self.app.check_confirm:
                print('check ok')
                print(self.app.parameter_settings)
                self.parameter_settings = self.app.parameter_settings
                self.indicator2.config(bg='green', text='已設定\n(Set)')
                # self.parameter_settings = self.app.treeview1.get_children()
            else:
                print(self.app.parameter_settings)
                print('check fail')
                self.parameter_settings = {}
                self.indicator3.config(bg='red', text='未設定\n(Not Set)')
            # self.app = Parameter_Setting(self.newwindow, [])
        else:
            tk.messagebox.showwarning('WARNING', '樣本檔案尚未設置!!')

    def param_confirm(self):
        listed_content = 'The parameter setting are listed below : \n'
        for title in self.parameter_settings:
            content = self.parameter_settings[title]
            listed_content += '{}\t{}\n'.format(title, content)
        listed_content += 'Are you sure the settings above is correct?'
        prompt = tk.messagebox.askquestion('All Parameter Summary', listed_content)
        print('Prompt:{}'.format(prompt))
        if prompt == 'yes':
            self.indicator3.config(bg='green', text='已設定\n(Set)')
        # check and green light the ouput process
        settings_state = [self.indicator0['bg'], self.indicator1['bg'], self.indicator2['bg'], self.indicator3['bg']]
        for state in settings_state:
            if state != 'green':
                tk.messagebox.showwarning('WARNING',
                                          'Step %s is not set yet, please check!!' % settings_state.index(state))
                return
        self.indicator4.config(bg='green', text='可輸出\nOutput Available')

    def output_sample(self):
        pass

    def clear_all(self):
        pass

    def exit(self):
        self.master.destroy()

    def on_closing(self):
        self.newwindow.destroy()
        self.master.deiconify()
        return

    def on_destroy(self, event):
        # self.newwindow.destroy()
        self.master.deiconify()
        return


class Parameter_Setting:
    def __init__(self, master, parameter_data):
        # set checking flag
        self.check_confirm = False
        self.parameter_settings = {}
        self.master = master
        self.parameter_data = parameter_data
        # GUi variables
        self.combovar1 = tk.StringVar()
        self.combovar2 = tk.StringVar()
        self.exp_method_option = ('全因子樣本輸出', '田口法',)
        self.gen_method_option = (('全因子樣本輸出',),('L4', 'L8', 'L9', 'L12', 'L18', 'L27',),)
        self.label1 = tk.Label(self.master, text='1.選擇實驗方法\nSelect Experiment Method', font=font,
                               ).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.combobox1 = ttk.Combobox(self.master, values=self.exp_method_option, state='readonly',
                                      textvariable=self.combovar1)
        self.combobox1.grid(row=0, column=3, columnspan=3, padx=50)
        self.label2 = tk.Label(self.master, text='2.選擇實驗樣本產生法\nSelect Experiment Sample Generation Method'
                               ).grid(row=1, column=0, columnspan=3)
        self.combobox2 = ttk.Combobox(self.master, values='', state='readonly', textvariable=self.combovar2)
        self.combobox2.grid(row=1, column=3, columnspan=3)
        self.label3 = tk.Label(self.master, text='2.設定各參數之實驗水準').grid(row=2, column=0, columnspan=6)
        self.treeview1 = ttk.Treeview(self.master, columns=['0', '1', '2', '3', '4'], selectmode='browse')
        self.treeview1.column('0', width=100, anchor='center')
        self.treeview1.column('1', width=100, anchor='center')
        self.treeview1.column('2', width=100, anchor='center')
        self.treeview1.column('3', width=100, anchor='center')
        self.treeview1.column('4', width=100, anchor='center')
        self.treeview1.heading('0', text='VAR1')
        self.treeview1.heading('1', text='VAR2')
        self.treeview1.heading('2', text='VAR3')
        self.treeview1.heading('3', text='VAR4')
        self.treeview1.heading('4', text='VAR5')
        self.treeview1.grid(row=3, column=0, columnspan=5, rowspan=6, padx=10)
        self.scrollbar1 = ttk.Scrollbar(self.master, orient='vertical', command=self.treeview1.yview)
        self.scrollbar1.grid(row=3, column=5, rowspan=6, sticky='ns')
        self.treeview1.configure(yscrollcommand=self.scrollbar1.set)
        self.clearparam = tk.Button(self.master, text='清除所有設定\nClear all settings', font=font,
                                    command=self.clear_settings).grid(row=10, column=0, columnspan=2, pady=5)
        self.confirmparam = tk.Button(self.master, text='確認參數設定\nConfirm all settings', font=font,
                                      command=self.confirm_settings).grid(row=10, column=2, columnspan=2, pady=5)
        self.cancel = tk.Button(self.master, text='取消設定\nCancel Settings', font=font, command=self.cancel_setting
                                ).grid(row=10, column=4, columnspan=2, pady=5)
        # event binding
        self.combobox1.bind('<<ComboboxSelected>>', self.change_gen_method)
        self.combobox2.bind('<<ComboboxSelected>>', self.check_variable_len_for_method)
        self.treeview1.bind('<Double-1>', self.set_parameter_data)
        # add CAT parameter from data
        if parameter_data != []:
            for param in parameter_data:
                self.treeview1.insert('', 'end', text=param)
        else:
            tk.messagebox.showwarning('WARNING', 'No Parameter Founded!!', parent=self.master)
            self.master.destroy()
        self.master.wait_window()

    def change_gen_method(self, event):
        if self.combobox1.get() == self.exp_method_option[0]:
            self.combobox2.config(values=self.gen_method_option[0])
            self.combobox2.set('')
        elif self.combobox1.get() == self.exp_method_option[1]:
            self.combobox2.config(values=self.gen_method_option[1])
            self.combobox2.set('')
        else:
            pass

    def check_variable_len_for_method(self, event):
        if self.combobox1.get() == self.exp_method_option[1]:
            taguchi_method = getattr(gen_method, self.combobox2.get())
            if len(self.parameter_data) > len(taguchi_method):
                tk.messagebox.showwarning('WARNING', 'Too Much Variable for Selected Taguchi OA!!')
                self.combobox2.set('')
                return
            else:
                pass

    # old one which shows another screen to set values
    # def set_parameter_data(self, event):
    #     exp_combobox = self.combovar1.get()
    #     gen_combobox = self.combovar2.get()
    #     target = self.treeview1.selection()[-1]
    #     if exp_combobox != '' and gen_combobox != '':
    #         if target is not None:
    #             target_param = self.treeview1.item(target, 'text')
    #             # hide master window
    #             self.master.withdraw()
    #             # ----------------This Part is to ask user to select variable's type is Bool or Num(Float)-------------
    #             # ask the variable type
    #             is_bool = tk.messagebox.askyesno('Is boolean type?',
    #                                              'Does the variable is boolean (True & False) type?')
    #             if is_bool:
    #                 var_type = 'bool'
    #             else:
    #                 is_float = tk.messagebox.askyesno('Is Number type?',
    #                                                   'Does the variable is Number (123 or 123.456) type?')
    #                 if is_float:
    #                     var_type = 'float'
    #                 else:
    #                     tk.messagebox.showwarning('ATTENTION',
    #                                               'I do not know what type is the variable, please reselect...')
    #                     # reshow main window
    #                     self.master.deiconify()
    #                     return
    #             # --------------------------------SEPERATION LINE------------------------------------------------------
    #             # -------This part is to set available level for variable according to selected OA---------------------
    #             if exp_combobox == '田口法':
    #                 taguchi_OA_level = gen_method.acceptable_param_count[gen_combobox]
    #                 if gen_combobox == 'L18':
    #                     print(re.split('[x&]',taguchi_OA_level))
    #                     level1, count1, level2, count2 = re.split('[x&]', taguchi_OA_level)
    #                     if target == 'I001':
    #                         var_level = level1
    #                     else:
    #                         var_level = level2
    #                         if is_bool:
    #                             tk.messagebox.showwarning('WARNING', 'The variable should be set to three-level factor '
    #                                                                  'instead of two-factor boolean!')
    #                             self.master.deiconify()
    #                             return
    #                 else:
    #                     level1, count1 = taguchi_OA_level.split('x')
    #                     var_level = level1
    #             else:
    #                 var_level = 5
    #             # create new window
    #             self.newwindow = tk.Toplevel(self.master)
    #             self.newwindow.resizable(0, 0)
    #             self.app = Parameter_data_setting(self.newwindow, exp_combobox, var_type, int(var_level))
    #             # reshow main window
    #             self.master.deiconify()
    #             if self.app.dataset != []:
    #                 self.treeview1.item(target, values=(self.app.dataset))
    #             else:
    #                 tk.messagebox.showwarning('ATTENTION', 'The param %s not set any variables yet!!' % target_param)
    #                 return
    #         else:
    #             return
    #     else:
    #         tk.messagebox.showwarning('ATTENTION', 'Exp method or Gen method not selected yet!')
    #         return

    def set_parameter_data(self, event):
        for item in self.treeview1.selection():
            item_text = self.treeview1.item(item, 'values')
        print('target XY=%s %s' % (event.x, event.y))
        target_col = self.treeview1.identify_column(event.x)
        target_row = self.treeview1.identify_row(event.y)
        print('target col and row = %s %s' % (target_col, target_row))
        cn = int(str(target_col).replace('#', ''))
        rn = int(str(target_row).replace('I', ''))
        print('cn, rn is = %s %s' % (cn, rn))
        # print('entry edit will placed at x=%s, y=%s' % (16 + (cn - 1) * 130, 6 + rn * 20))
        # print('okb will be placed at x=%s, y=%s' % (90 + (cn - 1) * 242, 2 + rn * 20))
        entryedit = tk.Text(self.treeview1, width=13, height=1, font=font)
        entryedit.place(x=206 + (cn - 1) * 100, y=6 + rn * 20)
        entryedit.config(wrap='none')
        def saveedit():
            self.treeview1.set(item, column=target_col, value=entryedit.get(0.0, "end"))
            entryedit.destroy()
            okb.destroy()
        okb = tk.Button(self.treeview1, text='OK', width=4, command=saveedit)
        okb.place(x=156 + (cn - 1) * 100, y=6 + rn * 20)


    def clear_settings(self):
        pass

    def confirm_settings(self):
        # checking all parameters
        if self.combovar1.get() != '' or self.combovar2.get() != '':
            any_empty_data = 0
            actual_data = {}
            all_data = self.treeview1.get_children()
            each_data_length = []
            for id in all_data:
                actual_data.update({self.treeview1.item(id)['text']: self.treeview1.item(id)['values']})
                each_data_length.append(len(self.treeview1.item(id)['values']))
                if self.treeview1.item(id)['values'] == '':
                    any_empty_data += 1
            print(actual_data)
            if any_empty_data != 0:
                tk.messagebox.showinfo('ATTENTION', 'Do you have any parameter not set yet?')
                return
            else:
                self.parameter_settings = actual_data
                self.check_confirm = True
                self.master.destroy()

        else:
            tk.messagebox.showwarning('ATTENTION', 'Exp method or Gen method not selected yet!')

    def cancel_setting(self):
        self.master.destroy()

class Parameter_data_setting:
    def __init__(self, master, exp_gen_method, var_type, var_level):
        self.exp_gen_method = exp_gen_method
        self.master = master
        self.var_level = var_level
        self.var_type = var_type
        self.dataset = []
        self.label0 = tk.Label(self.master, text="設定變數之各水準變數\nSet The variable's level factors", font=font
                               ).grid(row=0, column=0, columnspan=3, sticky='we', padx=20)
        self.label1 = tk.Label(self.master, text='第一水準變數\nFirst Level Factor', font=font).grid(
            row=1, column=0, padx=20)
        self.label2 = tk.Label(self.master, text='第二水準變數\nSecond Level Factor', font=font).grid(
            row=2, column=0, padx=20)

        if var_type == 'bool':
            self.var0 = tk.BooleanVar()
            self.var0.set(True)
            self.var1 = tk.BooleanVar()
            self.var1.set(True)

            self.combobox1 = ttk.Combobox(self.master, values=(True, False,), state='readonly',
                                          textvariable=self.var0)
            self.combobox1.grid(row=1, column=1, columnspan=2, padx=20, sticky='we')
            self.combobox2 = ttk.Combobox(self.master, values=(True, False,), state='readonly',
                                          textvariable=self.var1)
            self.combobox2.grid(row=2, column=1, columnspan=2, padx=20, sticky='we')
        elif var_type == 'float':
            self.var0 = tk.DoubleVar()
            self.var1 = tk.DoubleVar()
            self.var2 = tk.DoubleVar()
            self.var3 = tk.DoubleVar()
            self.var4 = tk.DoubleVar()
            self.label3 = tk.Label(self.master, text='第三水準變數\nThird Level Factor', font=font)
            self.label3.grid(row=3, column=0, padx=20)
            self.label4 = tk.Label(self.master, text='第四水準變數\nFourth Level Factor', font=font)
            self.label4.grid(row=4, column=0, padx=20)
            self.label5 = tk.Label(self.master, text='第五水準變數\nFifth Level Factor', font=font)
            self.label5.grid(row=5, column=0, padx=20)
            self.entry1 = tk.Entry(self.master, textvariable=self.var0)
            self.entry1.grid(row=1, column=1, columnspan=2, padx=20, sticky='we')
            self.entry2 = tk.Entry(self.master, textvariable=self.var1)
            self.entry2.grid(row=2, column=1, columnspan=2, padx=20, sticky='we')
            self.entry3 = tk.Entry(self.master, textvariable=self.var2)
            self.entry3.grid(row=3, column=1, columnspan=2, padx=20, sticky='we')
            self.entry4 = tk.Entry(self.master, textvariable=self.var3)
            self.entry4.grid(row=4, column=1, columnspan=2, padx=20, sticky='we')
            self.entry5 = tk.Entry(self.master, textvariable=self.var4)
            self.entry5.grid(row=5, column=1, columnspan=2, padx=20, sticky='we')

        self.button1 = tk.Button(self.master, text='清空所有變數設定\nClear all Param settings', font=font,
                                 command=self.clear_var).grid(row=6, column=0, padx=5)
        self.button2 = tk.Button(self.master, text='設定變數\nSet Parameter Settings', font=font, command=self.set_var
                                 ).grid(row=6, column=1, padx=5)
        self.button3 = tk.Button(self.master, text='取消設定\nCancel Parameter Settings', font=font, command=self.exit
                                 ).grid(row=6, column=2, padx=5)
        # disable entry by variable level
        if var_type == 'float':
            if var_level == 2:
                self.label3.grid_forget()
                self.label4.grid_forget()
                self.label5.grid_forget()
                self.entry3.grid_forget()
                self.entry4.grid_forget()
                self.entry5.grid_forget()
            elif var_level == 3:
                self.label4.grid_forget()
                self.label5.grid_forget()
                self.entry4.grid_forget()
                self.entry5.grid_forget()
            else:
                pass
        # testing wait_window
        self.master.wait_window()

    def clear_var(self):
        if self.var_type == 'bool':
            self.combobox1.selection_clear()
            self.combobox2.selection_clear()
        else:
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')
            self.entry3.delete(0, 'end')
            self.entry4.delete(0, 'end')
            self.entry5.delete(0, 'end')

    def set_var(self):
        zero_cout = 0
        if self.var_type == 'bool':
            if self.var0.get() != self.var1.get():
                self.dataset = [self.var0.get(), self.var1.get()]
                self.master.destroy()
            else:
                tk.messagebox.showwarning('ATTENTION', 'Same condition found, Please check your settings.',
                                          parent=self.master)

        elif self.var_type == 'float':
            temp = [self.var0.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get()]
            for data in range(0, int(self.var_level)-1):
                if temp[data] == 0:
                    zero_cout += 1
            if zero_cout == 0:
                for data in temp:
                    if data != 0:
                        self.dataset.append(data)
                self.master.destroy()
            # elif 0 < zero_cout < 4:
            #     set_cout = 5-zero_cout
            #     prompt = tk.messagebox.askyesno('Check Parameter?', 'The parameter you set is:\n'
            #                                                         '%s\n'
            #                                                         'The amount of parameter set is: %s\n'
            #                                                         'Are you sure this is what you want?'
            #                                     % (temp, set_cout))
            #     if prompt:
            #         for data in temp:
            #             if data != 0:
            #                 self.dataset.append(data)
            #         self.master.destroy()
            #     else:
            #         tk.messagebox.showwarning('ATTEHTION', 'No Input found, Please check your settings.',
            #                               parent=self.master)
            else:
                if self.exp_gen_method == '全因子樣本輸出':
                    for data in temp:
                        if data != 0:
                            self.dataset.append(data)
                    self.master.destroy()
                else:
                    tk.messagebox.showwarning('ATTEHTION', 'No Input found, Please check your settings.',
                                          parent=self.master)

    def exit(self):
        self.master.destroy()



def main():
    root = tk.Tk()
    app = Mainframe(root)
    root.resizable(0, 0)
    root.mainloop()


if __name__ == '__main__':
    # initialize global message
    info = info_msg()
    warning = warning_msg()
    error = error_msg()
    yesno = yesno_msg()
    main()
