import math


def ApproxAlgo(x0,tol):
    iter =0
    diff = x0
    x= x0
    print(f"{iter} :  {x}")
    while(diff>=tol):
        iter+=1
        y=x
        x=(x/2)+(1/x)
        print(f"{iter} :  {x}")
        diff = abs(x-y)
    print(f"\nConvergence after {iter} iterations")



def f(x):
    return x**3 + 4*x**2 -10
def BisectionMethod(tol,left,right,max):
    i=0
    while(abs(right-left)>tol and i<max):
        i+=1
        p = (left+right)/2

        if((f(left)<0 and f(p)>0) or (f(left)>0 and f(p)<0)):
            right = p
        else:
            left=p
    print(f"Took {i} iterations to get to number {p}")



def g(x):
    return(((10-x**3)**(.5))/2)
    #return x-(x**3)-(4*x**2)+10
def FixedPointOp(p0,TOL,n0):
    i=1
    div=0
    while(i<=n0):
        try:
            p=g(p0)
        except:
            div=1
            break
        print(f"{i} : {p}")
        if(abs(p-p0) < TOL):
            print(f"\nSuccess after {i} iterations")
            return
        i+=1
        p0=p
    if(div==1):
        print("\nResult diverges\n")
    print(f"Failure after {i} iterations")


def ff(x):
    return math.cos(x)-x
def fp(x):
    return -math.sin(x)-1

def NewtonsMethod(Pp,TOL,N0): #fp is fPrime and ff is the function for Newtons
    i=1
    while(i<=N0):
        print(f"{i} : {Pp}")
        if(fp(Pp)!=0):
            Pn = Pp - ff(Pp)/fp(Pp)
            if(abs(Pn-Pp) < TOL):
                print(f"Success {Pn}")
                return
            i=i+1
            Pp = Pn
        else:
            print(f"Failure")
            return
    print(f"Failure")
    return

ApproxAlgo(1.5,0.000001)
BisectionMethod(10**(-3),1,2,100)
FixedPointOp(1.5,.000001,50)
NewtonsMethod(3.14/4,.000001,50)