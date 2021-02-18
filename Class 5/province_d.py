provinces = { "QC": "Quebec", "PQ": "Quebec", "ON": "Ontario" }

# provincelist = ["Quebec", "Ontario"]

#print(provinces["XX"])

provincename = provinces.get("QC")

print(provincename)

# if provincename != None:
#     print(provincename)
# else:
#     print("This province doesn't exist")
