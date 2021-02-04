# Ask user to enter their name.
# Tell the user if their name is more than 6 characters or not.

#x = 5
# if x == 5:
#     print("The number is 5")
# else:
#     print("Not 5")

name = input("Please enter your name >").strip()

if len(name) >= 7:
    print("Name is longer than 6 characters")

    if len(name) < 10:
        print("But it's less than 10 characters")
else:
    print("Name is not longer than 6 characters")
    print("Please try again")

# 1-6 name not longer
# 7-9 name is longer than 6 AND less than 10
# 10 ->    Name is longer than 6 characters


