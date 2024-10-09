def function():
    a = int(input('enter the numarator :'))
    b = int(input('enter the denomenator :'))
    try:
        if b==0:
            raise ZeroDivisionError('we can not divide the any number with zero')
    except Exception as E:
        print(E)
    else:
        print(a/b)
function()
