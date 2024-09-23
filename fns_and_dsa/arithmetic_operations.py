def perform_operation(num1, num2, operation):
    match operation:
      case "add":
        print(f"The result is: {num1 + num2}")
      case "subtract":
        print(f"The result is: {num1 - num2}")
      case "multiply":
        print(f"The result is: {num1 * num2}") 
      case "divide":
        if num2 == 0:
            print("Can't divide by zero!")
        else:
            print(f"The result is: {num1 / num2}") 
      case _:
        print("Invalid input!")