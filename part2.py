import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import OptionMenu

pizza= Tk()
pizza.geometry("600x500")
pizza.title('Pizza ordering app')

#name and address labels
name_label = Label(pizza, text="What is your name?")
name_label.grid(row=0,column=0)

name_entry=Entry(pizza, width=30)
name_entry.grid(row=0, column=1)


address_label = Label(pizza, text="What is your address?")
address_label.grid(row=2,column=0)

address_entry=Entry(pizza, width=30)
address_entry.grid(row=2, column=1)



number_label = Label(pizza, text="What is your phone number?")
number_label.grid(row=3,column=0)

number_entry=Entry(pizza, width=30)
number_entry.grid(row=3, column=1)





#pizza list
my_pizza_list=["pepperoni","sausage","chicken","bacon","cheese","green peppers", "olives","mushroom","bannana peppers","onions","pinaple","jalapinos"]

pizza_list=Listbox(pizza, selectmode=MULTIPLE, bg="black", fg="white")
pizza_list.grid(row=4,column=1)


for item in my_pizza_list:
    pizza_list.insert(0,item)

#Buttons
def add_pizza():
    result=""
    for item in pizza_list.curselection():
        result=result+str(pizza_list.get(item))+"\n"

        add_lbl.config(text="Your pizza is as shown:"+"\n"+result)

add_lbl=Label(pizza, text="")
add_lbl.grid(row=5, column=1)



#functions of buttons
def check():
    text1= name_entry.get()
    new_lbl= Label(pizza, text="Name:"+text1)
    new_lbl.grid(row=5, column=2)

    text2= address_entry.get()
    new_lbl2=Label(pizza, text="Address:"+text2)
    new_lbl2.grid(row=6, column=2)

    text3= number_entry.get()
    new_lbl3= Label(pizza, text="phone number:"+ text3)
    new_lbl3.grid(row=7, column=2)

#physical buttons
check_button= Button(pizza, text="checkout", command=check)
check_button.grid(row=6, column=0)

def deleteme():
    pizza_list.delete(0,5)


del_button= Button(pizza, text="delete pizza", command=deleteme)
del_button.grid(row=7, column=0)

#Drinks drop down menu

drinks= StringVar()
drinks.set("choose a drink")

drink= OptionMenu(pizza, drinks, "coke", "diet coke", "sprite", "red cream soda", "fruit punch", "water")

drink.grid(row=8, column=0)
#pictures inserted using tk
pizza_picture= ImageTk.PhotoImage(Image.open("pizzaman.jpg"))
pic_lbl=Label(pizza, image=pizza_picture)

pic_lbl.grid(row=10, column=1)

pizza_picture2= ImageTk.PhotoImage(Image.open("pizzadude.jpg"))
pic_lbl=Label(pizza, image=pizza_picture2)

pic_lbl.grid(row=4, column=10)

pizza.mainloop()
