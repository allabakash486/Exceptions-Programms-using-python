try:
    if True:
        print([1,23,4]-[1,2])
    else:
        raise Exception
except Exception:
    print('Type Error')