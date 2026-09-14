# list = ["7", "14", "21", "28", "35", "42", "49", "56", "63", "70"]
list = [str(7*i) for i in range(1,11)]

result = "\n".join(list)
print(result)