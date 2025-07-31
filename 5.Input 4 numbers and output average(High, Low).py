num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
num4=int(input("Enter the fourth number: "))
Total=num1+num2+num3+num4
Average=Total/4
if (Average>50) :
    print("Average is HIGH")
elif (Average<50) :
    print("Average is LOW")
elif (Average==50) :
    print("Average is 50")
