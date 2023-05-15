from tkinter import *

root = Tk()
root.title("Classes")
root.geometry("400x400")

name_entry = Entry(root)
name_entry.place(relx=0.5,rely=0.2,anchor=CENTER)

age_entry = Entry(root)
age_entry.place(relx=0.5,rely=0.4,anchor=CENTER)

height_entry = Entry(root)
height_entry.place(relx=0.5,rely=0.6,anchor=CENTER)

mobile_entry = Entry(root)
mobile_entry.place(relx=0.5,rely=0.8,anchor=CENTER)

lbl_name = Label(root)
lbl_name.place(relx=0.5,rely=0.9,anchor=CENTER)

name_get = ""
age_get = ""
height_get = ""
mobile_get = ""

class citizen:
    def __init__(self,name,age,height,mobile):
        self.name = name
        self.age = age
        self.height = height
        self.mobile = mobile
    
    def addCitizen(self):
        
        global name_get
        global age_get
        global height_get
        global mobile_get
        
        name_get = name_entry.get()
        age_get = age_entry.get()
        height_get = height_entry.get()
        mobile_get = mobile_entry.get()
        
        #lbl_name[text]="Name: "+self.name
        print("Name: "+self.name)
        print("Age: "+str(self.age))
        print("Height: "+str(self.height))
        print("Mobile: "+str(self.mobile))
        
        print("Citizen Added")
        

citizen1 = citizen(name_get,age_get,height_get,mobile_get)
citizen1.addCitizen()

root.mainloop()