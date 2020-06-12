
startvalue = int(input("paste number"))
hundreds = startvalue // 100    # 1
tenths = (startvalue - hundreds * 100) // 10 # 2
units = startvalue - hundreds * 100 - tenths * 10 // 1 # 3
print(units * 100 + tenths * 10 + hundreds)
