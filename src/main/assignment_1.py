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

def NewtonsMethod(Pp,TOL,N0):
    i=1
    while(i<=N0):
        if(fo(Pp)!=0):
            Pn = Pp - f(Pp)/fp(Pp)
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