import sys

def simpleint(p,t,r):
    return(p*r*t)/100

p = int(sys.argv[1])
t = int(sys.argv[2])
r = int(sys.argv[3])
print("simple interest is :",simpleint(p,t,r))