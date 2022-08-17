import time
from tkinter import *
import multiprocessing
from tkinter import ttk, messagebox
from threading import *
hour_list = list(range(0, 24))
min_sec_list = list(range(0, 60))
class CountDown:
    def __init__(self, root):
        self.window = root
        self.window.geometry("480x320+0+0")
        self.window.title('Countdown Timer')
        self.window.configure(bg='black')
        self.window.resizable(width = False, height = False)
        self.pause = False
        self.button_frame = Frame(self.window, bg="black", width=240, height=40)
        self.button_frame.place(x=200, y=150)
        self.time_frame = Frame(self.window, bg="black", width=480, height=120).place(x=0, y=210)
        time_label = Label(self.window, text="Set Time", font=("times new roman",20, "bold"), bg='black',fg='red').place(x=180, y=30)
        hour_label = Label(self.window, text="Hour", font=("times new roman",15), bg='black', fg='white').place(x=50, y=70)
        minute_label = Label(self.window, text="Minute", font=("times new roman",15), bg='black', fg='white').place(x=200, y=70)
        second_label = Label(self.window, text="Second", font=("times new roman",15), bg='black', fg='white').place(x=350, y=70)
        self.hour = IntVar()
        self.hour_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.hour, font=("times new roman",15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.place(x=50,y=110)
        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.minute, font=("times new roman",15))
        self.minute_combobox['values'] = min_sec_list
        self.minute_combobox.place(x=200,y=110)
        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.second, font=("times new roman",15))
        self.second_combobox['values'] = min_sec_list
        self.second_combobox.place(x=350,y=110)
        cancel_button = Button(self.window, text='Cancel', font=('Helvetica',12), bg="white", fg="black", command=self.Cancel).place(x=50, y=160)
        set_button = Button(self.window, text='Set', font=('Helvetica',12), bg="white", fg="black", command=self.Get_Time).place(x=130, y=160)
    def Cancel(self):
        self.pause = True
        self.window.destroy()
    def Get_Time(self):
        self.time_display = Label(self.time_frame, 
        font=('Helvetica', 20 , "bold"), 
        bg = 'black', fg = 'red')
        self.time_display.place(x=130, y=230)
        try:
            h = (int(self.hour_combobox.get())*3600)
            m = (int(self.minute_combobox.get())*60)
            s = (int(self.second_combobox.get()))
            self.time_left = h + m + s
            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!',\
                'Please select a right time to set')
            else:
                start_button = Button(self.button_frame, text='Start', font=('Helvetica',12), bg="white", fg="black", command=self.Threading).place(x=100, y=10)
                pause_button = Button(self.button_frame, text='Pause', font=('Helvetica',12), bg="white", fg="black", command=self.pause_time).place(x=170, y=10)
                reset_button = Button(self.button_frame, text='Reset', font=('Helvetica',12), bg="white", fg="black", command=self.reset_time).place(x=20, y=10)
        except Exception as es:
            messagebox.showerror("Error!", \
            f"Error due to {es}")
    def Threading(self):
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()
    def Clear_Screen(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
    def pause_time(self):
        self.pause = True
        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
        self.time_display.update()
    def reset_time(self):
        self.time_left = 0
        self.time_display.config(text="Time Left: 0: 0: 0")
        self.time_display.update()
        self.Clear_Screen()
        self.Get_Time()
    def start_time(self):
        self.pause = False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)
            self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
            self.time_display.update()
            time.sleep(1)
            self.time_left = self.time_left -1
            if self.time_left <= 0:
                messagebox.showinfo('Time Over','Please ENTER')
                self.Clear_Screen()
            if self.pause == True:
                break
if __name__ == "__main__":
    root = Tk()
    obj = CountDown(root)
    root.mainloop()