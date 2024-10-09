print('start')
try:
    print('try block is starting execution...!')
    print('ongoing')
    print(a)
    print('try block is ended')
except NameError as ne:
    print(ne)
print('end')
