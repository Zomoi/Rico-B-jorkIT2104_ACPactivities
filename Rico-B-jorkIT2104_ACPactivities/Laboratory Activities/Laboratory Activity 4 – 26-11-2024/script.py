from Capybara import Capybara # importing capybara class from capybara module

def run_case():

    case_num = int(input("Enter the case number: "))
    if (case_num == 1):
        c1 = Capybara("Trisha","F",3)
        print(f"Test Case 1: Name: {c1.name}, Gender: {c1.gender}, Age: {c1.age} years old")
    elif (case_num == 2):
        c2 = Capybara("Gerts","F",2)
        print(f"Test Case 1: Name: {c2.name}, Gender: {c2.gender}, Age: {c2.age} years old")
    elif (case_num == 3):
        c3 = Capybara("Jenrick","M",5)
        print(f"Test Case 1: Name: {c3.name}, Gender: {c3.gender}, Age: {c3.age} years old")
    else:
        print("Only choose 1 to 3.")

run_case()