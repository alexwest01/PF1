def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def parse_float(input_str):
    try:
        return float(input_str), None  
    except ValueError:
        return None, "Error: Please enter a valid number."

def log_error(error_message):
    error_log.append(error_message)

def main():
    global error_log
    error_log = []
    
    while True:
        print("\nSimple Arithmetic Operations")
        a_str = input("Enter the first number: ")

        a, error = parse_float(a_str)
        if error:
            log_error(error)
            print(error)
            continue

        b_str = input("Enter the second number: ")

        b, error = parse_float(b_str)
        if error:
            log_error(error)
            print(error)
            continue

        print("Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Choose an operation (1-4): ")
        
        operation_functions = [add, subtract, multiply, divide]
        try:
            operation_index = int(choice) - 1
            result = operation_functions[operation_index](a, b)
            print("Result:", result)
        except (IndexError, ValueError):
            error_message = "Invalid choice. Please select a valid operation."
            log_error(error_message)
            print(error_message)
        except ZeroDivisionError:
            error_message = "Cannot divide by zero."
            log_error(error_message)
            print(error_message)
        
        while True:
            refresh = input("Perform another operation? (yes/no): ").strip().lower()
            if refresh in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        if refresh == 'no':
            break 

    if error_log:
        print("\nError Log:")
        for error in error_log:
            print(error)

if __name__ == "__main__":
    main()
