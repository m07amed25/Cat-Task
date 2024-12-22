def chewbacca_number(x):
    digits = list(str(x))
    
    for i in range(len(digits)):
        digit = int(digits[i])
        # If the first digit is 0
        if i == 0 and digit == 9:
            continue
        # Replace the digit with 9 - t
        if digit > 4:
            digits[i] = str(9 - digit)
    
    return int("".join(digits))

x = int(input("Enter the number: "))

result = chewbacca_number(x)
print(result)
