from tkinter import *
from SystemClasses import invoice, purchaseOrder,customer, code_gen

import sqlite3

#Function to connect to a specified database
def db_connect(file):
    conn=sqlite3.connect(file)
    return(conn)

#Window to enter Invoice details
class apScreen():
    def __init__(self,master):
        #Variable classes for entries
        self.amtvar=DoubleVar()
        self.numbervar=StringVar()
        self.datevar=StringVar()
        self.duedatevar=StringVar()
        self.custnamevar=StringVar()
        self.custnumvar=StringVar()
       
        
        #Geometry, title, and location of window
        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Invoice Details')
        
        #Labels for invoice detail fields
        self.numberlabel=Label(self.master,text='Invoice Number').grid(row=0,column=1)
        self.amtlabel=Label(self.master,text='Invoice Amount').grid(row=1,column=1)
        self.datelabel=Label(self.master,text='Invoice Date (MM/DD/YYYY)').grid(row=2,column=1)
        self.duedatelabel=Label(self.master,text='Due Date (MM/DD/YYYY)').grid(row=3,column=1)
        self.custnamelabel=Label(self.master,text='Customer Name').grid(row=4,column=1)
        self.custnumlabel=Label(self.master,text='Customer Number').grid(row=5,column=1)
        
        #Entry fields for Invoice Details
        self.number=Entry(self.master,textvariable=self.numbervar).grid(row=0,column=2)
        self.amt=Entry(self.master,textvariable=self.amtvar).grid(row=1,column=2)
        self.date=Entry(self.master,textvariable=self.datevar).grid(row=2,column=2)
        self.duedate=Entry(self.master,textvariable=self.duedatevar).grid(row=3,column=2)
        self.custname=Entry(self.master,textvariable=self.custnamevar).grid(row=4,column=2)
        self.custnum=Entry(self.master,textvariable=self.custnumvar).grid(row=5,column=2)
        
        #Button to save invoice, bound to the save invoice function
        self.button1=Button(self.master,text="Save Invoice",command=self.saveInvoice).grid(row=7,columnspan=3)
    
        
    def saveInvoice(self):
        #Connecting to AISyDB..
        conn=db_connect("AISyDB.db")
        
        #Cursor creation
        c=conn.cursor()
        
        #Capturing entries from window into a list to post to db
        invoice=[self.numbervar.get(),self.amtvar.get(),self.datevar.get(),self.custnamevar.get(),self.custnumvar.get(),self.duedatevar.get()]
        
        #SQL commands
        c.execute("INSERT INTO invoices VALUES (?,?,?,?,?,?)",invoice)

        #Commit changes to db
        conn.commit()

        #Close db
        conn.close()
