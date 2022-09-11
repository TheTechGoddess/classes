from tkinter import *
from bankappbckend import ItechBank

new = ItechBank()
root = Tk()
root.title('ItechBank Admin')

root.geometry('500x300')

#create page
def create_submit(name,amount):
	new_user = new.create(name,amount)
	return new_user
	#print(new_user)
	#print(name)

#create page design
def create_page():
	global exit, top_create
	top_create = Toplevel()
	top_create.geometry('400x300')
	label_name = Label(top_create,text='Fullname:')
	entry_name = Entry(top_create, width=35)
	label_amount = Label(top_create,text='Amount:')
	entry_amount = Entry(top_create, width=35)
	button_submit = Button(top_create, text='Submit', command=lambda:create_submit(entry_name.get(),entry_amount.get()))
	
	label_name.grid(row=0, column=0, padx=20, pady=10)
	entry_name.grid(row=0, column=1, padx=20, pady=10)
	label_amount.grid(row=1, column=0, padx=20, pady=10)
	entry_amount.grid(row=1, column=1, padx=20, pady=10)
	button_submit.grid(row=2, column=0 )
	label_success.grid(row=3, column=0)




#create_balance
def create_balance(amount):
	new.check_balance(amount)
	label_success = Label(top_create, text='successful')
	return amount

#create_balance design
def check_balance_page():
	global exit, top_create
	top_create = Toplevel()
	top_create.geometry('400x300')
	label_name = Label(top_create,text='Click the "check" button to check your Balance:')
	button_check_balance = Button(top_create, text='Check',width=18, command=lambda:create_balance(entry_amount.get()))	

	label_name.grid(row=0, column=0, padx=20, pady=10)
	button_check_balance.grid(row=1, column=0, columnspan=20 )




#deposit
def deposit_submit(depositor,amount):
	new.deposit(depositor,amount)

#deposit design
def deposit_page():
	global exit, top_create
	top_create = Toplevel()
	top_create.geometry('400x300')
	label_name = Label(top_create,text='Depositorsname:')
	entry_name = Entry(top_create, width=35)
	label_amount = Label(top_create,text='Amount:')
	entry_amount = Entry(top_create, width=35)
	label_id = Label(top_create,text='Recieversid:')
	entry_id = Entry(top_create, width=35)
	button_submit = Button(top_create, text='Submit', command=lambda:deposit_submit(entry_name.get(),entry_amount.get()))
	
	label_name.grid(row=0, column=0, padx=20, pady=10)
	entry_name.grid(row=0, column=1, padx=20, pady=10)
	label_amount.grid(row=1, column=0, padx=20, pady=10)
	entry_amount.grid(row=1, column=1, padx=20, pady=10)
	label_id.grid(row=2, column=0, padx=20, pady=10)
	entry_id.grid(row=2, column=1, padx=20, pady=10)
	button_submit.grid(row=3, column=0 )
	#label_success.grid(row=3, column=0)



#transfer
def transfer_submit(amount,name):
	new.transfer(amount,name)

#transfer design
def transfer_page():
	global exit, top_create
	top_create = Toplevel()
	top_create.geometry('400x300')
	label_name = Label(top_create,text='Recieversname:')
	entry_name = Entry(top_create, width=35)
	label_amount = Label(top_create,text='Amount:')
	entry_amount = Entry(top_create, width=35)
	button_submit = Button(top_create, text='Submit', command=lambda:transfer_submit(entry_amount.get(),entry_name.get()))
	
	label_name.grid(row=0, column=0, padx=20, pady=10)
	entry_name.grid(row=0, column=1, padx=20, pady=10)
	label_amount.grid(row=1, column=0, padx=20, pady=10)
	entry_amount.grid(row=1, column=1, padx=20, pady=10)
	button_submit.grid(row=2, column=0 )
	#label_success.grid(row=3, column=0)	


#withdraw
def withdraw_submit(amount):
	new.withdraw(amount)

#withdraw design
def withdraw_page():
	global exit, top_create
	top_create = Toplevel()
	top_create.geometry('400x300')
	label_amount = Label(top_create,text='Input Amount:')
	entry_amount = Entry(top_create, width=35)
	button_submit = Button(top_create, text='Submit', command=lambda:withdraw_submit(entry_amount.get()))
	
	label_amount.grid(row=1, column=0, padx=20, pady=10)
	entry_amount.grid(row=1, column=1, padx=20, pady=10)
	button_submit.grid(row=2, column=0 )
	#label_success.grid(row=3, column=0)

button_create = Button(root, text='Create', width=23, command = create_page)
button_deposit = Button(root, text='Deposit', width=23, command=deposit_page)
button_withdraw = Button(root, text='Withdraw', width=23, command=withdraw_page)
button_transfer = Button(root, text='Transfer', width=23, command=transfer_page)
button_check_balance = Button(root, text='Check Balance', width=46, command = check_balance_page)
# display button
button_create.grid(row=0, column=0)
button_deposit.grid(row=0, column=1)
button_withdraw.grid(row=0, column=2)
button_transfer.grid(row=1, column=0)
button_check_balance.grid(row=1, column=1, columnspan=2)


root.mainloop()

