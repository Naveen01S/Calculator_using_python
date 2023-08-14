def add(x,y):
    return x+y;
def sub(x,y):
    return x-y;
def mul (x,y):
    return x*y;
def div (x,y):
    return x/y;
print("*CALCULATOR*")
print("Select operation")
print("1.Add");
print("2.Subtract")
print("3.Multiply");
print("4.Division")
while True:
    ch=input("enter choice(1/2/3/4):")
    if ch in('1','2','3','4'):
        try:
            n=float(input("Enter First Number."))
            m=float(input("Enter Second Number."))
        except ValueError:
            print("Invalid input.Please enter a valid input")
            continue
         
        
    if ch=='1':
        print(n,"+",m,"=",add(n,m))
    elif ch=='2':
       print(n,"-",m,"=",sub(n,m))
    elif ch=='3':
        print(n,"*",m,"=",mul(n,m))
    elif ch=='4':
        print(n,"/",m,"=",div(n,m))
    nexcal=input("Lets do another calculation? (yes/no):")
    if nexcal=="yes":
        continue
    elif nexcal=="no":
        break
    else:
        print("Enter valid input")
