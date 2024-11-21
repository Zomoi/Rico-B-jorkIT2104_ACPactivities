def roman_to_integer(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and roman_values[roman[i]] < roman_values[roman[i + 1]]:
            ans -= roman_values[roman[i]]
        else:
            ans += roman_values[roman[i]]
    return ans


roman = input("Enter a Roman Numeral: ").strip().upper() 
integer_value = roman_to_integer(roman)
print(f"The integer value of '{roman}' is: {integer_value}")