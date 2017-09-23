purchaseorders=[10,11,12]
invoices=[7,8,9]
jes={20:"X",21:"Y",22:"Z"}

def inquire(dropdown,entry):
    doctype=dropdown
    docnumber=entry
    if doctype==1 and docnumber in purchaseorders:
        #This will have to be a function to look into the database of POs
        #SQL query to look up entry
        po="Purchase Order"
        return(po)
    elif doctype==2 and docnumber in invoices:
        #This will have to be a function to look into the database of Invoices
        #SQL query to look up entry
        invoice="Invoice"
        return(invoice)
    elif doctype==3 and docnumber in jes:
        #This will have to be a function to look into the database of Journal Entries
        #SQL query to look up entry
        je="Journal Entry"
        return(je, jes[docnumber])
    else:
        return("This document does not exist")
