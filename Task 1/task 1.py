from tkinter import *

w=Tk()
w.title("To-Do List App")

tasks=[]

def add_task():
    task=entry.get()
    if task!="":
        tasks.append(task)
        lb.insert(END,task)
        entry.delete(0,END)

def delete_task():
    selected=lb.curselection()
    if selected:
        tasks.pop(selected[0])
        lb.delete(selected[0])

def update_task():
    selected=lb.curselection()
    new_text=entry.get()
    if selected and new_text!="":
        tasks[selected[0]]=new_text
        lb.delete(selected[0])
        lb.insert(selected[0],new_text)
        entry.delete(0,END)

def mark_done():
    selected=lb.curselection()
    if selected:
        task=tasks[selected[0]]
        tasks[selected[0]]="✔ "+task
        lb.delete(selected[0])
        lb.insert(selected[0],"✔ "+task)

l=Label(w,text="Enter Task:")
entry=Entry(w,width=40)
lb=Listbox(w,width=50)
b1=Button(w,text="Add",command=add_task)
b2=Button(w,text="Delete",command=delete_task)
b3=Button(w,text="Update",command=update_task)
b4=Button(w,text="Mark as Done",command=mark_done)

l.grid(row=0,column=0,padx=10,pady=10)
entry.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
lb.grid(row=1,column=0,columnspan=4,padx=10,pady=10)
b1.grid(row=2,column=0,padx=10,pady=10)
b2.grid(row=2,column=1,padx=10,pady=10)
b3.grid(row=2,column=2,padx=10,pady=10)
b4.grid(row=2,column=3,padx=10,pady=10)

w.mainloop()
