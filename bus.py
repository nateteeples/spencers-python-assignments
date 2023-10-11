people = int(input("Input amount of people: "))
buses = people // 50
vans = (people % 50) // 10
print(f"Number of buses: {buses}\nNumber of vans: {vans}")
