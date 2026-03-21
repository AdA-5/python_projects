while True:
    temp=input("enter Temperature recorded (q to quit): ").lower()
    if temp=="q":
        print("Goodbye!")
        break

    temp=float(temp)
    unit=input("Enter C (for celcius) or F (for Fahrenheit): ").strip().upper()
    if unit=="C":
        results=float((temp * 9/5) + 32)
        print(f"{temp}°C = {results}°F")
    elif unit=="F":
        results=float((temp - 32) * 5/9)
        print(f"{temp}°F = {results}°C")
    else:
        print("Please enter the temperature")
