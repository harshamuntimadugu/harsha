print("=============shopping clothes==========================")

clothes=["t-shirt","jeans","formals","checks shirts","shorts","night dress"]

clothes.append("night pants")

clothes.remove("shorts")

print(clothes)



print("===========================")

print("products:",clothes)
print("total no.of. products:",len(clothes))
print("first-product:",clothes[2])
print("last product:",clothes[-1])
print("middle product:",clothes[5])



print("=====================clothes prices=========================")

prices=[200,400,600,900,1200,4500,650]

total_prices=sum(prices)
highest_price=max(prices)
lowest_price=min(prices)
formals_position=clothes.index("formals")




print("Total value:",{total_prices})
print("highest value:",{highest_price})
print("lowest value:",{lowest_price})
print("formalsposition",{formals_position})





print("==============sorting prices======================")

prices.sort()

print("lowest to highest:",prices)


print("total:",total_prices)



