def dec(f):
    print("Innsidde dec")
    def wrap(*args,**kwargs):
        print("In wrap")
        f(*args)
        print("WRAPPED")
    print("DECORATED")
    return wrap

@dec
def central(n1,n2):
    print("In central")
    print(n1+n2)
    print("done")

central(2,3)