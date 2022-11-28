from tkinter import*
from tkinter import ttk
from cgitb import text
from email import message
from tkinter import*
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import sqlite3




class payment:
    def __init__(self,root):
        self.root= root
        self.root.title("Payment")
        self.root.geometry("600x600+730+50")
        self.root.config(bg="white")
        self.root.focus_force()



        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_basic=StringVar()
        self.var_leave=StringVar()
        self.var_hra=StringVar()
        self.var_medical=StringVar()
        self.var_provident=StringVar()
        self.var_income=StringVar()
        
        self.roll_list=[]
        self.fetch_roll()

        title = Label(self.root, text="Employee payment", 
                                 font=("goudy old style",20,"bold"), 
                                 bg = "#07f0b6",fg="white").place(x=0,y=10, relwidth=1,height=50)

        txt_roll = Label(self.root, text="Roll no.", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=70)

        

        txt_month_year = Label(self.root, text="Month & Year", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=230,y=70)


        self.txt_roll = ttk.Combobox(self.root, textvariable=self.var_roll,values=self.roll_list,
                                 font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_roll.place(x=100,y=70,width=90)
        self.txt_roll.set("Select")



        self.txt_month = ttk.Combobox(self.root, textvariable=self.var_month,values=("Month","Jan","Feb","Mar","Apr","May","Jun","jul","Aug","Sep","Nov","Dec"),
                                 font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_month.place(x=370,y=70,width=100)
        self.txt_month.current(0)

        self.txt_year = ttk.Combobox(self.root, textvariable=self.var_year,values=("Year","2021","2022","2023","2024","2025","2026"),
                                 font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_year.place(x=480,y=70,width=100)
        self.txt_year.current(0)

      #  separator = ttk.Separator(self.root,orient='horizontal')
       # separator.place(x=0,y=150, relheight=1, relwidth=1)


        txt_earning = Label(self.root, text="Earning", 
                                 font=("goudy old style",15,"bold"), 
                                 bg = "white",fg="black").place(x=130,y=150)

        txt_deduction = Label(self.root, text="Deduction", 
                                 font=("goudy old style",15,"bold"), 
                                 bg = "white",fg="black").place(x=390,y=150)


        txt_basic = Label(self.root, text="Basic", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=200)

        txt_hra = Label(self.root, text="HRA", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=240)

        txt_medical = Label(self.root, text="Coveyance", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=280)


        txt_provident = Label(self.root, text="Provident", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=300,y=200)

        txt_income = Label(self.root, text="Income Tax", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=300,y=240)

        txt_leave = Label(self.root, text="Leave Deduction", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=300,y=280)


##################################################################################################


        self.txt_basic = Entry(self.root, textvariable=self.var_basic,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_basic.place(x=130,y=200, width=90)

        self.txt_hra = Entry(self.root, textvariable=self.var_hra,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_hra.place(x=130,y=240, width=90)

        self.txt_medical = Entry(self.root, textvariable=self.var_medical,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_medical.place(x=130,y=280, width=90)
        
        self.txt_provident = Entry(self.root, textvariable=self.var_provident,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_provident.place(x=450,y=200, width=90)

        self.txt_income = Entry(self.root, textvariable=self.var_income,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_income.place(x=450,y=240, width=90)

        self.txt_leave = Entry(self.root, textvariable=self.var_leave,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_leave.place(x=450,y=280, width=90)

        submit_btn = Button(self.root, text="Submit", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2").place(x=450,y=330,height=27,width=90)



        billarea=Frame(self.root,bg = "#07f0b6")
        billarea.place(x=30,y=370,width=470,height=200)
        
        self.txtarea=Text(billarea)
       
        self.txtarea.pack(fill=BOTH,expand=1)
        #self.employeeTable=ttk.Treeview(self.pos_frame,columns=("roll","name",))
        self.intro()

        #self.employeeTable.heading("roll",text="Roll")
        #self.employeeTable.heading("name",text="Name")
        
       #self.employeeTable["show"]="headings"

        #self.employeeTable.column("roll", width=235)
        #self.employeeTable.column("name", width=235)
    def intro(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\tHuman Resourse Management Mysten\n\tXYZ Co. Ltd.")
        self.txtarea.insert(END,f"\n\nEmployee no. : ")
        self.txtarea.insert(END,f"Employee Name :")
        self.txtarea.insert(END,f"\nPhone No. : ")
        self.txtarea.insert(END,"\n====================================\n")
        self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
        self.txtarea.insert(END,"\n====================================\n")      

        print_btn = Button(self.root, text="Print", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2").place(x=520,y=480,height=27,width=60)

        mail_btn = Button(self.root, text="Mail", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2").place(x=520,y=540,height=27,width=60)





    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
          cur.execute("Select roll from employee")
          rows=cur.fetchall()
          if len(rows)>0:
            for row in rows:
                self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")





if __name__ == "__main__":
    root = Tk()
    root.minsize(600, 600)
    root.maxsize(600, 600)
    obj = payment(root)
    
    root.mainloop()