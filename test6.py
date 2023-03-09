
'''try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))
    if width == length:
        exit("That looks like a square")
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number...")
'''
try:
    val1 = float(input("ENter the total value: "))
    val2 = float(input("Enter value: "))

    result = val1/val2 *100

    print("That is " + str(result), "%")
except ValueError or ZeroDivisionError:
    print("enter a number...")

