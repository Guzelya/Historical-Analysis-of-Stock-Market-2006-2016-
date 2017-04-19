from Tkinter import*
import sqlite3
import string

conn=sqlite3.connect('test.db')
c=conn.cursor()


root=Tk()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()


frame=Frame(root)
frame.grid()

label_1=Label(frame, text="Class: CSCI233")
#label_1.pack(side=TOP)
label_1.grid(row=0, sticky=W)
label_2=Label(frame, text="Professor: Felix Grezes")
#label_2.pack(side=TOP)
label_2.grid(row=1, sticky=W)
label_3=Label(frame, text="Student: Guzel Kisselev")
label_3.grid(row=2, sticky=W)
#label_3.pack(side=TOP)

pic=PhotoImage(file="C:\Users\Sergey\Documents\CSCI233/bear_bull.gif")
label_6=Label(frame, compound=CENTER,
              text="Historical Analysis of Stock Market\n(over perios of 10 years 2007-2017)",
              font="Baskerville 24 bold", image=pic)
label_6.grid()

#function changing SQLite value to float
def sql_to_float(number):
    numberStr= "%s" %number
    numberStr1=numberStr.replace("[(", "").replace(",)]","")
    print numberStr1
    numberFloat=float(numberStr1)
    numberFloat=round(numberFloat,3)
    return numberFloat

    
#now we program buttons

    


#this function opens into food industry
def window_foods():
    
    frame=Toplevel(root, bg="yellow")


    def show_result_food():
        
        answer={0:"Value from SQL database1", 1:"Value from SQL database2", 2:"Value from SQL database3",
                3:"Value from SQL database4", 4:"Value from SQL database5", 5:"Value from SQL database6",
                6: "Value from SQL database7"}
        if var1.get()==1:
            #number=" %s" % answer[0]
            number=c.execute("SELECT avg(Dividend_end/PriceOfShare_beg)*100 "
                             "FROM Food_Industry;").fetchall()
            #numberStr=str(number)
            #numberStr= "%s" %number
            #numberStr1=numberStr.replace("[(", "").replace(",)]","")
            #numberStr1=numberStr1[:4]+"%"
            #print numberStr1
            #numberFloat=float(numberStr1)
            #numberFloat=round(numberFloat,2)
            result=Label(frame,text=sql_to_float(number), bg="light sky blue")
            result.grid(row=0, column=1)
        if var2.get()==1:
            number=c.execute("SELECT avg((PriceOfShareEnd-PriceOfShare_beg)/"
                             "PriceOfShare_beg)*100 FROM Food_Industry;").fetchall()
            #number=" %s" % answer[1]
            result=Label(frame,text=sql_to_float(number), bg="light sky blue")
            result.grid(row=1, column=1)
        if var3.get()==1:
            #number=" %s" % answer[2]
            number=c.execute("SELECT avg((Dividend_end+PriceOfShareEnd-PriceOfShare_beg)"
                             "/PriceOfShare_beg)*100 FROM Food_Industry;").fetchall()
            result=Label(frame,text=sql_to_float(number), bg="light sky blue")
            result.grid(row=2, column=1)
        if var4.get()==1:
            number=" %s" % answer[3]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=3, column=1)
        if var5.get()==1:
            number=" %s" % answer[4]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=4, column=1)
        if var6.get()==1:
            number=" %s" % answer[5]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=5, column=1)
        if var7.get()==1:
            number=" %s" % answer[6]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=6, column=1)

    checkbox_1=Checkbutton(frame, text="Dividend Yield(%)\n on cost", variable=var1, bg="plum",
                           command=show_result_food).grid(row=0,column=0, sticky=W)
    checkbox_2=Checkbutton(frame, text="Capital Gain Yield(%)", variable=var2, bg="plum",
                           command=show_result_food).grid(row=1,column=0, sticky=W)
    checkbox_3=Checkbutton(frame, text="Rate of Return(%)", variable=var3, bg="plum",
                           command=show_result_food).grid(row=2,column=0, sticky=W)
    checkbox_4=Checkbutton(frame, text="Deviation", variable=var4, bg="plum",
                           command=show_result_food).grid(row=3,column=0, sticky=W)
    checkbox_5=Checkbutton(frame, text="Variance", variable=var5, bg="plum",
                           command=show_result_food).grid(row=4,column=0, sticky=W)
    checkbox_6=Checkbutton(frame, text="Sample Variance\n of the whole industry",
                           variable=var6, bg="plum",
                           command=show_result_food).grid(row=5,column=0, sticky=W)
    checkbox_7=Checkbutton(frame, text="Standard Deviation", variable=var7, bg="plum",
                           command=show_result_food).grid(row=6,column=0, sticky=W)

    
    
    #pic_2=PhotoImage(file="C:\Users\Sergey\Documents\CSCI233/pic_2.gif")
    
    #food_1=Label(frame_2,compound=CENTER, image=pic_2, text="decide what you want to do",
                 #font="Baskerville 26 bold", fg="magenta")
    #food_1.pic_2=pic_2
    #food_1.grid()

