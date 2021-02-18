# list1 = [2, 4, 7, 9]
# list2 = [value for value in list1]
# list3 = [value + 1 for value in list1]

# The tax rate used to extract tax amounts from our sales.
TAX_RATE = .1556

daily_sales = [10.99, 12.99, 1.99, 2.39]
daily_tax_paid = [x * TAX_RATE for x in daily_sales]

# squares = [value + 1 for value in range(1,11)]

print(daily_sales)
print(daily_tax_paid)

