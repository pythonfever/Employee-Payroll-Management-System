from tkinter import *
root = Tk()
root.geometry("1350x700+0+0")
root.title("Employee Payroll Management System")



# Frame 1-------------------------------------------------------------------------------------------------
f1 = LabelFrame(root)
f1.pack(side=TOP, fill="x")
l = Label(f1, text="Employee Payroll Management System",font=('batang','30'))
l.pack(side=LEFT,anchor="nw")
# Frame 1-------------------------------------------------------------------------------------------------

# Frame 2-------------------------------------------------------------------------------------------------
f2 = LabelFrame(root,width=670,height=630)
f2.place(x=5,y=60)

#Text for our form
ec = Label(f2, text="Employee Code:", borderwidth=6,font = ('Bookman Old Style','20'))
des = Label(f2, text="Designation:", borderwidth=6,font = ('Bookman Old Style','20'))
name = Label(f2, text="Name:", borderwidth=6,font = ('Bookman Old Style','20'))
age = Label(f2, text="Age:",borderwidth=6,font = ('Bookman Old Style','20'))
gender = Label(f2, text="Gender:", borderwidth=6,font = ('Bookman Old Style','20'))
email = Label(f2, text="Email:",borderwidth=6,font = ('Bookman Old Style','20'))
address = Label(f2, text="Address:", borderwidth=6,font = ('Bookman Old Style','20'))
doj = Label(f2, text="D.O.J:", borderwidth=6,font = ('Bookman Old Style','20'))
dob = Label(f2, text="D.O.B:", borderwidth=6,font = ('Bookman Old Style','20'))
expire = Label(f2, text="Experience:", borderwidth=6,font = ('Bookman Old Style','20'))
idp = Label(f2, text="ID Proof:", borderwidth=6,font = ('Bookman Old Style','20'))
contact = Label(f2, text="Contact No.", borderwidth=6,font = ('Bookman Old Style','20'))
date = Label(f2, text="Date:", borderwidth=6,font = ('Bookman Old Style','20'))

#Pack text for our form
ec.place(x=10, y=10)
des.place(x=10, y=70)
name.place(x=10,y=130)
age.place(x=10,y=190)
gender.place(x=10,y=250)
email.place(x=10,y=310)
address.place(x=10,y=370)
expire.place(x=10,y=430)
idp.place(x=10,y=490)
contact.place(x=370,y=190)
doj.place(x=370,y=70)
dob.place(x=370,y=130)
date.place(x=10,y=550)

# Tkinter variable for storing entries
ecvalue = StringVar()
desvalue = StringVar()
namevalue = StringVar()
agevalue = StringVar()
gendervalue = StringVar()
emailvalue = StringVar()
addressvalue = StringVar()
dojvalue = StringVar()
dobvalue = StringVar()
expirevalue = StringVar()
idpvalue = StringVar()
contactvalue = StringVar()
datevalue = StringVar()

#Entries for our form
ecentry = Entry(f2, textvariable=ecvalue,font = ('Bookman Old Style','15'),fg="Black")
desentry = Entry(f2, textvariable=desvalue,font = ('Bookman Old Style','15'),fg="Black")
nameentry = Entry(f2, textvariable=namevalue,font = ('Bookman Old Style','15'),fg="Black")
ageentry = Entry(f2, textvariable=agevalue,font = ('Bookman Old Style','15'),fg="Black")
genderentry = Entry(f2, textvariable=gendervalue,font = ('Bookman Old Style','15'),fg="Black")
emailentry = Entry(f2, textvariable=emailvalue,font = ('Bookman Old Style','15'),fg="Black")
addressentry = Entry(f2, textvariable=addressvalue,font = ('Bookman Old Style','15'),fg="Black")
dojentry = Entry(f2, textvariable=dojvalue,font = ('Bookman Old Style','15'),fg="Black")
dobentry = Entry(f2, textvariable=dobvalue,font = ('Bookman Old Style','15'),fg="Black")
expireentry = Entry(f2, textvariable=expirevalue,font = ('Bookman Old Style','15'),fg="Black")
idpentry = Entry(f2, textvariable=idpvalue,font = ('Bookman Old Style','15'),fg="Black")
contactentry = Entry(f2, textvariable=contactvalue,font = ('Bookman Old Style','15'),fg="Black")
dateentry = Entry(f2, textvariable=datevalue,font = ('Bookman Old Style','15'),fg="Black")

# Packing the Entries
ecentry.place(x=250 ,y=10,width=400,height=40)
desentry.place(x=200,y=70,width=160,height=40)
nameentry.place(x=120,y=130,width=240,height=40)
ageentry.place(x=90,y=190,width=250,height=40)
genderentry.place(x=130,y=250,width=240,height=40)
emailentry.place(x=130,y=310,width=490,height=40)
addressentry.place(x=130,y=370,width=490,height=40)
expireentry.place(x=180,y=430,width=200,height=40)
idpentry.place(x=150,y=490,width=200,height=40)
contactentry.place(x=400,y=250,width=250,height=40)
dojentry.place(x=470,y=70,height=40)
dobentry.place(x=470,y=130,height=40)
dateentry.place(x=100,y=550,height=40)
# Frame 2-------------------------------------------------------------------------------------------------

