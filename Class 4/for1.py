# for a in range(5, 8):
#     print(a, end=" ")

# for b in ["apple", "pear", "orange"]:
#     print(b)

# for a in range(10):
#     if a <= 5:
#         print("X")

    # if a < 5:
    #     print(str(a) + " less than 5")
    # else:
    #     print("more than 5")

# Rewrite this using the "continue" statement.
for a in range(10):
    if a <= 5:
        print(a)

for a in range(10):
    if a > 5:
        continue
    print(a)


