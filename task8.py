print('start')
l=[11,22,33,44,55]
try:
    print('try block is starting execution...!')
    print(l)
    ele = l[int(input('enter the element position ..:'))]
    divisor = int(input('Enter the divisor number:'))
    res = ele / divisor
    print('ongoing')    
    print('try block is ended')
except:
    print('i have handled the error...!!!....')
