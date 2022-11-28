from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from positions import positions
from employee import employee
from time import strftime

class hrms:
    def __init__(self,root):
        self.root= root
        self.root.title("Employee Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Employee Management System", 
                                 font=("goudy old style",20,"bold"), 
                                 bg = "#07f0b6",fg="white").place(x=0,y=0, relwidth=1,height=50)

        hr_name = Label(self.root, text="Hi, HR", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black").place(x=1150,y=0,height=50)

        logout_btn = Button(self.root, text="Logout", 
                                 font=("goudy old style",10), 
                                 bg = "#07f0b6",fg="black").place(x=1250,y=10,height=30)

#####################################

        positions_btn = Button(text="Add Positions", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2", command=self.position).place(x=20,y=70,height=40, width=200)

        add_employee_btn = Button(self.root, text="Add Employee", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2", command=self.employee).place(x=240,y=70,height=40, width=200)

        exit_btn = Button(self.root, text="Exit", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2", command=self.exit).place(x=680,y=70,height=40, width=200)   


########################################


        self.lbl_total = Label(self.root,text="Total Employees\n[ 0 ]", font=("goudy old style",20),bg="lightgrey",fg="white")
        self.lbl_total.place(x=20,y=180,width=300,height=100)

        self.lbl_total = Label(self.root,text="Total Employees\n[ 0 ]", font=("goudy old style",20),bg="lightgrey",fg="white")
        self.lbl_total.place(x=20,y=320,width=300,height=100)

        self.lbl_total = Label(self.root,text="Total Employees\n[ 0 ]", font=("goudy old style",20),bg="lightgrey",fg="white")
        self.lbl_total.place(x=20,y=460,width=300,height=100)

        self.bg_img = Image.open("img/hr.jpg")
        self.bg_img = self.bg_img.resize((900,540), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180, width=920, height=390) 





#########################
        footer = Label(self.root, text="Human Resource Management System - Employee Payment Rollout System\nContact us for any technical queries. rushabhdabhade30@gmail.com",
                        font=("goudy old style",13),bg="#07f0b6",fg="white").pack(side=BOTTOM,fill=X)                     



    def position(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = positions(self.new_win)

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employee(self.new_win)
           
    def exit(self):
            pass




if __name__ == "__main__":
    root = Tk()
    root.minsize(1350, 700)
    root.maxsize(1400, 690)
    obj = hrms(root)
    root.mainloop()