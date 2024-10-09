print('start')
def function1():
    print('function1 is started ')
    print(10/0)
    print('function1 is ended')
def function2():
    print('functioon2 is started ')
    try:
        function1()
    except Exception as a:
        print(a)
    print('function2 is ended successfully...!')
print('mainspace is started successfdully....')
function2()
print('mainspace is ended successfdully....')
