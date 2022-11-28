
from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from payment import payment

class employee:
    def __init__(self,root):
        self.root= root
        self.root.title("Add employee")
        self.root.geometry("1250x600+50+50")
        self.root.config(bg="white")
        self.root.focus_force()


        title = Label(self.root, text="Add New employee", 
                                 font=("goudy old style",20,"bold"), 
                                 bg = "#07f0b6",fg="white").place(x=0,y=0, relwidth=1,height=50)



        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_mobile=StringVar()
        self.var_position=StringVar()
   


        txt_name = Label(self.root, text="Name", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=160)

        txt_email = Label(self.root, text="Email", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=230)

        txt_gender = Label(self.root, text="Gender", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=300)

        txt_dob = Label(self.root, text="DOB", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=370)

        txt_mobile = Label(self.root, text="Mobile", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=440)

        txt_doj = Label(self.root, text="DOJ", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=380,y=90)

        txt_city = Label(self.root, text="City", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=380,y=160)

        txt_state = Label(self.root, text="State", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=380,y=230)

        txt_position = Label(self.root, text="position", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=375,y=300)

        txt_adddress = Label(self.root, text="Address", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=370,y=370)



        

        self.position_list=[]
        self.fetch_position()

     
        self.txt_name = Entry(self.root, textvariable=self.var_name,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_name.place(x=110,y=160,width=200)

        txt_email = Entry(self.root, textvariable=self.var_email,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=110,y=230,width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female"),
                                 font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_gender.place(x=110,y=300,width=200)
        self.txt_gender.current(0)

        txt_dob = Entry(self.root, textvariable=self.var_dob,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=110,y=370,width=200)

        txt_mobile = Entry(self.root, textvariable=self.var_mobile,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=110,y=440,width=200)

        txt_doj = Entry(self.root, textvariable=self.var_doj,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=450,y=90,width=200)

        txt_city = Entry(self.root, textvariable=self.var_city,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=450,y=160,width=200)

        txt_state = Entry(self.root, textvariable=self.var_state,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=450,y=230,width=200)

       
        self.txt_position = ttk.Combobox(self.root, textvariable=self.var_position,values=self.position_list,
                                 font=("goudy old style",15),state='readonly',justify=CENTER)
        self.txt_position.place(x=450,y=300,width=200)
        self.txt_position.set("Select")

        self.txt_address=Text(self.root,font=("goudy old style",15),bg = "#f0f0f0",fg="black")
        self.txt_address.place(x=450,y=370, width =200,height=70)




        self.save_btn = Button(self.root, text="Save", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.save)
        self.save_btn.place(x=150,y=510,height=40,width=110)

        self.update_btn = Button(self.root, text="Update", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.update)
        self.update_btn.place(x=270,y=510,height=40,width=110)

        self.clear_btn = Button(self.root, text="Clear", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.clear)
        self.clear_btn.place(x=390,y=510,height=40,width=110)

        self.delete_btn = Button(self.root, text="Delete", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.delete)
        self.delete_btn.place(x=510,y=510,height=40,width=110)

        self.payment_btn = Button(self.root, text="Payment", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.payment)
        self.payment_btn.place(x=1080,y=510,height=40,width=110)


#######################################

        self.var_search=StringVar()
        lbl_search = Label(self.root, text="Search", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=720,y=60)

        text_search = Entry(self.root, textvariable=self.var_search,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=780,y=62,width=210)

        search_btn = Button(self.root, text="Search", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.search).place(x=1000,y=60,height=27,width=90)

        clear_btn = Button(self.root, text="Clear", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.search_clear).place(x=1100,y=60,height=27,width=90)





        self.pos_frame = Frame(self.root)
        self.pos_frame.place(x=720,y=120,width=470,height=380)


        scrollx=Scrollbar(self.pos_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.pos_frame,orient=VERTICAL)


        self.employeeTable=ttk.Treeview(self.pos_frame,columns=("id","name","email","gender","dob","mobile","doj","city","state","position","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)

        self.employeeTable.heading("id",text="id")
        self.employeeTable.heading("name",text="Name")
        self.employeeTable.heading("email",text="email")
        self.employeeTable.heading("gender",text="gender")
        self.employeeTable.heading("dob",text="dob")
        self.employeeTable.heading("mobile",text="mobile")
        self.employeeTable.heading("doj",text="doj")
        self.employeeTable.heading("city",text="city")
        self.employeeTable.heading("state",text="state")
        self.employeeTable.heading("position",text="position")
        self.employeeTable.heading("address",text="address")


        self.employeeTable["show"]="headings"

        self.employeeTable.column("id", width=50)
        self.employeeTable.column("name", width=150)
        self.employeeTable.column("email", width=150)
        self.employeeTable.column("gender", width=100)
        self.employeeTable.column("dob", width=100)
        self.employeeTable.column("mobile", width=100)
        self.employeeTable.column("doj", width=100)
        self.employeeTable.column("city", width=100)
        self.employeeTable.column("state", width=100)
        self.employeeTable.column("position", width=100)
        self.employeeTable.column("address", width=200)

       

        self.employeeTable.pack(fill=BOTH,expand=1)
        self.employeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()



    def payment(self):
        title = Label(self.root, text="Add New Employee", 
                                 font=("goudy old style",20,"bold"), 
                                 bg = "#07f0b6",fg="white").place(x=-300,y=0, relwidth=1,height=50)
        self.new_win = Toplevel(self.root)
        self.new_obj = payment(self.new_win)


    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from employee where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.employeeTable.delete(*self.employeeTable.get_children())
            for row in rows:
                self.employeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear(self):
        
        self.show()
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_mobile.set("")
        self.var_doj.set("")
        self.var_city.set("")
        self.var_state.set("")
        self.var_position.set("")
        self.txt_address.delete('1.0',END)
        

    def save(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Employee Name required", parent=self.root)
            else:
                cur.execute("Select *  from employee where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee Name already exist", parent=self.root)
                else: 
                    cur.execute("insert into employee (name,email,gender,dob,mobile,doj,city,state,position,address) values(?,?,?,?,?,?,?,?,?,?)",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_mobile.get(),
                        self.var_doj.get(),
                        self.var_city.get(),
                        self.var_state.get(),
                        self.var_position.get(),
                        self.txt_address.get("1.0",END)
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Employee added sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def update(self):
        pass
    
    def delete(self):
        pass

    def clear(self):
        pass

    def get_data(self,ev):
        pass

    def show(self):
        pass

    def search_clear(self):
        self.show()
        self.var_search.set("")

    def fetch_position(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("Select name from positions")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.position_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    root.minsize(1250, 600)
    root.maxsize(1250, 600)
    obj = employee(root)
    
    root.mainloop()