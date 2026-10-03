print("==========shopping sort=========================")

cart = ["Laptop", "Mouse", "Keyboard", "Headphones", "USB Cable"]

cart.remove("USB Cable")

cart.append("Webcam")


webcam = cart.pop()
cart.insert(3, webcam)


print("========================================")
print("           SHOPPING CART")
print("========================================")

print("Products:", cart)
print("First Product  :", cart[0])
print("Last Product   :", cart[-1])
print("middle product:", cart[3])
print("Total Products :", len(cart))

print("----------------------------------------")
print("           PRICE SUMMARY")
print("----------------------------------------")


prices = [55000, 800, 1500, 2500, 2000]




total_price = sum(prices)
cheapest_price = min(prices)
most_expensive_price = max(prices)
webcam_position = cart.index("Webcam")
count_2000 = prices.count(2000)


print("Total Value    :", total_price)
print("Lowest Price   :", cheapest_price)
print("Highest Price  :", most_expensive_price)
print("Webcam Position:", webcam_position)
print("₹2000 Count    :", count_2000)



print("----------------------------------------")
print("Original Prices:", prices)

prices.sort()

print("Lowest to Highest:", prices)

prices.reverse()

print("Highest to Lowest:", prices)

print("========================================")
print("                 FINISH SHOPPING   ")
print("========================================")