# Frame 3-------------------------------------------------------------------------------------------------
f3 = LabelFrame(root,width=670,height=630)
f3.place(x=690,y=60)

month = Label(f3, text="Month:", borderwidth=6,font = ('Bookman Old Style','20'))
year = Label(f3, text="Year:", borderwidth=6,font = ('Bookman Old Style','20'))
bsalary = Label(f3, text="Basic Salary:", borderwidth=6,font = ('Bookman Old Style','20'))
day = Label(f3, text="Total days:", borderwidth=6,font = ('Bookman Old Style','20'))
absent = Label(f3, text="Absents:", borderwidth=6,font = ('Bookman Old Style','20'))
medical = Label(f3, text="Medical:", borderwidth=6,font = ('Bookman Old Style','20'))
pf = Label(f3, text="Provident Fund:", borderwidth=6,font = ('Bookman Old Style','20'))
convence = Label(f3, text="Convence:", borderwidth=6,font = ('Bookman Old Style','20'))
nsalary = Label(f3, text="Net Salary:", borderwidth=6,font = ('Bookman Old Style','20'))

month.place(x=10, y=10)
year.place(x=270, y=10)
bsalary.place(x=10, y=50)
day.place(x=350, y=50)
absent.place(x=10, y=110)
medical.place(x=300, y=110)
pf.place(x=10, y=150)
convence.place(x=380, y=150)
nsalary.place(x=10, y=200)

monthvalue = StringVar()
yearvalue = StringVar()
bsalaryvalue = StringVar()
dayvalue = StringVar()
absentvalue = StringVar()
medicalvalue = StringVar()
pfvalue = StringVar()
convencevalue = StringVar()
nsalaryvalue = StringVar()

monthentry = Entry(f3, textvariable=monthvalue,font = ('Bookman Old Style','15'),fg="Black")
yearentry = Entry(f3, textvariable=yearvalue,font = ('Bookman Old Style','15'),fg="Black")
bsalaryentry = Entry(f3, textvariable=bsalaryvalue,font = ('Bookman Old Style','15'),fg="Black")
dayentry = Entry(f3, textvariable=dayvalue,font = ('Bookman Old Style','15'),fg="Black")
absententry = Entry(f3, textvariable=absentvalue,font = ('Bookman Old Style','15'),fg="Black")
medicalentry = Entry(f3, textvariable=medicalvalue,font = ('Bookman Old Style','15'),fg="Black")
pfentry = Entry(f3, textvariable=pfvalue,font = ('Bookman Old Style','15'),fg="Black")
convenceentry = Entry(f3, textvariable=convencevalue,font = ('Bookman Old Style','15'),fg="Black")
nsalaryentry = Entry(f3, textvariable=nsalaryvalue,font = ('Bookman Old Style','15'),fg="Black")

monthentry.place(x=115 ,y=10,width=150,height=40)
yearentry.place(x=350 ,y=10,width=150,height=40)
bsalaryentry.place(x=200 ,y=60,width=150,height=40)
dayentry.place(x=505 ,y=60,width=150,height=40)
absententry.place(x=150 ,y=110,width=150,height=40)
medicalentry.place(x=430 ,y=110,width=200,height=40)
pfentry.place(x=230 ,y=160,width=150,height=40)
convenceentry.place(x=524 ,y=160,width=140,height=40)
nsalaryentry.place(x=180 ,y=210,width=200,height=40)

def save():
    with open(f"{namevalue.get()}.txt",'a') as f:
        f.write(f"Salary reciept of Python is Best Pvt. Ltd.\n\nName:\t\t{namevalue.get()}\nSalary:\t\t{nsalaryvalue.get()}\nDate:\t\t{datevalue.get()}\nDesignation:\t\t{desvalue.get()}\nAge:\t\t{agevalue.get()}\nGender:\t\t{gendervalue.get()}\nContact Number:\t\t{contactvalue.get()}\nMonth:\t\t{monthvalue.get()}")
        f.write(f"\nEmployee Code\t\t {ecvalue.get()}\nD.O.B\t\t{dobvalue.get()}\nE-mail\t\t{emailvalue.get()}\nID Proof{idpvalue.get()}\n")
        f.close

