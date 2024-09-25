'''def transactions():
    total = int(input("Enter the total purchase amount: "))
    convert_int_to_float = (float(total))
    print(f"Initial Purchase Amount: {convert_int_to_float: .2f}")

    greaterthan5k = convert_int_to_float * 0.010
    lessthan5k = convert_int_to_float * 0.05

    if convert_int_to_float > 5000:
        print(f"Discount : {greaterthan5k: .2f}")
        print(f"Final Price: {convert_int_to_float - greaterthan5k} ")
    else:
        print(f"Discount {lessthan5k: .2f}")
        print(f"Final Price: {convert_int_to_float - lessthan5k} ")


def main():
    transactions()

    wannaplay = input("Do you want to try again? (yes/no): ").lower()
    if (wannaplay == "yes"):
        transactions()
    else:
        print("Thank you!")

main()'''

while (True):
        total = int(input("Enter the total purchase amount: "))
        convert_int_to_float = (float(total))
        print(f"Initial Purchase Amount: {convert_int_to_float: .2f}")

        greaterthan5k = convert_int_to_float * 0.10
        lessthan5k = convert_int_to_float * 0.05

        if convert_int_to_float > 5000:
            print(f"Discount : {greaterthan5k: .2f}")
            print(f"Final Price: {convert_int_to_float - greaterthan5k: .2f} ")
        else:
            print(f"Discount {lessthan5k: .2f}")
            print(f"Final Price: {convert_int_to_float - lessthan5k: .2f} ")
        
        wannaplay = input("Do you want to try again? (yes/no): ").lower()
        if wannaplay == "yes":
             continue
        else:
             print("Thank you!")
             break