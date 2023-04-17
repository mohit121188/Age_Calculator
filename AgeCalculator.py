import tkinter
from tkcalendar import Calendar
from tkinter import messagebox
import datetime
import logic

def get_today_date():
    today = datetime.date.today()
    today = today.strftime("%Y-%m-%d")
    return today


class MyGUI:
    def __init__(self):
        #root widget
        self.root=tkinter.Tk()
        self.root.title("Age Calculator")
        self.root.geometry("600x200")
        self.root_icon=tkinter.PhotoImage(file="D:/Python Projects/age_calculator/images/icon.png")
        self.root.iconphoto(True,self.root_icon)
        self.root.config(bg="black")
        self.root.protocol("WM_DELETE_WINDOW",self.action_exit_btn)
        #lable,entry, button widget
        self.lbl_enter_birth_date=tkinter.Label(self.root,text="Date of Birth",font=('consolas',12,'bold'))
        self.lbl_enter_birth_date.config(bg='black',fg='white',font=('consolas',12,'bold'))
        self.entry_selected_birth_date=tkinter.Entry(self.root,font=('consolas',12,'bold'),state="readonly",width=30)
        self.btn_select_birth_date=tkinter.Button(self.root,text="Select",bg='black',fg='white',font=('calibre',11,'bold'),command=self.action_sel_dob)
        self.lbl_enter_age_at_date_of=tkinter.Label(self.root,text="Age at the date of",font=('consolas',12,'bold'))
        self.lbl_enter_age_at_date_of.config(bg='black',fg='white',font=('consolas',12,'bold'))
        self.btn_select_age_ate_date_of=tkinter.Button(self.root,text='Select',bg='black',fg='white',font=('calibre',11,'bold'),command=self.action_sel_date_of_age)
        self.entry_age_at_date_of=tkinter.Entry(self.root,font=('consolas',12,'bold'),state='normal',width=30)
        self.entry_age_at_date_of.insert(0,get_today_date())
        self.entry_age_at_date_of.config(state='readonly')
        self.btn_calculate=tkinter.Button(self.root,text="Calculate",font=('calibre',11,'bold'),fg='white',bg='black',command=self.action_calculate)
        self.lbl_your_age=tkinter.Label(self.root,text="Your Age",font=('consolas',12,'bold'))
        self.lbl_your_age.config(fg='white',bg='black')
        self.entry_your_age=tkinter.Entry(self.root,font=('consolas',12,'bold'),state='readonly',width=30)

        self.btn_reset=tkinter.Button(self.root,text="Reset",font=('calibre',11,'bold'),fg='white',bg='black',command=self.action_reset_btn)
        self.btn_exit=tkinter.Button(self.root,text="Exit",font=('calibre',11,'bold'),fg='white',bg='black',command=self.action_exit_btn)
        self.lbl_enter_birth_date.grid(row=0,column=0,sticky='E',padx=4,pady=4)
        self.entry_selected_birth_date.grid(row=0,column=1,padx=4,pady=4)
        self.btn_select_birth_date.grid(row=0,column=2,padx=4,pady=4)
        self.lbl_enter_age_at_date_of.grid(row=1,column=0,sticky='E',padx=4,pady=4)
        self.entry_age_at_date_of.grid(row=1,column=1,padx=4,pady=4)
        self.btn_select_age_ate_date_of.grid(row=1,column=2,padx=4,pady=4,sticky='W')
        self.btn_calculate.grid(row=2,column=1)
        self.lbl_your_age.grid(row=3,column=0,sticky='E',padx=4,pady=4)
        self.entry_your_age.grid(row=3,column=1,padx=4,pady=4,)
        self.btn_reset.grid(row=4,column=0,sticky='E',padx=4,pady=4)
        self.btn_exit.grid(row=4,column=1,padx=4,pady=4,sticky='E')
        self.calendar = Calendar(self.root, selectmode='day', date_pattern='yyyy-mm-dd')
        #string variables
        self.selected_date=None
        self.selected_dob=None
        self.selected_date_of_age=get_today_date()
        #defining the object of class Logic
        self.logic_object=logic.Logic()
        self.root.mainloop()

    def action_exit_btn(self):
        ans=messagebox.askyesno("Quitting","Are You Sure Want To Exit?")
        if ans==True:
            self.root.destroy()

    def action_reset_btn(self):
        self.entry_selected_birth_date.config(state='normal')
        self.entry_selected_birth_date.delete(0,tkinter.END)
        self.entry_selected_birth_date.config(state='readonly')
        self.entry_selected_birth_date.config(state='normal')
        self.entry_age_at_date_of.delete(0,tkinter.END)
        self.entry_age_at_date_of.insert(0,get_today_date())
        self.entry_selected_birth_date.config(state='readonly')
        self.entry_your_age.config(state='normal')
        self.entry_your_age.delete(0,tkinter.END)
        self.entry_your_age.config(state='readonly')
        self.selected_date=""
        self.selected_dob=""
        self.selected_date_of_age=""
        self.entry_selected_birth_date.focus()

    def action_sel_dob(self):
        self.flag_dob_selected=True
        self.calendar.place(x=250, y=40)
        self.calendar.selection_clear()
        self.calendar.bind("<<CalendarSelected>>", self.hide_calendar1)


    def action_sel_date_of_age(self):
        self.flag_date_of_age_selected=True
        self.calendar.place(x=250, y=40)
        self.calendar.selection_clear()
        self.calendar.bind("<<CalendarSelected>>", self.hide_calendar2)


    def action_calculate(self):
        year1,month1,day1=self.selected_dob.split("-")
        year2,month2,day2=self.selected_date_of_age.split("-")
        self.logic_object.set_date1(int(year1),int(month1),int(day1))
        self.logic_object.set_date2(int(year2),int(month2),int(day2))
        years,months,days=self.logic_object.calculate_duration()
        self.entry_your_age.config(state='normal')
        self.entry_your_age.delete(0,tkinter.END)
        final_message=str(years)+" years, "+str(months)+" months, "+str(days)+" days."
        self.entry_your_age.insert(0,final_message)
        self.entry_your_age.config(state='readonly')

    def hide_calendar1(self,event=None):
        self.selected_date = self.calendar.get_date()
        self.calendar.place_forget()
        self.selected_dob = self.selected_date
        self.entry_selected_birth_date.config(state='normal')
        self.entry_selected_birth_date.delete(0,tkinter.END)
        self.entry_selected_birth_date.insert(0, self.selected_dob)
        self.entry_selected_birth_date.config(state='readonly')



    def hide_calendar2(self,event=None):
        self.selected_date = self.calendar.get_date()
        self.calendar.place_forget()

        self.selected_date_of_age = self.selected_date
        self.entry_age_at_date_of.config(state='normal')
        self.entry_age_at_date_of.delete(0, tkinter.END)
        self.entry_age_at_date_of.insert(0, self.selected_date_of_age)
        self.entry_selected_birth_date.config(state='readonly')
        print(self.selected_date_of_age)

obj=MyGUI()