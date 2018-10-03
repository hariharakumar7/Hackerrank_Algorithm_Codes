import math
def print_formatted(n):
    for i in range(1,n+1):
        print(str(i).rjust(int(math.log(n))),str(oct(i))[2:].rjust(int(math.log(n))),str(hex(i))[2:].rjust(int(math.log(n))),str(bin(i))[2:].rjust(int(math.log(n))))