#Window to enter Purchase Order details
class arScreen():
    def __init__(self,master):
        #Variable classes for entries
        self.itemvar=StringVar()
        self.itemnumvar=StringVar()
        self.unitvar=StringVar()
        self.unitcostvar=DoubleVar()
        self.quantityvar=DoubleVar()
        self.custnamevar=StringVar()
        self.custnumbervar=IntVar()
        self.povar=IntVar()
        
        #Geometry, title, and window location
        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Purchase Order Details')

        #Labels for PO details fields
        self.polabel=Label(self.master,text="PO Number").grid(row=0,column=1)
        self.itemlabel=Label(self.master,text='Item Description').grid(row=1,column=1)
        self.itemnumlabel=Label(self.master,text='Item Number').grid(row=2,column=1)
        self.unitlabel=Label(self.master,text='Unit Type').grid(row=3,column=1)
        self.unitcostlabel=Label(self.master,text='Unit Price').grid(row=4,column=1)
        self.quantitylabel=Label(self.master,text='Quantity').grid(row=5,column=1)
        self.custnamelabel=Label(self.master,text='Customer Name').grid(row=6,column=1)
        self.custnumlabel=Label(self.master,text='Customer Number').grid(row=7,column=1)
                
        #Entry fields for PO details
        self.po=Entry(self.master,textvariable=self.povar).grid(row=0,column=2)
        self.item=Entry(self.master,textvariable=self.itemvar).grid(row=1,column=2)
        self.itemnum=Entry(self.master,textvariable=self.itemnumvar).grid(row=2,column=2)
        self.unit=Entry(self.master,textvariable=self.unitvar).grid(row=3,column=2)
        self.unitcost=Entry(self.master,textvariable=self.unitcostvar).grid(row=4,column=2)
        self.quantity=Entry(self.master,textvariable=self.quantityvar).grid(row=5,column=2)
        self.custname=Entry(self.master,textvariable=self.custnamevar).grid(row=6,column=2)
        self.custnum=Entry(self.master,textvariable=self.custnumbervar).grid(row=7,column=2)

        #Button to create PO
        self.button1=Button(self.master,text="Create PO",command=self.create_PO).grid(row=8,columnspan=3)
    
        
    #Function to create the PO in the AISyDB database in table PurchaseOrders
    def create_PO(self):
        #Connecting to AISyDB..
        conn=db_connect("AISyDB.db")
        
        #Cursor creation
        c=conn.cursor()
        
        #Capturing entries from window into a list to post to db
        po=[self.povar.get(),self.itemvar.get(),self.itemnumvar.get(),self.quantityvar.get(),self.unitvar.get(),self.unitcostvar.get()]
        
        #SQL commands
        c.execute("INSERT INTO PurchaseOrders VALUES (?,?,?,?,?,?)",po)

        #Commit changes to db
        conn.commit()

        #Close db
        conn.close()

class glScreen():
    def __init__(self,master):
        #Variables for option menus
        self.accountsvar1=StringVar()
        self.accountsvar2=StringVar()
        self.accountsvar3=StringVar()
        self.accountsvar4=StringVar()

        #Display text for option menus
        self.accountsvar1.set("Select an Account")
        self.accountsvar2.set("Select an Account")
        self.accountsvar3.set("Select an Account")
        self.accountsvar4.set("Select an Account")

        #Window Geometry and title
        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Manual Journal Entry')

        #List of general ledger accounts
        self.accounts={'Cash':100,'Accounts Receivable':101,'Inventory':102,'Property, Plant, and Equipment':103,'Prepaid Assets':104,'Intangible Assets':105,
                      'Accounts Payable':200,'Accrued Expenses':201,'Debt':202,
                       'Retained Earnings':300,
                       'Sales':400,
                       'Cost of Sales':500,'Depreciation and Amortization':501,'Selling and General Administrative':502}

        #Option drop down menus to select accounts
        self.option_menu1=OptionMenu(self.master,self.accountsvar1,*self.accounts.keys()).grid(row=1,column=0)
        self.option_menu2=OptionMenu(self.master,self.accountsvar2,*self.accounts.keys()).grid(row=2,column=0)
        self.option_menu3=OptionMenu(self.master,self.accountsvar3,*self.accounts.keys()).grid(row=3,column=0)
        self.option_menu4=OptionMenu(self.master,self.accountsvar4,*self.accounts.keys()).grid(row=4,column=0)

        #Labels for accounts, debits, credits columns
        self.accountheader=Label(self.master,text="Account").grid(row=0,column=0)
        self.debitsheader=Label(self.master,text="Debits (Enter as Positive Value)").grid(row=0,column=1)
        self.creditsheader=Label(self.master,text="Credits (Enter as Negative Value)").grid(row=0,column=2)

        #Variables for entry fields
        self.debit1var=DoubleVar()
        self.debit2var=DoubleVar()
        self.debit3var=DoubleVar()
        self.debit4var=DoubleVar()

        self.credit1var=DoubleVar()
        self.credit2var=DoubleVar()
        self.credit3var=DoubleVar()
        self.credit4var=DoubleVar()


        #Entry fields for debits and credits
        self.debit1=Entry(self.master,textvariable=self.debit1var).grid(row=1,column=1)
        self.debit2=Entry(self.master,textvariable=self.debit2var).grid(row=2,column=1)
        self.debit3=Entry(self.master,textvariable=self.debit3var).grid(row=3,column=1)
        self.debit4=Entry(self.master,textvariable=self.debit4var).grid(row=4,column=1)

        self.credit1=Entry(self.master,textvariable=self.credit1var).grid(row=1,column=2)
        self.credit2=Entry(self.master,textvariable=self.credit2var).grid(row=2,column=2)
        self.credit3=Entry(self.master,textvariable=self.credit3var).grid(row=3,column=2)
        self.credit4=Entry(self.master,textvariable=self.credit4var).grid(row=4,column=2)

        
        #Button to create JE
        self.button1=Button(self.master,text="Post Journal Entry",command=self.postJE).grid(row=5,columnspan=3)

    def postJE(self):
        self.code=code_gen()
        
        #Netting together credits and debits
        self.net1=self.debit1var.get()+self.credit1var.get()
        self.net2=self.debit2var.get()+self.credit2var.get()
        self.net3=self.debit3var.get()+self.credit3var.get()
        self.net4=self.debit4var.get()+self.credit4var.get()

        self.a1=self.accounts[self.accountsvar1.get()]
        self.a2=self.accounts[self.accountsvar2.get()]
        self.a3=self.accounts[self.accountsvar3.get()]
        self.a4=self.accounts[self.accountsvar4.get()]

        self.values=[self.net1,self.net2,self.net3,self.net4]
        self.accounts_selected=[self.a1,self.a2,self.a3,self.a4]
   
        conn=db_connect("AISyDB.db")
        
        #Cursor creation
        c=conn.cursor()
        #SQL commands
        for x,y in zip(self.values,self.accounts_selected):
            c.execute("INSERT INTO JournalEntries VALUES (?,?,?)",(self.code,y,x))
        

        #Commit changes to db
        conn.commit()

        #Close db
        conn.close()




