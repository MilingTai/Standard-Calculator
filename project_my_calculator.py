#Subject: Tkinter - calculator
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont



#def Functions 
def calculate():  #calculate and output result.
    result= eval(equl.get())
    equl.set(equl.get()+"=\n"+ str(result))
    
def show(buttonString): #update dispaly sapce.    
    content=equl.get()
    if content=="0":
         content=""
    equl.set(content + buttonString) 
   
def multiple_reverse (buttonString): #update dispaly sapce.    
    content=equl.get()
    if content=="0":
         content=""
    equl.set(1/buttonString )
    
def backspace(): #clear last char
    equl.set(str(equl.get()[:-1]))
    
def clear():  #clear display space, and show 0.
    equl.set("0")

    
#2-4.										
win =tk.Tk()
win.title("Calculator")
win.geometry("340x360") #iphone 8 interface
win.resizable(0,0)
win.iconbitmap(r"apple.ico")


Light_grey="#F5F5F5"
Light_blue="#299bff"
White="#FFFFFF"
Off_white="#FAFAFF"
Label_color="#25265e"

#Use tkFont packages to set font
Font_style=tkFont.Font(family="Yu Gothic bold", size=16)

#Use dict, key-value
digits={
      7:(3,0) ,8:(3,1),9:(3,2),
      4:(4,0) ,5:(4,1),6:(4,2),
      1:(5,0) ,2:(5,1),3:(5,2),
      ".":(6,2)
       }
operations={"/":"÷","*":"×","-":"－","+":"+" } 

#==========================================================
#5.To add window widgets
equl=tk.StringVar()
equl.set(0) #default is 0

#Label - display space.
label1 =tk.Label(win, width=25, height=3, textvariable=equl
             , anchor=tk.SE, justify=tk.RIGHT, relief=tk.SUNKEN,font=Font_style
            ).grid(row=0, column=0, columnspan=4,padx=2, pady=5)

#Buttons - clear/delete
#Use PIL packages
image1 =Image.open("delete.png")   #image sources
img1=ImageTk.PhotoImage(image1.resize((30,24))) #To resize 


btn_CE=tk.Button(win, width=3, text="CE",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=backspace).grid(row=1, column=1, sticky=tk.NSEW)
btn_Clear=tk.Button(win, width=3, text="C",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=clear).grid(row=1, column=2, sticky=tk.NSEW)
btn_DEL=tk.Button(win, width=3, height=20,borderwidth=0, image=img1,bg=Off_white, command=backspace
                 ).grid(row=1, column=3, sticky=tk.NSEW)
#btn_DEL.image=img1

 
#Buttons - Digits
#w1 Use for loop!!
for digit, grid_value in digits.items():
    button=tk.Button(win, width=3,text=str(digit),bg="white",font=Font_style,borderwidth=0, command=lambda x=digit:show(str(x)))
    button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW) #stick to every side

#w2 type for each digits as same thing.
#btn7=tk.Button(win, width=5, text="7", command=lambda:show("7")).grid(row=3, column=0, pady=5)
#....
btn0=tk.Button(win, width=14, text="0",borderwidth=0,bg="white",font=Font_style, command=lambda:show("0")).grid(row=6, column=0, columnspan=2)

#Button - operators
btn_PI=tk.Button(win, width=3, text="%",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=lambda:show("*0.01")).grid(row=1, column=0, sticky=tk.NSEW)
btn_X1=tk.Button(win, width=3, text="1/x",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=lambda:multiple_reverse("1/")).grid(row=2, column=0,sticky=tk.NSEW)
btn_X2=tk.Button(win, width=3, text="x\u00b2",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=lambda:show("**2")).grid(row=2, column=1,sticky=tk.NSEW)
btn_X3=tk.Button(win, width=3, text="\u221ax",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=lambda:show("**0.5")).grid(row=2, column=2, sticky=tk.NSEW)

i=2
for operator,symbol in operations.items(): #.itmes()
    button= tk.Button(win, width=3,text=symbol
             , fg=Label_color, bg=Off_white, font=Font_style,borderwidth=0, command=lambda x=operator :show(x))
    button.grid(row=i, column=3,sticky=tk.NSEW) 
    i+=1    
#btn_DIV=tk.Button(win, width=5, text="\u00f7",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=lambda:show("/")).grid(row=2, column=3, sticky=tk.NSEW)
#btn_MUT=tk.Button(win, width=5, text="\u00d7",borderwidth=0,fg=Label_color,bg=Off_white,font=Font_style, command=lambda:show("*")).grid(row=3, column=3, sticky=tk.NSEW)
btn_EQU=tk.Button(win, width=3, text="=",fg=Label_color,bg=Light_blue,relief="groove",font=Font_style, borderwidth=0,  command=calculate).grid(row=6, column=3,sticky=tk.NSEW)

 
#8.To 進入事件處理迴圈
win.mainloop() 


