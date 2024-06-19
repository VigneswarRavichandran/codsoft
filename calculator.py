try:
    def calculator():
        print("CALCULATOR")
        print("\nOperations:\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Divison")
        #getting inputs
        num1=float(input("Enter the first number:")) 
        num2=float(input("Enter the second number:"))
        opt=int(input("Enter the operation number:"))
        if opt==1:
                res=num1+num2
                optr='+'
        elif opt==2:
                res=num1-num2
                optr='-'
        elif opt==3:
                res=num1*num2
                optr='*'
        elif opt==4:
                try:
                    res=num1/num2
                    optr='/'
                except:
                    res="Not possible"
                    optr='/'
        #printing the result  
        print("Result of",{num1},{optr},{num2},"is",{res})
    #calling the function
    calculator()
except:
    print("Invalid input")