class invScreen():
    def __init__(self,master):
        self.amtvar=DoubleVar()
        self.numbervar=StringVar()
        self.datevar=StringVar()
        self.duedatevar=StringVar()
        self.custnamevar=StringVar()
        self.custnumvar=StringVar()
        self.currencyvar=StringVar()
        
        
        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Invoice Details')

class inqScreen():
    def __init__(self,master):
        self.documentnumbervar=IntVar()
        self.documentsvar=StringVar()
        

        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Document Number')

        self.documents=["Purchase Order Number","Invoice Number","Journal Entry Number"]

        self.documentsvar.set(self.documents[0])

        self.option_menu=OptionMenu(self.master,self.documentsvar,*self.documents).grid(row=0,column=0)
        self.documentnumber=Entry(self.master,textvariable=self.documentnumbervar).grid(row=0,column=1)

        #Button to create PO
        self.button1=Button(self.master,text="Get Document",command=self.getDoc).grid(row=1,columnspan=2)

    def getDoc(self):
        #Connecting to AISyDB..
        conn=db_connect("AISyDB.db")
        
        #Cursor creation
        c=conn.cursor()
        
        doctype=self.documentsvar.get()
        docnumber=(self.documentnumbervar.get(),)

        print(doctype)
        print(docnumber)

        if doctype=="Purchase Order Number":  
            #SQL commands
            c.execute("SELECT * FROM PurchaseOrders WHERE id=?",docnumber)
            result=c.fetchone()
            if result == None:
                print("Document not found")
            else:
                print(result)
    
            #Close db
            conn.close()

        elif doctype=="Invoice Number":
            c.execute("SELECT * FROM invoices WHERE id=?",docnumber)
            result=c.fetchone()
            if result == None:
                print("Document not found")
            else:
                print(result)
            conn.close()

        elif doctype=="Journal Entry Number":
            c.execute("SELECT * FROM Journal Entries WHERE id=?",docnumber)
            result=c.fetchone()
            if result == None:
                print("Document not found")
            else:
                print(result)
            conn.close()


        

       
