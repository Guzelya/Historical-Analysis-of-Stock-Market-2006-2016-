from Tkinter import*
import sqlite3
import string

conn=sqlite3.connect('FinalProject.db')
c=conn.cursor()

root=Tk()

varb1=StringVar()
varb2=StringVar()
varb3=IntVar()
varb4=StringVar()
varb5=StringVar()
varb6=StringVar()

root.geometry("1700x800")
frame2=Frame(root).place()

backgr_image=PhotoImage(file="/Users/Guzel/Desktop/Project Done/coins_1.gif")
backgr_label=Label(root, image=backgr_image)
backgr_label.place(x=0,y=0, relwidth=1, relheight=1)

label_1=Label(frame2, text="Class: CSCI233\n Professor: Felix Grezes\n Student: Guzel Kisselev ")
label_1.place(x=10, y=10)

label_2=Label(frame2, text="Historical Analysis of Stock Market\n(over period of 11 years 2006-2016)",
              font="Baskerville 24 bold")
label_2.place(x=550, y=400)

def window_foods():
    #function changing SQLite value to float
    def sql_to_float(result):
        result= "%s" %result
        result=result.replace("[(", "").replace(",)]","")
        print result
        # u'' - is printed out when there is no value in the cell
        if result=="u''":
            return "None"
        else:
            result=float(result)
            answer=(result)*100
            answer=round(answer,3)
            return answer

    def sql_to_float1(number):
        number= "%s" %number
        number=number.replace("[(", "").replace(",)]","")
        print number
        number=float(number)
        number=round(number,3)
        return number
        
    def get_result():       
        varb1=var1.get()
        print varb1
        varb2=var2.get()
        print varb2
        varb3=spinbox1.get()
        print varb3

        if varb1=="Pepsico, Inc.":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                    print result1
                    

        if varb1=="Tyson Foods, Inc.":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Nestle S.A.":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="JBS S.A.":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                    print result1
        
        if varb1=="The Coca-Cola Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Anheuser-Busch InBev":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="General Mills, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                    print result1
        if varb1=="Conagra Brands, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Kellogg Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                    print result1

        if varb1=="Dean Foods Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Hormel Foods Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="Molson Coors Brewing Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                    print result1
        if varb1=="Pilgrim's Pride Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="The Hershey's Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                    print result1
        if varb1=="Mondelez International, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                    print result1

        if varb1=="Archer-Daniels-Midland Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                    print result1

        if varb1=="Unilever N.V.":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                    print result1

        if varb1=="Danone":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                    print result1

        if varb1=="Associated British Foods plc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                    print result1

        if varb1=="Campbell Soup Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "food industryCSV" '
                                     'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                    print result1







        #label5 clears previous numbers            
        label5=Label(frame1,text="         ", font="Baskerville 20 bold").place(x=1230, y=50)
        label1=Label(frame1,text=sql_to_float(result1),font="Baskerville 20 bold")
        label1.place(x=1200, y=50)
        label2=Label(frame1, text="%",font="Baskerville 20 bold")
        label2.place(x=1280, y=50)
        
            
            
    def get_result1():
        varb1=var1.get()
        print varb1
        varb4=var3.get()
        print varb4
        if varb1=="Pepsico, Inc.":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Pepsico Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Pepsico Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Pepsico Inc (rate of return)";').fetchall()
                print result2

        if varb1=="Tyson Foods, Inc.":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Tyson Foods Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Tyson Foods Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Tyson Foods Inc (rate of return)";').fetchall()
                print result2

        if varb1=="Nestle S.A.":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Nestle S.A. (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Nestle S.A. (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Nestle S.A. (rate of return)";').fetchall()
                print result2
        if varb1=="JBS S.A.":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="JBS S.A. (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="JBS S.A. (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="JBS S.A. (rate of return)";').fetchall()
                print result2
        if varb1=="The Coca-Cola Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="The Coca-Cola Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="The Coca-Cola Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="The Coca-Cola Company (rate of return)";').fetchall()
                print result2
        if varb1=="Anheuser-Busch InBev":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Anheuser-Busch InBev (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Anheuser-Busch InBev (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Anheuser-Busch InBev (rate of return)";').fetchall()
                
        if varb1=="General Mills, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="General Mills Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="General Mills Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="General Mills Inc (rate of return)";').fetchall()
                print result2
                
        if varb1=="Conagra Brands, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Conagra Brands Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Conagra Brands Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Conagra Brands Inc (rate of return)";').fetchall()
                print result2
        if varb1=="Kellogg Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Kellogg Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Kellogg Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Kellogg Company (rate of return)";').fetchall()
                print result2
                
        if varb1=="Dean Foods Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Dean Foods Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Dean Foods Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Dean Foods Company (rate of return)";').fetchall()
                print result2
                
        if varb1=="Hormel Foods Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Hormel Foods Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Hormel Foods Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Hormel Foods Corp (rate of return)";').fetchall()
                print result2
        if varb1=="Molson Coors Brewing Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Molson Coors Brewing Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Molson Coors Brewing Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Molson Coors Brewing Company (rate of return)";').fetchall()
                print result2

        if varb1=="Pilgrim's Pride Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Pilgrim\'s Pride Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Pilgrim\'s Pride Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Pilgrim\'s Pride Corp (rate of return)";').fetchall()
                print result2

        if varb1=="The Hershey's Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="The Hershey Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="The Hershey Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="The Hershey Company (rate of return)";').fetchall()
                print result2

        if varb1=="Mondelez International, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Mondelez International Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Mondelez International Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Mondelez International Inc (rate of return)";').fetchall()
                print result2
        if varb1=="Archer-Daniels-Midland Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Archer-Daniels-Midland Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Archer-Daniels-Midland Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Archer-Daniels-Midland Company (rate of return)";').fetchall()
                print result2
        if varb1=="Unilever N.V.":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Unilever N.V. (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Unilever N.V. (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Unilever N.V. (rate of return)";').fetchall()
                print result2

        if varb1=="Danone":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Danone (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Danone (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Danone (rate of return)";').fetchall()
                print result2

        if varb1=="Associated British Foods plc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Associated British Foods plc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Associated British Foods plc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Associated British Foods plc (rate of return)";').fetchall()
                print result2

        if varb1=="Campbell Soup Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Campbell Soup Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Campbell Soup Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "food industryCSV" '
                                 'WHERE "CompanyName"="Campbell Soup Company (rate of return)";').fetchall()
                print result2

                
        label6=Label(frame1,text="         ", font="Baskerville 20 bold").place(x=1250, y=200)        
        label3=Label(frame1,text=sql_to_float(result2),font="Baskerville 20 bold")
        label3.place(x=1200, y=200)
        label8=Label(frame1, text="%",font="Baskerville 20 bold").place(x=1280, y=200)




    def get_result2():
        varb5=var4.get()
        print varb5
        label9=Label(frame1,text="           ", font="Baskerville 20 bold",).place(x=1050, y=400)
        if varb5=="current dividend yield":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average of current dividend yield";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1080, y=400)
            
        elif varb5=="capital gains yield":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average of capital gains yield";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1080, y=400)

            
        elif varb5=="rate of return":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average rate of return";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1080,y=400)
        
        elif varb5=="stock prices":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average of stock prices";').fetchall()
            label7=Label(frame1, text=sql_to_float1(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="   ", font="Baskerville 20 bold").place(x=1080,y=400)
        elif varb5=="dividends":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average of dividends";').fetchall()
            label7=Label(frame1, text=sql_to_float1(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="   ", font="Baskerville 20 bold").place(x=1080,y=400)


    def get_result3():
        varb6=var5.get()
        print varb6
        label9=Label(frame1,text="          ", font="Baskerville 20 bold").place(x=1050, y=600)
        if varb6=="dividend yield on cost":
            result4=c.execute('SELECT dividendyieldoncost '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average rate of return";').fetchall()
            label10=Label(frame1,text=sql_to_float(result4), font="Baskerville 20 bold").place(x=1000, y=600)
        elif varb6=="capital gains yield":
            result4=c.execute('SELECT capitalgainsyieldoverperiodof11years '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average rate of return";').fetchall()
            label10=Label(frame1,text=sql_to_float(result4), font="Baskerville 20 bold").place(x=1000, y=600)
            
        elif varb6=="rate of return":
            result4=c.execute('SELECT rateofreturnover11years '
                              'FROM "food industryCSV" '
                              'WHERE "CompanyName"="average rate of return";').fetchall()        
            label10=Label(frame1,text=sql_to_float(result4), font="Baskerville 20 bold").place(x=1000, y=600)

        label11=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1080,y=600)
        
            


            

    #root.geometry("1700x800")
    #frame1=Frame(root).place()
    frame1=Toplevel(root, height=800, width=1700)

    backgr_image=PhotoImage(file="/Users/Guzel/Desktop/Project Done/corn.gif")
    backgr_label=Label(frame1, image=backgr_image)
    backgr_label.image=backgr_image
    backgr_label.place(x=0,y=0, relwidth=1, relheight=1)

    choices1=['Pepsico, Inc.', 'Tyson Foods, Inc.', 'Nestle S.A.', 'JBS S.A.', 'The Coca-Cola Company',
              'Anheuser-Busch InBev','General Mills, Inc', 'Conagra Brands, Inc', 'Kellogg Company',
              'Dean Foods Company', 'Hormel Foods Corp', 'Molson Coors Brewing Company', "Pilgrim's Pride Corp",
              "The Hershey's Company", 'Mondelez International, Inc', 'Archer-Daniels-Midland Company',
              'Unilever N.V.', 'Danone', 'Associated British Foods plc', 'Campbell Soup Company']
    var1=StringVar(frame1)
    var1.set('Choose a company')
    option1=OptionMenu(frame1, var1, *choices1)
    option1.config(font=("Baskerville bold", (20)))
    option1.place(x=100, y=150)


    choices2=['Current dividend yield', 'Capital gains yield', 'Rate of return']
    var2=StringVar(frame1)
    var2.set('Choose an option')
    option2=OptionMenu(frame1, var2, *choices2)
    option2.config(font=("Baskerville bold", (20)))
    option2.place(x=400, y=50)


    choices3=['current dividend yield','capital gains yield','rate of return']
    label7=Label(frame1, text="Sample standard deviation \n for a period of 11 years ",
                 font="Baskerville 20 bold")
    label7.place(x=400, y=200)
    var3=StringVar(frame1)
    var3.set("Choose an option")
    option3=OptionMenu(frame1, var3, *choices3)
    option3.config(font=("Baskerville bold", (20)))
    option3.place(x=700, y=200)


    spinbox1=Spinbox(frame1, from_=2006, to=2016)
    spinbox1.config(font=("Baskerville bold", (20)))
    spinbox1.place(x=700, y=50)


    button1=Button(frame1, text="get result", font="Baskerville 20 bold", command=get_result)
    button1.place(x=1000, y=50)


    button2=Button(frame1, text="get result", font="Baskerville 20 bold", command=get_result1)
    button2.place(x=1000, y=200)


    AVGlabel=Label(frame1, text="Standard deviation for the whole\n industry over a period of 11 years for ",
                   font="Baskerville 20 bold",)
    AVGlabel.place(x=50, y=400)

    choices4=['stock prices', 'dividends', 'current dividend yield', 'capital gains yield',
              'rate of return']
    var4=StringVar(frame1)
    var4.set("Choose an option")
    option4=OptionMenu(frame1, var4, *choices4)
    option4.config(font=("Baskerville bold", (20)))
    option4.place(x=500, y=400)

    button3=Button(frame1, text="get result", font="Baskerville 20 bold",command=get_result2)
    button3.place(x=800, y=400)

    portfLabel=Label(frame1, text="Imagine you bought one share of each\n company in 2006 and sold in 2016",
                     font="Baskerville 20 bold",)
    portfLabel.place(x=50, y=600)

    choices5=['dividend yield on cost', 'capital gains yield','rate of return']
    var5=StringVar(frame1)
    var5.set("Choose and option")
    option5=OptionMenu(frame1, var5, *choices5)
    option5.config(font=("Baskerville bold", (20)))
    option5.place(x=500, y=600)

    button4=Button(frame1, text="get result", font="Baskerville 20 bold", command=get_result3)
    button4.place(x=800, y=600)


def window_nat():
        #function changing SQLite value to float
    def sql_to_float(result):
        result= "%s" %result
        result=result.replace("[(", "").replace(",)]","")
        print result
        # u'' - is printed out when there is no value in the cell
        if result=="u''":
            return "None"
        else:
            result=float(result)
            answer=(result)*100
            answer=round(answer,3)
            return answer

    def sql_to_float1(number):
        number= "%s" %number
        number=number.replace("[(", "").replace(",)]","")
        print number
        number=float(number)
        number=round(number,3)
        return number
        
        



    def get_result():
        
        varb1=var1.get()
        print varb1
        varb2=var2.get()
        print varb2
        varb3=spinbox1.get()
        print varb3

        if varb1=="Exxon Mobile Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                    print result1
                    

        if varb1=="Chevron Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Marathon Petroleum Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="ConocoPhillips":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                    print result1
        
        if varb1=="Enterprise Bancorp Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Chesapeake Energy Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="The Williams Companies Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                    print result1
        if varb1=="Encana Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="BP plc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                    print result1

        if varb1=="Devon Energy Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Occidental Petroleum Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="EOG Resources Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                    print result1
        if varb1=="Anadarko Petroleum Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="Valero Energy Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="Pioneer Natural Resources Company":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                    print result1

        if varb1=="Apache Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                    print result1

        if varb1=="Hess Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                    print result1

        if varb1=="Continental Resources Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                    print result1

        if varb1=="Royal Dutch Shell plc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                    print result1

        if varb1=="Noble Energy Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "natural resourcesCSV" '
                                     'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                    print result1







        #label5 clears previous numbers            
        label5=Label(frame1,text="         ", font="Baskerville 20 bold").place(x=1230, y=50)
        label1=Label(frame1,text=sql_to_float(result1),font="Baskerville 20 bold")
        label1.place(x=1200, y=50)
        label2=Label(frame1, text="%", font="Baskerville 20 bold")
        label2.place(x=1270, y=50)
        
            
            
    def get_result1():
        varb1=var1.get()
        print varb1
        varb4=var3.get()
        print varb4
        if varb1=="Exxon Mobile Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Exxon Mobile Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Exxon Mobile Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Exxon Mobile Corp (rate of return)";').fetchall()
                print result2

        if varb1=="Chevron Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Chevron Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Chevron Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Chevron Corp (rate of return)";').fetchall()
                print result2

        if varb1=="Marathon Petroleum Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Marathon Petroleum Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Marathon Petroleum Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Marathon Petroleum Corp (rate of return)";').fetchall()
                print result2
        if varb1=="ConocoPhillips":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="ConocoPhillips (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="ConocoPhillips (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="ConocoPhillips (rate of return)";').fetchall()
                print result2
        if varb1=="Enterprise Bancorp Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Enterprise Bancorp Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Enterprise Bancorp Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Enterprise Bancorp Inc (rate of return)";').fetchall()
                print result2
        if varb1=="Chesapeake Energy Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Chesapeake Energy Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Chesapeake Energy Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Chesapeake Energy Corp (rate of return)";').fetchall()
                
        if varb1=="The Williams Companies Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="The Williams Companies Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="The Williams Companies Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="The Williams Companies Inc (rate of return)";').fetchall()
                print result2
                
        if varb1=="Encana Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Encana Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Encana Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Encana Corp (rate of return)";').fetchall()
                print result2
        if varb1=="BP plc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="BP plc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="BP plc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="BP plc (rate of return)";').fetchall()
                print result2
                
        if varb1=="Devon Energy Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Devon Energy Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Devon Energy Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Devon Energy Corp (rate of return)";').fetchall()
                print result2
                
        if varb1=="Occidental Petroleum Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Occidental Petroleum Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Occidental Petroleum Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Occidental Petroleum Corp (rate of return)";').fetchall()
                print result2
        if varb1=="EOG Resources Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="EOG Resources Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="EOG Resources Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="EOG Resources Inc (rate of return)";').fetchall()
                print result2

        if varb1=="Anadarko Petroleum Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Anadarko Petroleum Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Anadarko Petroleum Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Anadarko Petroleum Corp (rate of return)";').fetchall()
                print result2

        if varb1=="Valero Energy Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Valero Energy Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Valero Energy Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Valero Energy Corp (rate of return)";').fetchall()
                print result2

        if varb1=="Pioneer Natural Resources Company":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Pioneer Natural Resources Company (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Pioneer Natural Resources Company (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Pioneer Natural Resources Company (rate of return)";').fetchall()
                print result2
        if varb1=="Apache Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Apache Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Apache Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Apache Corp (rate of return)";').fetchall()
                print result2
        if varb1=="Hess Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Hess Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Hess Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Hess Corp (rate of return)";').fetchall()
                print result2

        if varb1=="Continental Resources Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Continental Resources Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Continental Resources Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Continental Resources Inc (rate of return)";').fetchall()
                print result2

        if varb1=="Royal Dutch Shell plc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Royal Dutch Shell plc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Royal Dutch Shell plc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Royal Dutch Shell plc (rate of return)";').fetchall()
                print result2

        if varb1=="Noble Energy Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Noble Energy Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Noble Energy Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "natural resourcesCSV" '
                                 'WHERE "CompanyName"="Noble Energy Inc (rate of return)";').fetchall()
                print result2

                
        label6=Label(frame1,text="         ", font="Baskerville 20 bold").place(x=1250, y=200)        
        label3=Label(frame1,text=sql_to_float(result2), font="Baskerville 20 bold")
        label3.place(x=1200, y=200)
        label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1270, y=200)




    def get_result2():
        varb5=var4.get()
        print varb5
        label9=Label(frame1,text="           ", font="Baskerville 20 bold").place(x=1030, y=400)
        if varb5=="current dividend yield":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of dividend yield";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1070, y=400)
            
        elif varb5=="capital gains yield":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of capital gains yield";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1070, y=400)

            
        elif varb5=="rate of return":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of rate of return";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1070,y=400)
        
        elif varb5=="stock prices":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of stock prices";').fetchall()
            label7=Label(frame1, text=sql_to_float1(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="   ", font="Baskerville 20 bold").place(x=1070,y=400)
        elif varb5=="dividends":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of dividends";').fetchall()
            label7=Label(frame1, text=sql_to_float1(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="   ", font="Baskerville 20 bold").place(x=1070,y=400)


    def get_result3():
        varb6=var5.get()
        print varb6
        label9=Label(frame1,text="          ", font="Baskerville 20 bold").place(x=1050, y=600)
        if varb6=="dividend yield on cost":
            result4=c.execute('SELECT dividendyieldoncost '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of original prices";').fetchall()
            label10=Label(frame1,text=sql_to_float(result4), font="Baskerville 20 bold").place(x=1000, y=600)
        elif varb6=="capital gains yield":
            result4=c.execute('SELECT capitalgainsyieldoverperiodof11years '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of original prices";').fetchall()
            label10=Label(frame1,text=sql_to_float(result4), font="Baskerville 20 bold").place(x=1000, y=600)
            
        elif varb6=="rate of return":
            result4=c.execute('SELECT rateofreturnoverperiodof11years '
                              'FROM "natural resourcesCSV" '
                              'WHERE "CompanyName"="average of original prices";').fetchall()        
            label10=Label(frame1,text=sql_to_float(result4), font="Baskerville 20 bold").place(x=1000, y=600)

        label11=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1070,y=600)
        
            


            

    #root.geometry("1700x800")
    frame1=Toplevel(root, height=800, width=1700)

    backgr_image=PhotoImage(file="/Users/Guzel/Desktop/Project Done/oil.gif")
    backgr_label=Label(frame1, image=backgr_image)
    backgr_label.image=backgr_image
    backgr_label.place(x=0,y=0, relwidth=1, relheight=1)

    choices1=['Exxon Mobile Corp','Chevron Corp','Marathon Petroleum Corp','ConocoPhillips',
              'Enterprise Bancorp Inc', 'Chesapeake Energy Corp','The Williams Companies Inc',
              'Encana Corp', 'BP plc','Devon Energy Corp','Occidental Petroleum Corp',
              'EOG Resources Inc','Anadarko Petroleum Corp','Valero Energy Corp',
              'Pioneer Natural Resources Company','Apache Corp','Hess Corp',
              'Continental Resources Inc','Royal Dutch Shell plc','Noble Energy Inc']
    var1=StringVar(frame1)
    var1.set('Choose a company')
    option1=OptionMenu(frame1, var1, *choices1)
    option1.config(font=("Baskerville bold", (20)))
    option1.place(x=100, y=150)


    choices2=['Current dividend yield', 'Capital gains yield', 'Rate of return']
    var2=StringVar(frame1)
    var2.set('Choose an option')
    option2=OptionMenu(frame1, var2, *choices2)
    option2.config(font=("Baskerville bold", (20)))
    option2.place(x=400, y=50)


    choices3=['current dividend yield','capital gains yield','rate of return']
    label7=Label(frame1, text="Sample standard deviation \n for a period of 11 years ", font="Baskerville 20 bold")
    label7.place(x=400, y=200)
    var3=StringVar(frame1)
    var3.set("Choose an option")
    option3=OptionMenu(frame1, var3, *choices3)
    option3.config(font=("Baskerville bold", (20)))
    option3.place(x=700, y=200)


    spinbox1=Spinbox(frame1, from_=2006, to=2016)
    spinbox1.config(font=("Baskerville bold", (20)))
    spinbox1.place(x=700, y=50)


    button1=Button(frame1, text="get result", font="Baskerville 20 bold",command=get_result)
    button1.place(x=1000, y=50)


    button2=Button(frame1, text="get result", font="Baskerville 20 bold",command=get_result1)
    button2.place(x=1000, y=200)


    AVGlabel=Label(frame1, text="Standard deviation for the whole\n industry over a period of 11 years for ",
                   font="Baskerville 20 bold" )
    AVGlabel.place(x=50, y=400)

    choices4=['stock prices', 'dividends', 'current dividend yield', 'capital gains yield',
              'rate of return']
    var4=StringVar(frame1)
    var4.set("Choose an option")
    option4=OptionMenu(frame1, var4, *choices4)
    option4.config(font=("Baskerville bold", (20)))
    option4.place(x=500, y=400)

    button3=Button(frame1, text="get result",font="Baskerville 20 bold", command=get_result2)
    button3.place(x=800, y=400)

    portfLabel=Label(frame1, text="Imagine you bought one share of each\n company in 2006 and sold in 2016",
                     font="Baskerville 20 bold")
    portfLabel.place(x=50, y=600)

    choices5=['dividend yield on cost', 'capital gains yield','rate of return']
    var5=StringVar(frame1)
    var5.set("Choose and option")
    option5=OptionMenu(frame1, var5, *choices5)
    option5.config(font=("Baskerville bold", (20)))
    option5.place(x=500, y=600)

    button4=Button(frame1, text="get result",font="Baskerville 20 bold",command=get_result3)
    button4.place(x=800, y=600)


        
def window_tech():
    def sql_to_float(result):
        result= "%s" %result
        result=result.replace("[(", "").replace(",)]","")
        print result
        # u'' - is printed out when there is no value in the cell
        if result=="u''":
            return "None"
        else:
            result=float(result)
            answer=(result)*100
            answer=round(answer,3)
            return answer

    def sql_to_float1(number):
        number= "%s" %number
        number=number.replace("[(", "").replace(",)]","")
        print number
        number=float(number)
        number=round(number,3)
        return number
        
        



    def get_result():
        
        varb1=var1.get()
        print varb1
        varb2=var2.get()
        print varb2
        varb3=spinbox1.get()
        print varb3

        if varb1=="Apple, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                    print result1
                    

        if varb1=="Alphabet, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Microsoft Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="HP, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                    print result1
        
        if varb1=="IBM Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Intel Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Sony Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="Panasonic Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Nintendo Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                    print result1

        if varb1=="NVIDIA Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                    print result1
                    
        if varb1=="Advanced Micro Devices, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                    print result1
        if varb1=="Siemens Aktiengesellschaft":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                    print result1
        if varb1=="Oracle Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="Symantec Corp":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                    print result1
        if varb1=="LG Display Co. Ltd":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                    print result1

        if varb1=="Motorola Solutions, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                    print result1

        if varb1=="Texas Instruments, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                    print result1

        if varb1=="Adobe Systems, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                    print result1

        if varb1=="SAP SE":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                    print result1

        if varb1=="Intuit, Inc":
            if varb2=="Current dividend yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                    print result1                

            #capital gains yield
            if varb2=="Capital gains yield":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                    print result1
            #rate of return
            if varb2=="Rate of return":
                if varb3=="2006":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2006 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2007":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2007 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2008":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2008 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2009":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2009 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2010":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2010 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2011":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2011 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2012":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2012 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2013":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2013 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2014":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2014 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2015":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2015 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1
                elif varb3=="2016":
                    #result=StringVar()
                    result1=c.execute('SELECT priceofstockanddividendfor2016 '
                                     'FROM "technologyCSV" '
                                     'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                    print result1







        #label5 clears previous numbers            
        label5=Label(frame1,text="         ", font="Baskerville 20 bold").place(x=1230, y=50)
        label1=Label(frame1,text=sql_to_float(result1), font="Baskerville 20 bold")
        label1.place(x=1200, y=50)
        label2=Label(frame1, text="%",font="Baskerville 20 bold" )
        label2.place(x=1280, y=50)
        
            
            
    def get_result1():
        varb1=var1.get()
        print varb1
        varb4=var3.get()
        print varb4
        if varb1=="Apple, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Apple Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Apple Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Apple Inc (rate of return)";').fetchall()
                print result2

        if varb1=="Alphabet, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Alphabet Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Alphabet Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Alphabet Inc (rate of return)";').fetchall()
                print result2

        if varb1=="Microsoft Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Microsoft Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Microsoft Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Microsoft Corp (rate of return)";').fetchall()
                print result2
        if varb1=="HP, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="HP Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="HP Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="HP Inc (rate of return)";').fetchall()
                print result2
        if varb1=="IBM Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="IBM Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="IBM Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="IBM Corp (rate of return)";').fetchall()
                print result2
        if varb1=="Intel Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Intel Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Intel Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Intel Corp (rate of return)";').fetchall()
                
        if varb1=="Sony Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Sony Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Sony Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Sony Corp (rate of return)";').fetchall()
                print result2
                
        if varb1=="Panasonic Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Panasonic Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Panasonic Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Panasonic Corp (rate of return)";').fetchall()
                print result2
        if varb1=="Nintendo Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Nintendo Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Nintendo Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Nintendo Corp (rate of return)";').fetchall()
                print result2
                
        if varb1=="NVIDIA Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="NVIDIA Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="NVIDIA Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="NVIDIA Corp (rate of return)";').fetchall()
                print result2
                
        if varb1=="Advanced Micro Devices, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Advanced Micro Devices Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Advanced Micro Devices Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Advanced Micro Devices Inc (rate of return)";').fetchall()
                print result2
        if varb1=="Siemens Aktiengesellschaft":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Siemens Aktiengesellschaft (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Siemens Aktiengesellschaft (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Siemens Aktiengesellschaft (rate of return)";').fetchall()
                print result2

        if varb1=="Oracle Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Oracle Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Oracle Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Oracle Corp (rate of return)";').fetchall()
                print result2

        if varb1=="Symantec Corp":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Symantec Corp (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Symantec Corp (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Symantec Corp (rate of return)";').fetchall()
                print result2

        if varb1=="LG Display Co. Ltd":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="LG Display Co. Ltd (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="LG Display Co. Ltd (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="LG Display Co. Ltd (rate of return)";').fetchall()
                print result2
        if varb1=="Motorola Solutions, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Motorola Solutions Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Motorola Solutions Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Motorola Solutions Inc (rate of return)";').fetchall()
                print result2
        if varb1=="Texas Instruments, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Texas Instruments Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Texas Instruments Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Texas Instruments Inc (rate of return)";').fetchall()
                print result2

        if varb1=="Adobe Systems, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Adobe Systems Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Adobe Systems Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Adobe Systems Inc (rate of return)";').fetchall()
                print result2

        if varb1=="SAP SE":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="SAP SE (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="SAP SE (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="SAP SE (rate of return)";').fetchall()
                print result2

        if varb1=="Intuit, Inc":
            if varb4=="current dividend yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Intuit Inc (current dividend yield)";').fetchall()
                print result2
            if varb4=="capital gains yield":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Intuit Inc (capital gains yield)";').fetchall()
                print result2
            if varb4=="rate of return":
                #result=StringVar()
                result2=c.execute('SELECT standarddeviation '
                                 'FROM "technologyCSV" '
                                 'WHERE "CompanyName"="Intuit Inc (rate of return)";').fetchall()
                print result2

                
        label6=Label(frame1,text="         ", font="Baskerville 20 bold").place(x=1230, y=200)        
        label3=Label(frame1,text=sql_to_float(result2),font="Baskerville 20 bold")
        label3.place(x=1200, y=200)
        label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1280, y=200)




    def get_result2():
        varb5=var4.get()
        print varb5
        label9=Label(frame1,text="           ", font="Baskerville 20 bold").place(x=1040, y=400)
        if varb5=="current dividend yield":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="average of dividend yield";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1070, y=400)
            
        elif varb5=="capital gains yield":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="average of capital gains yield";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1070, y=400)

            
        elif varb5=="rate of return":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="average of rate of return";').fetchall()
            label7=Label(frame1, text=sql_to_float(result3),font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1070,y=400)
        
        elif varb5=="stock prices":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="average of stock prices";').fetchall()
            label7=Label(frame1, text=sql_to_float1(result3), font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="    ", font="Baskerville 20 bold").place(x=1075,y=400)
        elif varb5=="dividends":
            result3=c.execute('SELECT standarddeviation '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="average of dividends";').fetchall()
            label7=Label(frame1, text=sql_to_float1(result3),font="Baskerville 20 bold").place(x=1000, y=400)
            label8=Label(frame1, text="    ", font="Baskerville 20 bold").place(x=1065,y=400)


    def get_result3():
        varb6=var5.get()
        print varb6
        label9=Label(frame1,text="          ", font="Baskerville 20 bold").place(x=1030, y=600)
        if varb6=="dividend yield on cost":
            result4=c.execute('SELECT dividendyieldoncost '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="for separate calculations";').fetchall()
            label10=Label(frame1,text=sql_to_float(result4),font="Baskerville 20 bold").place(x=1000, y=600)
        elif varb6=="capital gains yield":
            result4=c.execute('SELECT capitalgainsyieldoverperiodof11years '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="for separate calculations";').fetchall()
            label10=Label(frame1,text=sql_to_float(result4),font="Baskerville 20 bold").place(x=1000, y=600)
            
        elif varb6=="rate of return":
            result4=c.execute('SELECT rateofreturnover11years '
                              'FROM "technologyCSV" '
                              'WHERE "CompanyName"="for separate calculations";').fetchall()        
            label10=Label(frame1,text=sql_to_float(result4),font="Baskerville 20 bold").place(x=1000, y=600)

        label11=Label(frame1, text="%", font="Baskerville 20 bold").place(x=1080,y=600)
        
            


            

    #root.geometry("1700x800")
    #frame1=Frame(root).place()
    frame1=Toplevel(root, height=800, width=1700)

    backgr_image=PhotoImage(file="/Users/Guzel/Desktop/Project Done/wally.gif")
    backgr_label=Label(frame1, image=backgr_image)
    backgr_label.image=backgr_image
    backgr_label.place(x=0,y=0, relwidth=1, relheight=1)

    choices1=['Apple, Inc', 'Alphabet, Inc', 'Microsoft Corp', 'HP, Inc', 'IBM Corp',
              'Intel Corp','Sony Corp', 'Panasonic Corp', 'Nintendo Corp',
              'NVIDIA Corp', 'Advanced Micro Devices, Inc', 'Siemens Aktiengesellschaft', 'Oracle Corp',
              'Symantec Corp', 'LG Display Co. Ltd', 'Motorola Solutions, Inc',
              'Texas Instruments, Inc', 'Adobe Systems, Inc', 'SAP SE', 'Intuit, Inc']
    var1=StringVar(frame1)
    var1.set('Choose a company')
    option1=OptionMenu(frame1, var1, *choices1)
    option1.place(x=100, y=150)
    option1.config(font=("Baskerville bold", (20)))


    choices2=['Current dividend yield', 'Capital gains yield', 'Rate of return']
    var2=StringVar(frame1)
    var2.set('Choose an option')
    option2=OptionMenu(frame1, var2, *choices2)
    option2.place(x=400, y=50)
    option2.config(font=("Baskerville bold", (20)))


    choices3=['current dividend yield','capital gains yield','rate of return']
    label7=Label(frame1, text="Sample standard deviation \n for a period of 11 years ", font="Baskerville 20 bold")
    label7.place(x=400, y=200)
    var3=StringVar(frame1)
    var3.set("Choose an option")
    option3=OptionMenu(frame1, var3, *choices3)
    option3.place(x=700, y=200)
    option3.config(font=("Baskerville bold", (20)))


    spinbox1=Spinbox(frame1, from_=2006, to=2016, font="Baskerville 20 bold")
    spinbox1.place(x=700, y=50)


    button1=Button(frame1, text="get result", font="Baskerville 20 bold", command=get_result)
    button1.place(x=1000, y=50)


    button2=Button(frame1, text="get result", font="Baskerville 20 bold", command=get_result1)
    button2.place(x=1000, y=200)


    AVGlabel=Label(frame1, text="Standard deviation for the whole\n industry over a period of 11 years for ",
                   font="Baskerville 20 bold")
    AVGlabel.place(x=50, y=400)

    choices4=['stock prices', 'dividends', 'current dividend yield', 'capital gains yield',
              'rate of return']
    var4=StringVar(frame1)
    var4.set("Choose an option")
    option4=OptionMenu(frame1, var4, *choices4)
    option4.place(x=500, y=400)
    option4.config(font=("Baskerville bold", (20)))

    button3=Button(frame1, text="get result",font="Baskerville 20 bold", command=get_result2)
    button3.place(x=800, y=400)

    portfLabel=Label(frame1, text="Imagine you bought one share of each\n company in 2006 and sold in 2016",
                     font="Baskerville 20 bold")
    portfLabel.place(x=50, y=600)

    choices5=['dividend yield on cost', 'capital gains yield','rate of return']
    var5=StringVar(frame1)
    var5.set("Choose and option")
    option5=OptionMenu(frame1, var5, *choices5)
    option5.place(x=500, y=600)
    option5.config(font=("Baskerville bold", (20)))

    button4=Button(frame1, text="get result", font="Baskerville 20 bold", command=get_result3)
    button4.place(x=800, y=600)

    




    
#this function creates a window with three major industries
def new_window():
    frame3=Toplevel(root, height=800, width=1700)
    #frame3.geometry("1700*800")
    #C=Canvas(root, height=800, width=1700)
    backgr_image=PhotoImage(file="/Users/Guzel/Desktop/Project Done/coin_plant.gif")
    backgr_label=Label(frame3, image=backgr_image)
    backgr_label.image=backgr_image
    backgr_label.place(x=0,y=0, relwidth=1, relheight=1)
 
                  
    win_1=Button(frame3, text="FOOD AND BEVERAGE INDUSTRIES",font="Baskerville 20 bold",
                  bg="yellow", command=window_foods).place(x=100, y=100)
        
    win_2=Button(frame3, text="NATURAL RESOURCES INDUSTRIES",font="Baskerville 20 bold",
                  bg="orange", command=window_nat).place(x=100, y=200)

    win_3=Button(frame3, text="TECHNOLOGY",font="Baskerville 20 bold",
                  bg="light pink", command=window_tech).place(x=100, y=300)  

    
    
    
button_1=Button(frame2,text="QUIT", font="Baskerville 20 bold",command=root.destroy)
button_1.place(x=10, y=760)

button_2=Button(frame2, text="NEXT", font="Baskerville 20 bold", command=new_window)
button_2.place(x=1350, y=760)

root.title("Historical Analysis of Stock Market")


root.mainloop()
