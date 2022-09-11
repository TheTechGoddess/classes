fr
for x in range(1,1000001):
    if x % 10 == 0:
        print('\033[95m' + str(x) + '\33[0m')
    else:
        print(x)