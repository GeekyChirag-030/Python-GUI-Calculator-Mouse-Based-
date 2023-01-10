#!/usr/bin/env python
# coding: utf-8

# In[11]:


from tkinter import *
import tkinter 
from tkinter.messagebox import*



def Add():
    Enter.insert(END,"+")
def Sub():
    Enter.insert(END,"-")
def Mul():
    Enter.insert(END,"*")
def Per():
    Enter.insert(END,"%")
def Div():
    Enter.insert(END,"/")
def One():
    Enter.insert(END,"1")
def Two():
    Enter.insert(END,"2")
def Three():
    Enter.insert(END,"3")
def Four():
    Enter.insert(END,"4")
def Five():
    Enter.insert(END,"5")
def Six():
    Enter.insert(END,"6")
def Seven():
    Enter.insert(END,"7") # This statement will insert the specify the text into the entry box or entry widget when the corresponding text button is clicked
def Eight():
    Enter.insert(END,"8")
def Nine():
    Enter.insert(END,"9")
def Zero():
    Enter.insert(END,"0")

def Dot():
    Enter.insert(END,".")
def Left_Br():
    Enter.insert(END,"(")
def Right_Br():
    Enter.insert(END,")")
def Clear():
    Enter.delete(0,END)
    
def Equal_Solution(Equation): #Recieved Automatically Equation in Equation Variable Equation Without Using the Data.get()  Here Because It is Used inside Entry Widget or with Button Using Lambda 
    
    if Equation=="":
        Enter.delete(0,END)
        showwarning(title=" Warning🚫",message=' Dont Submit the Entry Box Empty ❌')
        Window.destroy()
        pass
    
    Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$^&~;?<>"
    Last=Equation[len(Equation)-1]
    Last_Sec=Equation[len(Equation)-2] #Second Last Character
        
    if Last in "+-*/%#.":
        Enter.delete(0,END)
        showerror(title=' Invalid Attempt❌ ',message='    Invalid Equation ❎  ')
    
    elif Last=='0' and Last_Sec=='/':
        Enter.delete(0,END)
        showerror(title=' Invalid Attempt❌ ',message='    Invalid Equation ❎  ')
    
    elif any(Char in Alphabet for Char in Equation): #Itearte Over Equation and if Any Char That Found in Equation is Also Present in the Alphabet (like : ABCD.....Any ! Symbol) then Eroor is Occured as Invalid Equation
        Enter.delete(0,END)
        showerror(title=' Invalid Attempt❌ ',message='    Invalid Equation ❎  ')
    
    else: #If the Equation is Valid With All Proper Digits and Operators then the Entered Equation is Evaluated and Answer Will be Inserted in The Text Box  Automatically After Submit it Using Press Enter or Click on =
        Answer=eval(Equation)
        Enter.delete(0,END) 
        Enter.insert(END,Answer)


# In[14]:


#New Window Creation 
Window=Tk()

Data=StringVar() #Text Variable or String Varible of the Tkinter for the Entry Widget (Data is Actully the String Varible in Which Entry Widget equation Will Comes or get the Equation of Entry Widget in Data)

#Set window Size With Fixed Position and Also set That It cant be Resizeable 

Window.geometry("615x800+400+100")
Window.resizable(False,False)

#Title for Window and Color of Tkinter Window and set the Icon on Tkinter Window 

Window.title(" ➗ ----------------- Scientific Calculator ----------------- 💰")

Window['bg']="#8B8B83"
Window.iconbitmap("Calculator_Icon.ico")

#Add a Label in Tkinter window and Set on window By Using gemotery manager Grid 
 
L1=Label(Window,text="  Scientific Calculator  ",font=("Times New Roman",45,"bold","italic"),cursor="hand1",fg="black",bg="#FFFFFA",highlightthickness=4,bd=15,relief="ridge",highlightcolor="white")
L1.grid(row=0,column=0,padx=0,pady=15)
#Set Frame Over Tkinter Window 

F2=Frame(Window,bd=20,highlightthickness=9,cursor="hand2",highlightcolor="red",relief="sunken")

#Create the Entry Widget on Window  and Which ahs the Text String Varible Data , wehen Data is Given and Submit in Entry Then It comes in the data String Varible 

Enter=Entry(Window,font=("Arial",30,"bold"),textvariable=Data,highlightthickness=7,bd=9,highlightcolor="black",relief="groove",selectbackground="blue",selectforeground="yellow")

Enter.bind('<Return>',lambda event:Equal_Solution(Data.get())) #This(labmbda) Will Automatically Call the Equal_Solution function with event Argument Also and Data will Provide to the Argument Equation that is Present at the Defination of the Function , Data.get() Automatically Take data in it and Proviide to Equation Argument with the Help of lambda 

