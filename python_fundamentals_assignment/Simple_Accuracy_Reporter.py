while True:
    try:
        accuracy = float(input("Enter a floating-point accuracy value: "))
        print(f"Model accuracy is {accuracy}")
        break
    except ValueError:
        print("Error: Please enter a valid numeric value.")