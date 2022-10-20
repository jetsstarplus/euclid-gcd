def GCD(x,y):
    z=0
    if x and y:
        z = x % y
        if (z == 0):
            return y
        return GCD(y,z)