#This Code Will Setting the Signs Over the Tkinter Frame F2 like +,-,*,/,% whn Any Of Will Clicked then Corresponding Function will called and That Particular operator or Sign Will Inserted in the Entry Widget 

But_Equal=Button(F2,text=" = ",font=("Times New Roman",30,"bold"),command=lambda :Equal_Solution(Data.get()),highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")
But_Add=Button(F2,text=" + ",font=("Times New Roman",30,"bold"),command=Add,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")
But_Sub=Button(F2,text="  - ",font=("Times New Roman",30,"bold"),command=Sub,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")
But_Mul=Button(F2,text=" x ",font=("Times New Roman",30,"bold"),command=Mul,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")
But_Div=Button(F2,text=" /  ",font=("Times New Roman",30,"bold"),command=Div,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")
But_Per=Button(F2,text="%",font=("Times New Roman",30,"bold"),command=Per,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")
Left_Bracket=Button(F2,text=" (  ",font=("Times New Roman",30,"bold"),command=Left_Br,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")
Right_Bracket=Button(F2,text="  ) ",font=("Times New Roman",30,"bold"),command=Right_Br,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

#This Below Code for Setting the Digits Buttons Over the F2 Frame With Various Types of Customization Also , With Proper Structure , When Here Anyone Button will Clicked then Their Correponding Function Will Called like With 1 is One Function and Which will inserted 1 in entry Widget

But_0=Button(F2,text=" 0 ",font=("Times New Roman",30,"bold"),command=Zero,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_1=Button(F2,text=" 1 ",font=("Times New Roman",30,"bold"),command=One,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_2=Button(F2,text=" 2 ",font=("Times New Roman",30,"bold"),command=Two,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_3=Button(F2,text=" 3 ",font=("Times New Roman",30,"bold"),command=Three,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_4=Button(F2,text=" 4 ",font=("Times New Roman",30,"bold"),command=Four,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_5=Button(F2,text=" 5 ",font=("Times New Roman",30,"bold"),command=Five,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_6=Button(F2,text=" 6 ",font=("Times New Roman",30,"bold"),command=Six,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_7=Button(F2,text=" 7 ",font=("Times New Roman",30,"bold"),command=Seven,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_8=Button(F2,text=" 8 ",font=("Times New Roman",30,"bold"),command=Eight,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

But_9=Button(F2,text=" 9 ",font=("Times New Roman",30,"bold"),command=Nine,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='#FFFFB5',activebackground="green",activeforeground="yellow")

#Code for Setting the Dot and Claer Button on the F2 Frame with Proper Customiuzation. When Any of Will Clicked Then Corresponding Function Will Called Which is Given in with Command Attribute in the Button Function of Tkinter 

But_Clear=Button(F2,text=" C",font=("Times New Roman",30,"bold"),activebackground="green",activeforeground="yellow",command=Clear,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='brown')
But_Dot=Button(F2,text="  . ",font=("Times New Roman",30,"bold"),activebackground="green",activeforeground="yellow",command=Dot,highlightthickness=8,bd=8,highlightcolor='#FFFF69',relief='ridge',bg='brown')

#Packed or Setting All the Things Over Window 
Enter.grid(row=1,column=0)

F2.grid(row=2,column=0,pady=30)

But_Equal.grid(row=0,column=0,padx=1.5,pady=1)   
But_Add.grid(row=0,column=1,padx=1.5,pady=1)
But_Sub.grid(row=0,column=2,padx=1.5,pady=1)
But_Mul.grid(row=0,column=3,padx=1.5,pady=1)
But_Div.grid(row=1,column=0,padx=1.5,pady=1)
But_Per.grid(row=1,column=1,padx=1.5,pady=1)
Left_Bracket.grid(row=1,column=2,padx=1.5,pady=1)
Right_Bracket.grid(row=1,column=3,padx=1.5,pady=1)

But_0.grid(row=2,column=0,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)           
But_1.grid(row=2,column=1,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_2.grid(row=2,column=2,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_3.grid(row=2,column=3,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_4.grid(row=3,column=0,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_5.grid(row=3,column=1,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_6.grid(row=3,column=2,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_7.grid(row=3,column=3,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_8.grid(row=4,column=0,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)
But_9.grid(row=4,column=1,padx=1.5,pady=1)           #Packed or Set The Buttons Over the Frame F2 by Using the Grid Gemotery manager (Actully the Numbers in Sequece is Set or packed Over the Frame)

But_Dot.grid(row=4,column=2,padx=1.5,pady=1)
But_Clear.grid(row=4,column=3,padx=1.5,pady=1)




Window.mainloop() #Display the Window Unitil User will Close It


# In[ ]:




