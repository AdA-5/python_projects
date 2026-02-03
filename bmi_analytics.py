while True:
    height=float(input("Enter height: "))
    height_unit=input("Enter height unit (F-feet,C-centimetres,M-metres): ").upper()
    weight=float(input("Enter weight: "))
    weight_unit=input("Enter weight unit (K/L): ").upper()
    print("**************************************************************")

    if height_unit=="F":
        height=float(height*0.3048)
    elif height_unit=="C":
        height=float(height/100)
    elif height_unit=="M":
        pass
    else:
        print("invalid")
        exit()

    if weight_unit=="L":
        weight=float(weight/2.205)
        print(weight)
    elif weight_unit=="K":
        pass
    else:
        print("invalid")
        exit()

    BMI=float(weight/(height*height))

    if BMI<18.5:
        print(f"Classification: Underweight")
    elif BMI>=18.5 and BMI<25:
        print(f"Classification: Normal weight")
    elif BMI>=25 and BMI<30:
        print(f"Classification: Overweight")
    elif BMI>=30:
        print(f"Classification: Obese")
    else:
        print("Invalid")
    print("**************************************************************")

    again=input("Do you want to calculate BMI again? y/n: ").lower()

    if again!="y":
        print("The End")
        break


#success🎉🎉🎉
