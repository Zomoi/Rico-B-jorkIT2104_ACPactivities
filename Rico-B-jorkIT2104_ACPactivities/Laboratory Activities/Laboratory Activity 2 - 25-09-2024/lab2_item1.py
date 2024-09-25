'''def main():
    nums =  int(input("Enter an integer: "))
    if palindrome(nums):
        print("Palindrome")
    else:
        print("Not a Palindrome")


def palindrome(num):
    convert_int_to_string = str(num)
    if convert_int_to_string == convert_int_to_string[::-1]: # [::-1] makes the string reversed, we checked if its equal, if not then we return False. 
        return True
    else:
        return False
    
main()'''

nums = int(input("Enter an integer: "))
convert_int_to_string = str(nums)
if convert_int_to_string == convert_int_to_string[::-1]:
        print("Palindrome")
else: 
        print("Not a Palindrome")

