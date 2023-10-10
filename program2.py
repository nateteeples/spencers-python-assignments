value1 = int(input("Input first value: "))
value2 = int(input("Input second value: "))
value3 = int(input("Input third value: "))
if value1 > value2 and value1 > value3:
    print(f"Largest value: {value1}")
elif value2 > value1 and value2 > value3:
    print(f"Largest value: {value2}")
elif value3 > value1 and value3 > value2:
    print(f"Largest value: {value3}")
elif value1 == value2 and value2 == value3:
    print("All values are equal")
if value1 < value2 and value1 < value3:
    print(f"Smallest value: {value1}")
elif value2 < value1 and value2 < value3:
    print(f"Smallest value: {value2}")
elif value3 < value1 and value3 < value2:
    print(f"Smallest value: {value3}")
