print("\n\n\n")
funct = input("enter the equstion".upper()).lower().strip()
def solve(x):
    x = x
    result = eval(funct)
    return result

def falsePosition(xl,xu):
    xrold = 0.0
    xr = 0.0
    error = 100
    EE = float(input("enter the error ".upper()).strip())
    while(error > EE):
        xr = xu -((solve(xu)*(xl -xu))/(solve(xl)-solve(xu)))
        error = abs( ((xr -xrold)/xr) * 100 )
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

falsePosition(xl,xu)

#-26+(82.3*x)-(88*pow(x,2))+(45.4*pow(x,3))-(9*pow(x,4))+(0.65*pow(x,5))