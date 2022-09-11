leapYear = int(input("type the year: "))

if (leapYear % 4 == 0) and (leapYear % 100 != 0) and (leapYear % 400 != 0) :
	print('True')
else:
    print('False')	
    