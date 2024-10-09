print('start')
def function1():
    print('function1 is started ')
    print(10/0)
    print('function1 is ended')
def function2():
    print('functioon2 is started ')
    function1()
    print('function2 is ended successfully...!')
print('mainspace is started successfdully....')
try:
    function2()
except Exception as a:
    print(a)
print('mainspace is ended successfdully....')
