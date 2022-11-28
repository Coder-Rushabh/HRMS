
from tkinter import*
from tkinter import ttk, messagebox
import sqlite3

class positions:
    def __init__(self,root):
        self.root= root
        self.root.title("Add Positions")
        self.root.geometry("1250x600+50+50")
        self.root.config(bg="white")
        self.root.focus_force()


        title = Label(self.root, text="Add New Positions", 
                                 font=("goudy old style",20,"bold"), 
                                 bg = "#07f0b6",fg="white").place(x=0,y=0, relwidth=1,height=50)



        self.var_ID=StringVar()
        self.var_name=StringVar()
        self.var_posts=StringVar()
   


        txt_name = Label(self.root, text="Name of\nPosition", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=90)

        txt_posts = Label(self.root, text="Number of\nPosts", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=160)

        txt_description = Label(self.root, text="Description", 
                                 font=("goudy old style",15), 
                                 bg = "white",fg="black").place(x=20,y=230)


        

        self.txt_name = Entry(self.root, textvariable=self.var_name,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_name.place(x=150,y=90, width=200)

        txt_posts = Entry(self.root, textvariable=self.var_posts,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black").place(x=150,y=160,width=200)

        self.txt_description = Text(self.root,
                                 font=("goudy old style",15), 
                                 bg = "#f0f0f0",fg="black")
        self.txt_description.place(x=150,y=230,width=400,height=100)




        self.save_btn = Button(self.root, text="Save", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.save)
        self.save_btn.place(x=150,y=400,height=40,width=110)

        self.update_btn = Button(self.root, text="Update", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.update)
        self.update_btn.place(x=270,y=400,height=40,width=110)

        self.clear_btn = Button(self.root, text="Clear", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.clear)
        self.clear_btn.place(x=390,y=400,height=40,width=110)

        self.delete_btn = Button(self.root, text="Delete", 
                                 font=("goudy old style",15), 
                                 bg = "#07f0b6",fg="black",cursor="hand2",command=self.delete)
        self.delete_btn.place(x=510,y=400,height=40,width=110)


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


        self.posTable=ttk.Treeview(self.pos_frame,columns=("id","name","posts","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.posTable.xview)
        scrolly.config(command=self.posTable.yview)

        self.posTable.heading("id",text="ID")
        self.posTable.heading("name",text="Positons Name")
        self.posTable.heading("posts",text="no. of posts")
        self.posTable.heading("description",text="Description")

        self.posTable["show"]="headings"

        self.posTable.column("id", width=50)
        self.posTable.column("name", width=150)
        self.posTable.column("posts", width=100)
        self.posTable.column("description", width=200)
       

        self.posTable.pack(fill=BOTH,expand=1)
        self.posTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from positions where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.posTable.delete(*self.posTable.get_children())
            for row in rows:
                self.posTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear(self):
        self.show()
        self.var_name.set("")
        self.var_posts.set("")
        self.txt_description.delete('1.0',END)
        self.txt_name.config(state=NORMAL)

    def search_clear(self):
        self.show()
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Position Name required", parent=self.root)
            else:
                cur.execute("Select *  from positions where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select position from list", parent=self.root)
                else: 
                    op=messagebox.askyesno("confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from positions where name=?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Position deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        self.txt_name.config(state='readonly')
        self.txt_name
        r=self.posTable.focus()
        content=self.posTable.item(r)
        row=content["values"]
        self.var_name.set(row[1])
        self.var_posts.set(row[2])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])

    def save(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Position Name required", parent=self.root)
            else:
                cur.execute("Select *  from positions where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Position Name already exist", parent=self.root)
                else: 
                    cur.execute("insert into positions (name,posts,description) values(?,?,?)",(
                        self.var_name.get(),
                        self.var_posts.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Position added sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Position Name required", parent=self.root)
            else:
                cur.execute("select *  from positions where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Position from list", parent=self.root)
                else: 
                    cur.execute("update positions set posts=?, description=? where name=?",(
                        self.var_posts.get(),
                        self.txt_description.get("1.0",END),
                        self.var_name.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Position update sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("Select *  from positions")
            rows=cur.fetchall()
            self.posTable.delete(*self.posTable.get_children())
            for row in rows:
                self.posTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    root.minsize(1250, 600)
    root.maxsize(1250, 600)
    obj = positions(root)
    
    root.mainloop()