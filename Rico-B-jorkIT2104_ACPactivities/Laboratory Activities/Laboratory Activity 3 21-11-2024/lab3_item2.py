def perfect_num(num):
    sumv = 0
    for i in range(1,num):
        if num % i == 0:
            sumv += i
    if sumv == num:
        return f"{num} is a perfect number."
    else:
        return f"{num} is not a perfect number."
    
num = input("Enter a number: ")
if  num.isdigit() :
    num = int(num)
    result = perfect_num(num)
    print(result)    
else:
    print("Please enter a valid integer.")