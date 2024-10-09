print('start')
try:
    print('try block is starting execution...!')
    print('outer try block')
    try:
        print('inner try block')
        print(10/0)
        print('ineer try block is executed successfully ...!')
    except Exception as InnerE:
        print(InnerE)
except Exception as OuterE:
    print(OuterE)
print('ongoing')    
print('try block is ended')
