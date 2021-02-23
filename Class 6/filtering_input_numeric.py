base_size = input("Enter the size of the triangle base as a whole integer value. >")

if not base_size.isnumeric():
    print("The amount must be a number, try again.")
    exit()

if float(base_size) % 2 == 0:
    print("The number must be odd.")
    exit()

# ABC
# 1.2
# 2 4 6 8 10


