## WAP TO INPUT A NUMBER AND CHECK WHETHER IT IS POSTIVE NEGATIVE OR ZERO
# WAP TO INPUT A NUMBER AND CHECK IT IS EXACTLY DIVISIBLE BY 5 AND 2 OR NOT 
# PRINT THE FACTORIAL OF NUMBER 5


# num = int(input("Enter any number : "))
# if (num > 0):
#     print("It is a Positive number")

# elif(num < 0):

#     print("It is a Negative number")
# else:
#     print("it is a zero ")


#2

# num = int(input("Enter any number : "))

# if ( num % 5 == 0 and num%2 == 0):
#     print("num is divisble by 5 and 2")

# elif( num%5==0 ):
#     print("num is divisble by 5")

# elif( num%2 ==0):
#     print("num is divisble by 2")

# else(num%5!=0 and num%2!=0):
#     print("not idivisble by 5 and 2")

    
num = int(input("Enter the number to get factorial of : "))
factorial =1
if (num < 0):
    print("Enter valid number.")
elif(num == 0):
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial *i
    print(f"The factorial of {num} is {factorial}")


