from tkinter import *
calc=Tk()
calc.config(background="Dark Grey")
calc.title("Calculator")
calc.geometry("500x500")
textin=StringVar()
operator=" "

def clickbut(number):
	global operator
	operator=operator+str(number)
	textin.set(operator)

def equlbut(): 
	global operator
	eq=str(eval(operator))
	textin.set(eq)
	operator=''

def clrbut(): 
	global operator 
	textin.set('')
	operator=''
	e1.insert(0,"0")



a1=Label(calc, text="CALCULATOR", font=("courier", "50"), bg='white', fg="black")
a1.pack()
txt=Entry(calc,font=("Courier", 16,'bold'), textvar=textin, width=30,bd=5, bg="powder blue", fg="black", justify=RIGHT)
txt.pack()
txt.insert(0,"0")
but1=Button(calc, padx=14,pady=14, bd=4, bg="white", command=lambda:clickbut(1), text="1", font=("Courier", 16,'bold'))
but1.place(x=10,y=100)
but2=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(2), text="2", font=("Courier", 16, 'bold'))
but2.place(x=100,y=100)
but3=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(3),text="3", font=("Courier", 16, 'bold'))
but3.place(x=190,y=100)
but4=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(4), text="4", font=("Courier", 16, 'bold'))
but4.place(x=280,y=100)
but5=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(5), text="5", font=("Courier", 16, 'bold'))
but5.place(x=10,y=170)
but6=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(6),text="6", font=("Courier", 16, 'bold'))
but6.place(x=100,y=170)
but7=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(7),text="7", font=("Courier", 16, 'bold'))
but7.place(x=190,y=170)
but8=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(8),text="8", font=("Courier", 16, 'bold'))
but8.place(x=280,y=170)
but9=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(9),text="9", font=("Courier", 16, 'bold'))
but9.place(x=10,y=240)
but0=Button(calc,padx=14, pady=14, bd=4, bg="white", command=lambda:clickbut(0), text="0", font=("Courier", 16, 'bold'))
but0.place(x=100,y=240)
butm=Button(calc,padx=35, pady=14, bd=4, bg="white", command=lambda:clickbut('*'), text="*", font=("Courier", 16, 'bold'))
butm.place(x=370,y=100)
buta=Button(calc,padx=35, pady=14, bd=4, bg="white", command=lambda:clickbut('+'),text="+", font=("Courier", 16, 'bold'))
buta.place(x=370,y=170)
butd=Button(calc,padx=35, pady=14, bd=4, bg="white", command=lambda:clickbut('÷'),text="÷", font=("Courier", 16, 'bold'))
butd.place(x=370,y=240)
buts=Button(calc,padx=35, pady=14, bd=4, bg="white", command=lambda:clickbut('-'), text="-", font=("Courier", 16, 'bold'))
buts.place(x=370,y=310)
butc=Button(calc,padx=30, pady=35, bd=4, bg="white", command=clrbut, text="CE", font=("Courier", 16, 'bold'))
butc.place(x=370,y=380)
bute=Button(calc,padx=60, pady=70, bd=4, bg="white", command=equlbut,text="=", font=("Courier", 16, 'bold'))
bute.place(x=10,y=310)
butdo=Button(calc,padx=60, pady=105, bd=4, bg="white", command=lambda:clickbut('.'), text=".", font=("Courier", 16, 'bold'))
butdo.place(x=190,y=240)


calc.mainloop()