# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()
if sys.argv[1] == "customers":
	customers = cur.execute("SELECT Id, ContactName FROM customer").fetchall()
	print("Id\t\tCustomer Name")
	for row in customers:
		print('{}\t\t{}'.format(*row), sep='')


elif sys.argv[1] == "employees":
	employees = cur.execute("SELECT Id, FirstName, LastName FROM employee").fetchall()
	print("Id\t\tEmployee Name")
	for row in employees:
		print('{}\t\t{} {}'.format(*row), sep='')

elif sys.argv[1] == "orders":
	cmd, opt = sys.argv[2].split('=')
	if cmd == "cust":
		cs = cur.execute("SELECT OrderDate FROM [Order] WHERE CustomerId ='{}'".format(opt)).fetchall()
		print('Order date by ID {}'.format(opt))
		for row in cs:
			print(*row)

	elif cmd == "emp":
		eId = cur.execute("SELECT EmployeeId FROM Employee WHERE LastName = '{}')".format(opt)).fetchone[0]
		print(eId)
		es = cur.execute("SELECT OrderDate FROM [Order] WHERE EmployeeId = '{}'".format(eId)).fetchall()
		print('Order dates processed by Employee {}, ID {}'.format(opt, eId))
		for row in es:
			print(*es)
cur.close()	
