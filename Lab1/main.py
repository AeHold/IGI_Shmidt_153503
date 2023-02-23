from constants import ADD, MUL, SUB, DIV


print("Hello World!")


try:    
    num1 = int(input("Input first number "))
    num2 = int(input("Input second number "))
    operation = input("Input operation ")
    if operation == ADD:
        print(num1 + num2)
    elif operation == MUL:
        print(num1 * num2)
    elif operation == SUB:
        print(num1 - num2)
    elif operation == DIV:
        if num2 == 0:
            print("Division by zero")
        else:
            print(num1 // num2)
    else:
        print("Invalid operation")
except ValueError:
    print("Please try again")


try
	s = input("Input array(in one line) \n")
	arr = list(map(int, s.split()))
	out = [x for x in arr if x % 2 == 0]
	print(out)
except ValueError:
	print ("Please try again")