#this function opens into natural resources industry
def window_nat():
    
    frame=Toplevel(root, bg="yellow")


    def show_result_nat():
        answer={0:"Value from SQL database1", 1:"Value from SQL database2", 2:"Value from SQL database3",
                3:"Value from SQL database4", 4:"Value from SQL database5", 5:"Value from SQL database6",
                6: "Value from SQL database7"}
        if var1.get()==1:
            number=" %s" % answer[0]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=0, column=1)
        if var2.get()==1:
            number=" %s" % answer[1]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=1, column=1)
        if var3.get()==1:
            number=" %s" % answer[2]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=2, column=1)
        if var4.get()==1:
            number=" %s" % answer[3]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=3, column=1)
        if var5.get()==1:
            number=" %s" % answer[4]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=4, column=1)
        if var6.get()==1:
            number=" %s" % answer[5]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=5, column=1)
        if var7.get()==1:
            number=" %s" % answer[6]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=6, column=1)

    checkbox_1=Checkbutton(frame, text="Dividend Yield", variable=var1, bg="plum",
                           command=show_result_nat).grid(row=0,column=0, sticky=W)
    checkbox_2=Checkbutton(frame, text="Capital Gain Yield", variable=var2, bg="plum",
                           command=show_result_nat).grid(row=1,column=0, sticky=W)
    checkbox_3=Checkbutton(frame, text="Rate of Return", variable=var3, bg="plum",
                           command=show_result_nat).grid(row=2,column=0, sticky=W)
    checkbox_4=Checkbutton(frame, text="Deviation", variable=var4, bg="plum",
                           command=show_result_nat).grid(row=3,column=0, sticky=W)
    checkbox_5=Checkbutton(frame, text="Variance", variable=var5, bg="plum",
                           command=show_result_nat).grid(row=4,column=0, sticky=W)
    checkbox_6=Checkbutton(frame, text="Sample Variance\n of the whole industry",
                           variable=var6, bg="plum",
                           command=show_result_nat).grid(row=5,column=0, sticky=W)
    checkbox_7=Checkbutton(frame, text="Standard Deviation", variable=var7, bg="plum",
                           command=show_result_nat).grid(row=6,column=0, sticky=W)
    
    
    #pic_3=PhotoImage(file="C:\Users\Sergey\Documents\CSCI233/nat2.gif")
    
    #nat_res=Label(frame_3,compound=CENTER, image=pic_3, text="decide what you want to do",
                 #font="Baskerville 26 bold", fg="green", width=800, height=250)
    #nat_res.pic_3=pic_3
    #nat_res.grid()



#this function opens into technological industry
def window_tech():
    
    frame=Toplevel(root, bg="yellow")


    def show_result_tech():
        answer={0:"Value from SQL database1", 1:"Value from SQL database2", 2:"Value from SQL database3",
                3:"Value from SQL database4", 4:"Value from SQL database5", 5:"Value from SQL database6",
                6: "Value from SQL database7"}
        if var1.get()==1:
            number=" %s" % answer[0]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=0, column=1)
        if var2.get()==1:
            number=" %s" % answer[1]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=1, column=1)
        if var3.get()==1:
            number=" %s" % answer[2]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=2, column=1)
        if var4.get()==1:
            number=" %s" % answer[3]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=3, column=1)
        if var5.get()==1:
            number=" %s" % answer[4]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=4, column=1)
        if var6.get()==1:
            number=" %s" % answer[5]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=5, column=1)
        if var7.get()==1:
            number=" %s" % answer[6]
            result=Label(frame,text=number, bg="light sky blue")
            result.grid(row=6, column=1)

    checkbox_1=Checkbutton(frame, text="Dividend Yield", variable=var1, bg="plum",
                           command=show_result_tech).grid(row=0,column=0, sticky=W)
    checkbox_2=Checkbutton(frame, text="Capital Gain Yield", variable=var2, bg="plum",
                           command=show_result_tech).grid(row=1,column=0, sticky=W)
    checkbox_3=Checkbutton(frame, text="Rate of Return", variable=var3, bg="plum",
                           command=show_result_tech).grid(row=2,column=0, sticky=W)
    checkbox_4=Checkbutton(frame, text="Deviation", variable=var4, bg="plum",
                           command=show_result_tech).grid(row=3,column=0, sticky=W)
    checkbox_5=Checkbutton(frame, text="Variance", variable=var5, bg="plum",
                           command=show_result_tech).grid(row=4,column=0, sticky=W)
    checkbox_6=Checkbutton(frame, text="Sample Variance\n of the whole industry",
                           variable=var6, bg="plum",
                           command=show_result_tech).grid(row=5,column=0, sticky=W)
    checkbox_7=Checkbutton(frame, text="Standard Deviation", variable=var7, bg="plum",
                           command=show_result_tech).grid(row=6,column=0, sticky=W)

    
#this function creates a window with three major industries
def new_window():
    frame_1=Toplevel(root, bg="gold")
    frame_1.grid()
                  
    win_1=Button(frame_1, text="FOOD AND BEVERAGE INDUSTRIES",font="Baskerville 16 bold",
                 width=50, bg="yellow", command=window_foods)
    win_1.grid(row=0)
    
    win_2=Button(frame_1, text="NATURAL RESOURCES INDUSTRIES",font="Baskerville 16 bold",
                 width=50,bg="orange", command=window_nat)
    win_2.grid(row=1)
    
    win_3=Button(frame_1, text="TECHNOLOGY",font="Baskerville 16 bold",width=50,
                 bg="light pink", command=window_tech)
    win_3.grid(row=2)
    
    food_logos=PhotoImage(file="C:\Users\Sergey\Documents\CSCI233/food_logos.gif")
    label=Label(frame_1, compound=CENTER,image=food_logos, width=800, height=250, bg="gold")
    label.food_logos=food_logos
    label.grid()
    
    
    
button_1=Button(frame,text="QUIT", command=root.destroy)
button_1.grid(row=4, sticky=W)

button_2=Button(frame, text="NEXT", command=new_window)
button_2.grid(row=4, sticky=E)

root.title("Historical Analysis of Stock Market")



conn.commit()
#c.close()
#conn.close()



root.mainloop()
