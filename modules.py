from tkinter import *
from SystemClasses import invoice, purchaseOrder,customer


class apScreen():
    def __init__(self,master):
        self.amtvar=DoubleVar()
        self.numbervar=StringVar()
        self.datevar=StringVar()
        self.duedatevar=StringVar()
        self.custnamevar=StringVar()
        self.custnumvar=StringVar()
       
        
        
        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Invoice Details')
        
        self.numberlabel=Label(self.master,text='Invoice Number').grid(row=0,column=1)
        self.amtlabel=Label(self.master,text='Invoice Amount').grid(row=1,column=1)
        self.datelabel=Label(self.master,text='Invoice Date (MM/DD/YYY)').grid(row=2,column=1)
        self.duedatelabel=Label(self.master,text='Due Date (MM/DD/YYY)').grid(row=3,column=1)
        self.custnamelabel=Label(self.master,text='Customer Name').grid(row=4,column=1)
        self.custnumlabel=Label(self.master,text='Customer Number').grid(row=5,column=1)
        
        
        self.number=Entry(self.master,textvariable=self.numbervar).grid(row=0,column=2)
        self.amt=Entry(self.master,textvariable=self.amtvar).grid(row=1,column=2)
        self.date=Entry(self.master,textvariable=self.datevar).grid(row=2,column=2)
        self.duedate=Entry(self.master,textvariable=self.duedatevar).grid(row=3,column=2)
        self.custname=Entry(self.master,textvariable=self.custnamevar).grid(row=4,column=2)
        self.custnum=Entry(self.master,textvariable=self.custnumvar).grid(row=5,column=2)
        
        
        self.button1=Button(self.master,text="Save Invoice",command=self.saveInvoice).grid(row=7,columnspan=3)
    
        
    def saveInvoice(self):
        #catch=messagebox.askyesno(self.master,'Are all invoice details correct?')
        invoicedetails=invoice(self.numbervar.get(),self.amtvar.get(),self.datevar.get(),self.custnamevar.get(),self.custnumvar.get(),self.duedatevar.get())
        print(invoicedetails.custname)

class arScreen():
    def __init__(self,master):
        self.itemvar=StringVar()
        self.itemnumvar=StringVar()
        self.unitvar=StringVar()
        self.unitcostvar=DoubleVar()
        self.quantityvar=DoubleVar()
        self.custnamevar=StringVar()
        self.custnumbervar=IntVar()
        self.povar=IntVar()
        
        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Purchase Order Details')

        self.polabel=Label(self.master,text="PO Number").grid(row=0,column=1)
        self.itemlabel=Label(self.master,text='Item Description').grid(row=1,column=1)
        self.itemnumlabel=Label(self.master,text='Item Number').grid(row=2,column=1)
        self.unitlabel=Label(self.master,text='Unit Type').grid(row=3,column=1)
        self.unitcostlabel=Label(self.master,text='Unit Price').grid(row=4,column=1)
        self.quantitylabel=Label(self.master,text='Quantity').grid(row=5,column=1)
        self.custnamelabel=Label(self.master,text='Customer Name').grid(row=6,column=1)
        self.custnumlabel=Label(self.master,text='Customer Number').grid(row=7,column=1)
                
        self.po=Entry(self.master,textvariable=self.povar).grid(row=0,column=2)
        self.item=Entry(self.master,textvariable=self.itemvar).grid(row=1,column=2)
        self.itemnum=Entry(self.master,textvariable=self.itemnumvar).grid(row=2,column=2)
        self.unit=Entry(self.master,textvariable=self.unitvar).grid(row=3,column=2)
        self.unitcost=Entry(self.master,textvariable=self.unitcostvar).grid(row=4,column=2)
        self.quantity=Entry(self.master,textvariable=self.quantityvar).grid(row=5,column=2)
        self.custname=Entry(self.master,textvariable=self.custnamevar).grid(row=6,column=2)
        self.custnum=Entry(self.master,textvariable=self.custnumbervar).grid(row=7,column=2)

        self.button1=Button(self.master,text="Create PO",command=self.createPO).grid(row=8,columnspan=3)
    
        
    def createPO(self):
        #current=purchaseOrder(self.item.get(),self.itemnum.get(),self.quantity.get(),self.unit.get(),self.unitcost.get(),self.po.get())
        current=customer(self.custnamevar.get(),self.custnumbervar.get(),0,0)

        print(current.custname)

class glScreen():
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
