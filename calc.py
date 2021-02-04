'''Can Only perform Operations on only 2 operands at a time'''


from tkinter import *
# import math as m

#if required Import math module

root = Tk()
root.title("GUI CALCULATOR")
root.configure(background="light blue")
# root.geometry("900x800")


def click(n):
    curr = e.get()
    e.delete(0,END) #We specify the INDEX POSITIONS start to stop for deletion 
    #for deleting the entire data of the entry widget use (start --> 0 ; stop --> END)
    e.insert(0,str(curr)+str(n))

def clear():
    e.delete(0,END)

def equal():
    var = e.get()
    my_list=[]
    my_res = 0
    
    if "+" in var:
        my_list=var.split("+")
        for i in range(len(my_list)):
            my_res += float(my_list[i])

    elif "-" in var:
        my_list=var.split("-")
        my_res = float(my_list[0])-float(my_list[1])
    elif "*" in var:
         my_list=var.split("*")
         my_res = float(my_list[0])*float(my_list[1])
    else:
        my_list=var.split("/")
        my_res = float(my_list[0])/float(my_list[1])
    e.delete(0,END)
    e.insert(0,my_res)


def add():
    var = e.get()
    e.delete(0,END)
    e.insert(0,var+"+")


def sub():
    var = e.get()
    e.delete(0,END)
    e.insert(0,var+"-")

def div():
    var = e.get()
    e.delete(0,END)
    e.insert(0,var+"/")

def mul():
    var = e.get()
    e.delete(0,END)
    e.insert(0,var+"*")

def dell():
    var = e.get()
    e.delete(len(var)-1)

def dot():
    var = e.get()
    e.delete(0,END)
    e.insert(0,var+str("."))

e=Entry(root,font='100')
e.grid(row =0 ,column = 0,padx=40,pady=30,columnspan=3)

button1 = Button(root, text=' 1 ',command=lambda: click(1), padx=40 , pady = 20) 
button1.grid(row =1 ,column = 0) 

button2 = Button(root, text=' 2 ',command=lambda: click(2),  padx=40 , pady = 20) 
button2.grid(row =1 ,column = 1) 

button3 = Button(root, text=' 3 ',command=lambda: click(3),  padx=40 , pady = 20) 
button3.grid(row =1 ,column = 2) 

button4 = Button(root, text=' 4 ',command=lambda: click(4),  padx=40 , pady = 20) 
button4.grid(row =2 ,column = 0) 

button5 = Button(root, text=' 5 ',command=lambda: click(5),  padx=40 , pady = 20) 
button5.grid(row =2 ,column = 1) 

button6 = Button(root, text=' 6 ',command=lambda: click(6),  padx=40 , pady = 20) 
button6.grid(row =2 ,column = 2) 

button7 = Button(root, text=' 7 ',command=lambda: click(7),  padx=40 , pady = 20) 
button7.grid(row =3 ,column = 0) 

button8 = Button(root, text=' 8 ',command=lambda: click(8),  padx=40 , pady = 20) 
button8.grid(row =3 ,column = 1) 

button9 = Button(root, text=' 9 ',command=lambda: click(9),  padx=40 , pady = 20) 
button9.grid(row =3 ,column = 2) 

button10 = Button(root, text=' 0 ',command=lambda: click(0),  padx=40 , pady = 20) 
button10.grid(row =4 ,column = 0) 

butt_clear = Button(root, text=' Clear ',command=clear,  padx=80 , pady = 20)
butt_clear.grid(columnspan=3,row=4,column=1)

butt_dot = Button(root,text=".",command = dot,padx=40 , pady = 20)
butt_dot.grid(row=7,column=0)

# 

b_add = Button(text='+',padx=40,pady=20,command=add)
b_add.grid(row =5 ,column = 0)

b_sub = Button(text='-',padx=45,pady=20,command =sub)
b_sub.grid(row =5 ,column = 1)

b_mul = Button(text='*',padx=45,pady=20,command =mul)
b_mul.grid(row =5 ,column = 2)

b_div = Button(text='/',padx=40,pady=20,command =div)
b_div.grid(row =6 ,column = 0)

butt_equal = Button(root,text=" = ",padx=90,pady=20,command=equal)
butt_equal.grid(row =6 ,column = 1,columnspan=2)

butt_del = Button(root,text = "Delete",padx=90,pady=20,command=dell)
butt_del.grid(row =7 ,column = 1,columnspan=2)

root.mainloop()
