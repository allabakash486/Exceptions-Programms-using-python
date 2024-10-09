def function():
    a = int(input('enter the numarator :'))
    b = int(input('enter the denomenator :'))
    try:
        if 1:
            print(a/b)
        else:
            raise ZeroDivisionError
    except Exception as E:
        print(E)
function()
