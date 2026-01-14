def add(a,b):
    return a+b
    
def multiply(a,b):
    return a*b

def power(a,b):
    if mod(b,1)==0:
        c=1
        flag=0
        if b<0:
            flag=1
            b*=-1

        for i in range(b):
            c*=a
        d=1/c
        if flag==0:
            return c
        else:
            return d
    else:
        return exp(b * ln(a))

def sqrt(a):
    b=a/2
    for i in range(10):
        b=0.5*(b+a/b)
    return b

def factorial(a):
    b=1
    for i in range(1,a+1):
        b*=i
    return b

def exp(a):
    i=0
    b=0
    c=0.1
    while True:
        b+=power(a,i)/factorial(i)
        if b/c < 1.00000001 and b!=0:
            break
        c=b
        i+=1
    return b

def ln(a):
    if a<0:
        return ValueError("dont play with me GET lost")
    count=0
    while a>2:
        a/=2
        count+=1
    i=1
    j=1
    r=0
    b=a-1
    y=0.01 
    while True:
        r+=j*pow(b,i)/i
        if abs(r-y) < .00000001 and b!=0:
            break
        y=r
        i+=1
        j*=-1
    return r + count*0.69314718056

def log10(a):
    return ln(a) / ln(10)

def mod(a,b):
    count=0
    while a>=b:
        a-=b
        count+=1
    return a

def sin(z):
    a=mod(z,6.28)
    sign=1
    i=1
    b=0
    c=0.1
    while True:
        b+=sign*power(a,i)/factorial(i)
        if b/c < 1.00000001 and b/c>0.999999999 and b!=0:
            break
        c=b
        sign*=-1
        i+=2
    return b
    
def cos(z):
    a=mod(z,6.28)
    i=0
    b=0
    c=0.1
    sign=1
    while True:
        b+=sign*power(a,i)/factorial(i)
        if b/c < 1.00000001 and b>0.99999999 and b!=0:
            break
        c=b
        sign*=-1
        i+=2
        return b
    
def tan(a):
    return sin(a)/cos(a)

def arcsin(a):
    if abs(a) > 1:
        return ValueError("arcsin undefined for |x| > 1")
    term = a
    result = a
    i = 1
    while abs(term) > 0.0000000001:
        term *= ( pow(2*i-1,2)*a*a ) / ( (2*i)*(2*i+1) )
        result += term
        i += 1
    return result
    
def arccos(a):
    return 1.57079632679-arcsin(a)

def arctan(a):
    return arcsin(a/sqrt(a*a+1))

    
while True:
    a=float(input("Enter a "))
    b=float(input("enter b "))
    op=input("operation? ")
    if op=='1':
        print(add(a,b))
    if op=='2':
        print(multiply(a,b))
    if op=='3':
        print(power(a,b))
    if op=='4':
        print(sqrt(a))
    if op=='5':
        print(exp(a))
    if op=='6':
        print(sin(a))
    if op=='7':
        print(cos(a))
    if op=='8':
        print(tan(a))
    if op=='9':
        print(ln(a))
    if op=='10':
        print(log10(a))
    if op=='11':
        print(arcsin(a))
    if op=='12':
        print(arccos(a))
    if op=='13':
        print(arctan(a))

    x = input("bye?(y/n) ")
    if x == 'y':
        break