def show():
    a = f"Salary reciept of Nakoda Enterprise Pvt. Ltd.\n\nName:\t\t{namevalue.get()}\nSalary:\t\t{nsalaryvalue.get()}\nDate:\t\t{datevalue.get()}\nDesignation:\t\t{desvalue.get()}\nAge:\t\t{agevalue.get()}\nGender:\t\t{gendervalue.get()}\nContact Number:\t\t{contactvalue.get()}\nMonth:\t\t{monthvalue.get()}"
    reciept= Label(f4,text=a,bg="white", borderwidth=6,font = ('Batang','11'),justify=LEFT)
    reciept.place(x=10,y=50,width=300,height=250)

b2 = Button(f3,text="Show Reciept",font=('batang','20'),command=show)
b2.place(x=10,y=260,height=50) 

b3 = Button(f3,text="Save",font=('batang','20'),command=save)
b3.place(x=220,y=260,height=50)

def clear():
    ecvalue.set("")
    desvalue.set("")
    namevalue.set("")
    agevalue.set("")
    gendervalue.set("")
    emailvalue.set("")
    addressvalue.set("")
    dojvalue.set("")
    dobvalue.set("")
    expirevalue.set("")
    idpvalue.set("")
    contactvalue.set("")
    datevalue.set("")
    monthvalue.set("")
    yearvalue.set("")
    bsalaryvalue.set("")
    dayvalue.set("")
    absentvalue.set("")
    medicalvalue.set("")
    pfvalue.set("")
    convencevalue.set("")
    nsalaryvalue.set("")

b4 = Button(f3,text="Clear",font=('batang','20'),command=clear)
b4.place(x=320,y=260,height=50) 
# Frame 3-------------------------------------------------------------------------------------------------

# Frame 4-------------------------------------------------------------------------------------------------
f4 = LabelFrame(f3,width=335,height=315)
f4.place(x=335,y=315)

sr = Label(f4, text="Salary Reciept", borderwidth=6,font = ('Bookman Old Style','20'))
sr.place(x=50,y=0)


# Frame 4-------------------------------------------------------------------------------------------------

# Frame 5-------------------------------------------------------------------------------------------------
f5 = LabelFrame(f3,width=335,height=315)
f5.place(x=0,y=315)
equation = StringVar()
expression_field = Entry(f5, textvariable=equation,font=('Bookman Old Style','50')) 
expression_field.place(x=0,y=0,width=330,height=90)
expression = "" 

def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 
def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "0" 
    except:
        equation.set(" error ") 
        expression = "0" 

def clear2(): 
    global expression 
    expression = "" 
    equation.set("0")


button1 = Button(f5, text=' 1 ', fg='black', command=lambda: press(1), height=2, width=10) 
button1.place(x=0,y=100)
  
button2 = Button(f5, text=' 2 ', fg='black', command=lambda: press(2), height=2, width=10) 
button2.place(x=83,y=100)
  
button3 = Button(f5, text=' 3 ', fg='black', command=lambda: press(3), height=2, width=10) 
button3.place(x=166,y=100) 
  
button4 = Button(f5, text=' 4 ', fg='black', command=lambda: press(4), height=2, width=10) 
button4.place(x=0,y=140)
  
button5 = Button(f5, text=' 5 ', fg='black',command=lambda: press(5), height=2, width=10) 
button5.place(x=83,y=140)

button6 = Button(f5, text=' 6 ', fg='black', command=lambda: press(6), height=2, width=10) 
button6.place(x=166,y=140)

button7 = Button(f5, text=' 7 ', fg='black', command=lambda: press(7), height=2, width=10) 
button7.place(x=0,y=180) 
  
button8 = Button(f5, text=' 8 ', fg='black', command=lambda: press(8), height=2, width=10) 
button8.place(x=83,y=180)
  
button9 = Button(f5, text=' 9 ', fg='black', command=lambda: press(9), height=2, width=10) 
button9.place(x=166,y=180)
  
button0 = Button(f5, text=' 0 ', fg='black', command=lambda: press(0), height=2, width=10) 
button0.place(x=0,y=220) 
  
plus = Button(f5, text=' + ', fg='black', command=lambda: press("+"), height=2, width=10) 
plus.place(x=250,y=100)
  
minus = Button(f5, text=' - ', fg='black',  command=lambda: press("-"), height=2, width=10) 
minus.place(x=250,y=140)
  
multiply = Button(f5, text=' * ', fg='black',  command=lambda: press("*"), height=2, width=10) 
multiply.place(x=250,y=180) 
 
divide = Button(f5, text=' / ', fg='black', command=lambda: press("/"), height=2, width=10) 
divide.place(x=250,y=220)
  
equal = Button(f5, text=' = ', fg='black', command=equalpress, height=2, width=10) 
equal.place(x=166,y=220)
  
decimal = Button(f5, text='.', fg='black', command=lambda: press('.'), height=2, width=10) 
decimal.place(x=83,y=220)
  
clear= Button(f5, text='Clear', fg='black', command=clear2, height=2, width=46) 
clear.place(x=0,y=260)
# Frame 5-------------------------------------------------------------------------------------------------
root.mainloop()
