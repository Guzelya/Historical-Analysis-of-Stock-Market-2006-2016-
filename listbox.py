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



#function changing SQLite value to float
def sql_to_float(result):
    result= "%s" %result
    result=result.replace("[(", "").replace(",)]","")
    print result
    result=float(result)
    answer=(result)*100
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
                result1="None"
                print result1
            elif varb3=="2007":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2008":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2009":
                #result=StringVar()
                result1="None"
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
                result1="None"
                print result1
            elif varb3=="2007":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2008":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2009":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2010":
                #result=StringVar()
                result1="None"
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
                result1="None"
                print result1
            elif varb3=="2007":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2008":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2009":
                #result=StringVar()
                result1="None"
                print result1
            elif varb3=="2010":
                #result=StringVar()
                result1="None"
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
    #label5 clears previous numbers            
    label5=Label(frame1,text="         ", borderwidth=10).place(x=1000, y=200)           
    if result1=="None":
        label1=Label(frame1, text="None", borderwidth=10)
        label1.place(x=1000, y=200)       
    else:
        label1=Label(frame1,text=sql_to_float(result1), borderwidth=10)
        label1.place(x=1000, y=200)
        label2=Label(frame1, text="%", borderwidth=10)
        label2.place(x=1060, y=200)
            

def get_result1():
    varb1=var1.get()
    print varb1
    varb4=var4.get()
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
    label6=Label(frame1,text="         ", borderwidth=10).place(x=1000, y=300)           
    label3=Label(frame1,text=sql_to_float(result2), borderwidth=10)
    label3.place(x=1000, y=300)
    label4=Label(frame1, text="%", borderwidth=10).place(x=1060, y=300)
    
#download from pexels custom size that coincides with root.geometry()
root.geometry("1700x800")
frame1=Frame(root).place()

backgr_image=PhotoImage(file="/Users/Guzel/Desktop/Final Project/skyline3.gif")
backgr_label=Label(root, image=backgr_image)
backgr_label.place(x=0,y=0, relwidth=1, relheight=1)

choices1=['Pepsico, Inc.', 'Tyson Foods, Inc.', 'Nestle S.A.', 'JBS S.A.', 'The Coca-Cola Company',
          'Anheuser-Busch InBev','General Mills, Inc', 'Conagra Brands, Inc', 'Kellogg Company',
          'Dean Foods Company', 'Hormel Foods Corp', 'Molson Coors Brewing Company', "Pilgrim's Pride Corp",
          "The Hershey's Company", 'Mondelez International, Inc', 'Archer-Daniels-Midland Company',
          'Unilever N.V.', 'Danone', 'Associated British Foods plc', 'Campbell Soup Company']
var1=StringVar(frame1)
var1.set('Choose a company')
option1=OptionMenu(frame1, var1, *choices1)
option1.place(x=100, y=250)

choices2=['Current dividend yield', 'Capital gains yield', 'Rate of return']


var2=StringVar(frame1)
var2.set('choose an option')
option2=OptionMenu(frame1, var2, *choices2)
option2.place(x=300, y=200)

choices3=['current dividend yield','capital gains yield','rate of return']

label7=Label(frame1, text="Sample standard deviation \n for a period of 11 years (2006-2016)")
label7.place(x=300, y=300)

var4=StringVar(frame1)
var4.set("choose an option")
option3=OptionMenu(frame1, var4, *choices3)
option3.place(x=600, y=300)

spinbox1=Spinbox(frame1, from_=2006, to=2016)
spinbox1.place(x=600, y=200)

button1=Button(frame1, text="get result", command=get_result)
button1.place(x=900, y=200)


button2=Button(frame1, text="get result", command=get_result1)
button2.place(x=900, y=300)



#label1=Label(frame1,text="your answer is here")
#label1.place(x=830, y=200)



root.mainloop()
