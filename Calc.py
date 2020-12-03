#Import from tkinter
from tkinter import* 

#Creates the btnClick function which takes in a number and returns
#that number in operator as a string value and then inputs that number
#into the entry box
def btnClick (numbers):
    global operator
    operator = operator + str(numbers)
    text_Inp.set(operator)

#Creates the btnClear function which makes the operator = ""
#and sets the entry box = operator which clears the entry box.
def btnClear():
    global operator
    operator= ""
    text_Inp.set("")
    
#Creates the btnEquals funciton which takes the str in the entry box
#and converts the str with eval into an operatable equation, then
#evaluates the function, places the answer in the entry box, and clears
#the operator.  
def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Inp.set(sumup)
    operator = ""
    
#sets calc= window
calc = Tk() 

#creates the title of the program in the window
calc.title("Calculator") 

#sets the operator to ""
operator = ""  #sets the operator to ""

#Makes the text_Inp variable a string variable
text_Inp = StringVar() 

#Sets the display area of the calculator
txtDisp = Entry(calc,font=('arial', 20, 'bold'), textvariable =text_Inp, bd=30, insertwidth=4,
                bg = "powder blue", justify = 'right').grid(columnspan=4)

#Creates top row buttons including their functions
btn7=Button(calc,padx=16,bd=8, fg ="black", font=('arial', 20,'bold'),
            text ="7", bg = "powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="8", bg = "powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="9", bg = "powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="+", bg = "powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)
                                               
#Creates the 2nd row buttons including their functions
btn4=Button(calc,padx=16,bd=8, fg ="black", font=('arial', 20,'bold'),
            text ="4", bg = "powder blue",command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="5", bg = "powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="6", bg = "powder blue",command=lambda:btnClick(6)).grid(row=2,column=2)

Subtraction=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="-", bg = "powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)

#Creates the 3rd row buttons including their functions
btn1=Button(calc,padx=16,bd=8, fg ="black", font=('arial', 20,'bold'),
            text ="1", bg = "powder blue",command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="2", bg = "powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="3", bg = "powder blue",command=lambda:btnClick(3)).grid(row=3,column=2)

Multiplication=Button(calc,padx=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="*", bg = "powder blue",command=lambda:btnClick("*")).grid(row=3,column=3)

#Creates the final row of buttons including their functions
btn0=Button(calc,padx=16,pady=16,bd=8, fg ="black", font=('arial', 20,'bold'),
            text ="0", bg = "powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(calc,padx=16,pady=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="C", bg = "powder blue",command=btnClear).grid(row=4,column=1)

btnEquals=Button(calc,padx=16,pady=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="=", bg = "powder blue",command=btnEquals).grid(row=4,column=2)

Division=Button(calc,padx=16,pady=16,bd=8, fg ="black",font=('arial', 20,'bold'),
            text ="/", bg = "powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)  

#Ends the calc.main loop
calc.mainloop() 
