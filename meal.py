charge = float(input("Input charge of meal ($): "))
tip = charge * 0.18
tax = charge * 0.07
total = charge + tip + tax
print(f"18% tip: ${tip:.2f}")
print(f"7% sales tax: ${tax:.2f}")
print(f"Total charge: ${total:.2f}")
