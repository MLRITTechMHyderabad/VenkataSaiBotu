def calculator(a, b, operator):        
    try:
        if not isinstance(a, (int,float)) or not isinstance(b, (int,float)) :
            raise ValueError("Error: Invalid input type")
        elif operator not in ['+', '-', '*', '/', '%', '**']:
            raise TypeError("Error: Unsupported operator")
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        elif operator == '%':
            return a % b
        elif operator == '**':
            return a ** b
                     
    except ZeroDivisionError as e:
        return e
    except ValueError as e:
        return e
    except TypeError as e:
       return e
    except Exception as e:
        return e

print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"