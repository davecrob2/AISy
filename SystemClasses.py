from datetime import datetime
import sqlite3


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

# class JournalEntry(object):
# 	#Class for JournalEntries
#     def __init__(self,code,entries):
#         self.code=code
#         self.entries=entries
#     #Add function JE_Write
#     #Add function if balanced
# 	def code():

# 		today = str(datetime.now())
# 		today_format = today[:4]+today[5:7]+today[8:10]
# 		counter=1000
# 		str_counter = str(counter)
# 		je_num = today_format+str_counter
# 		conn=db_connect("AISyDB.db")
# 		c=conn.cursor()
# 		c.execute(SELECT * FROM 'Journal Entries' ORDER BY ID DESC LIMIT 1)
# 		last=str(c.fetchone())
# 		if last[:8]==je_num[:8]:
# 			counter=last+1
# 			code=(today_format+str(counter))

# 		else:
# 			code=je_num
# 	return(code)

#class fuck(object):
def code_gen():

	today = str(datetime.now())
	today_format = today[:4]+today[5:7]+today[8:10]
	counter=1000
	str_counter = str(counter)
	je_num = today_format+str_counter
	conn=sqlite3.connect("AISyDB.db")
	c=conn.cursor()
	c.execute("SELECT ID FROM JournalEntries ORDER BY ID DESC LIMIT 1")
	last=str(c.fetchone())
	if last[1:9]==je_num[:8]:
		counter=int(last[9:13])+1
		code=(today_format+str(counter))
	else:
		code=je_num
	return(int(code))

##today = str(datetime.now())
##today_format = today[:4]+today[5:7]+today[8:10]
##counter=1000
##str_counter = str(counter)
##je_num = today_format+str_counter
##conn=sqlite3.connect("AISyDB.db")
##c=conn.cursor()
##c.execute("SELECT ID FROM JournalEntries ORDER BY ID DESC LIMIT 1")
##last=str(c.fetchone())
##if last[1:9]==je_num[:8]:
##        counter=int(last[9:13])+1
##        code=(today_format+str(counter))
##        print(code)
##else:
##        code=je_num
##        print(code)

