from tkinter import *
from modules import *
import tkinter.messagebox
root=Tk()


class Dashboard():
    def __init__(self,master):
        
        self.master=master
        self.master.geometry('500x300')
        self.master.title('AISx Dashboard')

        #Access AP module
        self.buttonAP=Button(self.master,text="Enter Invoice",command=self.enterInvoice).grid(row=0,column=2)
        #Access AR Module
        self.buttonAR=Button(self.master,text="Create Purchase Order",command=self.enterPurchaseOrder).grid(row=0,column=3)
        #Access GL Module
        self.buttonGL=Button(self.master,text="Go to GL",command=self.gotoGL).grid(row=0,column=4)
        #Access Inventory Module
        self.buttonINV=Button(self.master,text="Inventory Manager",command=self.gotoInventory).grid(row=0,column=5)
        #Access Inquiries Module
        self.buttonINQ=Button(self.master,text="Inquiry Center",command=self.gotoInquiries).grid(row=0,column=6)


    def enterInvoice(self):
        leveltwo=Toplevel(self.master)
        window=apScreen(leveltwo)
    def enterPurchaseOrder(self):
        leveltwo=Toplevel(self.master)
        window=arScreen(leveltwo)
    def gotoGL(self):
        leveltwo=Toplevel(self.master)
        window=glScreen(leveltwo)
    def gotoInventory(self):
        leveltwo=Toplevel(self.master)
        window=invScreen(leveltwo)
    def gotoInquiries(self):
        leveltwo=Toplevel(self.master)
        window=inqScreen(leveltwo)

    def finish(self):
        self.master.destroy()
initDashboard=Dashboard(root)
# def main():
#     root=Tk()
#     initDashboard=Dashboard(root)
#     root.mainloop()
root.mainloop()