class purchaseOrder(object):
	#Class to store Purchase Orders for sales process
	def __init__(self,item,itemnum,quantity,unit,unitcost,number):
		self.item=item
		self.itemnum=itemnum
		self.quantity=quantity
		self.unit=unit
		self.unitcost=unitcost
		self.number=number

	def totalCost(self):
		#Returns the total cost of the inventory items
		print(self.quantity*self.unitcost)

class customer(object):
	#Class to store individual customers for purchasing process and sales process
	def __init__(self,custname,custnumber,address,bank):
		self.custname=custname
		self.custnumber=custnumber
		self.address=address
		self.bank=bank

class item(object):
	#Class for inventory system to store individual items
	def __init__(self,quantity,description,unit,unitcost):
		self.quantity=float(quantity)
		self.unit=string(unit)
		self.unitcost=float(unitcost)
		self.description=string(description)

class invoice(object):
	#Class for Invoices for purchasing process
    def __init__(self,number,amount,date,custname,custnum,duedate):
        self.number=number
        self.amount=amount
        self.date=date
        self.custname=custname
        self.custnum=custnum
        self.duedate=duedate


class JournalEntry(object):
	#Class for JournalEntries
    def __init__(self,code,entries):
        self.code=code
        self.entries=entries
    #Add function JE_Write
    #Add function if balanced
