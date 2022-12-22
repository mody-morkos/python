print("\n\n\n")
funct = input("enter your equation".upper()).lower().strip()
def solve(x):
    x = x
    result = eval(funct)
    return result

def bisection(xl,xu):
    xr = 0.0
    xrold = 0.0
    error = 100
    EE = float(input("Enter the ERROR "))
    print("\n\n\t\t\tSOLVE\n\n")
    while(error > EE):
        xr = ( xl + xu)/2
        error = abs(((xr - xrold)/ xr)*100)
        print("{:<9} {:<9} {:<9} {:<9} {:<9} {:<9} {:<9}"
        .format(round(xl,4),round(solve(xl),4),round(xu,4),round(solve(xu),4),
        round(xr,4),round(solve(xr),4),round(error,4)))
        xrold = xr
        if solve(xl)*solve(xr)<0:
            xu = xr
        else:
            xl = xr
    else:
        print(" \n the final result is".upper(),round(xr,4),"\n")

xl=float(input("Enter XL".upper()).strip())
xu=float(input("Enter xu".upper()).strip())

bisection(xl,xu)
