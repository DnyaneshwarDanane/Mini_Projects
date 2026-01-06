print("---------simple billing app ------------")

prices = []

while True:
    user_input = input("Enter the price or(type'finist' to stop) : ")

    if user_input == "finish":
        print("Finish Billing")
        break
    else:
        price = int(user_input)
        prices.append(user_input)
        print("added")

print("billing sumarry")
print("items: ",prices)
print("total items: ",len(prices))
print("total amount: ",sum(prices))
    


