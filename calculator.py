while True:
    try:
        firstnumber=input("Enter first number (or q to quit): ").lower()
        if firstnumber =="q":
              print("goodbye!")
              break
        
        num1=float(firstnumber)
        operator=input("Enter operator(+,-,/,*): ")

        num2=float(input("Enter second number: "))

        if operator=="+":
            result=(num1+num2)
        elif operator=="-":
            result=(num1-num2)
        elif operator=="*":
            result=(num1*num2)
        elif operator=="/":
            if num2==0:
                print("You cannot divide a number by zero!!")
            else:
                result=num1/num2
        else:
            print(f"{operator} is an Invalid operator!!!")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print(f"Invalid ! Please enter a number")
