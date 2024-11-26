def main():
    try:
        size = int(input("Enter the size of the array: "))

        if size <= 0:
            print("The size must be greater than 0")
            return
        
        arr = [0.0] * size

        print("Enter the elements of the array: ")
        for i in range(size):
            arr[i] = int(input())

        print_e = int(input("Enter the index of the element to print: "))
        print(f"Element at index {print_e}:{arr[print_e] : .2f}")

    except IndexError:
        print(f"Index {print_e} is invalid.")

main()