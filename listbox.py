from Tkinter import*
import sqlite3
import string

conn=sqlite3.connect('excel.db')
c=conn.cursor()

root=Tk()

varb1=StringVar()
varb2=StringVar()
varb3=IntVar()

#function changing SQLite value to float
def sql_to_float(result1, result2):
    result1= "%s" %result1
    result1=result1.replace("[(", "").replace(",)]","")
    print result1
    result1=float(result1)

    result2= "%s" %result2
    result2=result2.replace("[(", "").replace(",)]","")
    print result2
    result2=float(result2)
    answer=(result1/result2)*100
    answer=round(answer,3)
    return answer



def get_result():
    
    varb1=var1.get()
    print varb1
    varb2=var2.get()
    print varb2
    varb3=spinbox1.get()
    print varb3
    if varb1=="Pepsico, Inc.":
        print "true"
    else:
        print "false"
    if varb1=="Pepsico, Inc.":
        if varb2=="Current dividend yield":
            if varb3=="2006":
                #result=StringVar()
                result1=c.execute('SELECT "price of stock and dividend for 2006" '
                                 'FROM "food industry" '
                                 'WHERE "Company Name"="Pepsico, Inc (dividend)";').fetchall()
                print result1
                result2=c.execute('SELECT "price of stock and dividend for 2006" '
                                  'FROM "food industry" '
                                  'WHERE "Company Name"="Pepsico, Inc (stock price)";').fetchall()
                print result2
                label1=Label(frame1,text=sql_to_float(result1, result2))
                label1.place(x=830, y=200)
                label2=Label(frame1, text="%").place(x=880, y=200)


            elif varb3=="2007":
                #result=StringVar()
                result1=c.execute('SELECT "price of stock and dividend for 2007" '
                                 'FROM "food industry" '
                                 'WHERE "Company Name"="Pepsico, Inc (dividend)";').fetchall()
                print result1
                result2=c.execute('SELECT "price of stock and dividend for 2007" '
                                  'FROM "food industry" '
                                  'WHERE "Company Name"="Pepsico, Inc (stock price)";').fetchall()
                print result2
                label1=Label(frame1,text=sql_to_float(result1, result2))
                label1.place(x=830, y=200)
                label2=Label(frame1, text="%").place(x=880, y=200)

root.geometry("1700x800")
frame1=Frame(root).place()

backgr_image=PhotoImage(file="C:\Users\Sergey\Documents\CSCI233/skyline.gif")
backgr_label=Label(root, image=backgr_image)
backgr_label.place(x=0,y=0, relwidth=1, relheight=1)

choices1=['Pepsico, Inc.', 'Tyson Foods Inc.', 'Nestle', 'JBS USA' ,
         'Coca-Cola Co.']
var1=StringVar(frame1)
var1.set('Choose a company')
option1=OptionMenu(frame1, var1, *choices1)
option1.place(x=100, y=200)

choices2=['Current dividend yield', 'Capital gain yield', 'Rate of return',
          'Sample variance', 'Standard deviation']

var2=StringVar(frame1)
var2.set('Find yield, return or statistics')
option2=OptionMenu(frame1, var2, *choices2)
option2.place(x=300, y=200)

spinbox1=Spinbox(frame1, from_=2006, to=2016)
spinbox1.place(x=550, y=200)

button1=Button(frame1, text="get result", command=get_result)
button1.place(x=730, y=200)

#label1=Label(frame1,text="your answer is here")
#label1.place(x=830, y=200)



root.mainloop()
