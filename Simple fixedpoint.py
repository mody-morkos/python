import math
print("\n\n\n")
xi = 0
xiplus = 0
Error = 0
f = input("enter the function".upper()).lower().strip()
err = float(input("enter the error".upper()).strip())
def solve(x):
    x = x
    result = eval(f)
    return result

    print("\n\n\t\t\tSOLVE\n\n")


def fixedpoint(x):
    global xi,xiplus,Error
    xi = x
    xiplus = solve(xi)
    print("{:<9} {:<9} {:<9} ".format(round(xi,4),round(xiplus,4),round(Error,4)))
    Error = abs(((xiplus - xi)/xiplus)*100)
    if Error > err:
        fixedpoint(xiplus)
    else:
        return print("\n\nThe finial result is",round(xiplus,4),"\n\n")


x = float(input("enter the X0".upper()).strip())
fixedpoint(x)
