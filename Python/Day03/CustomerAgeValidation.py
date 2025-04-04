customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

customersForDiscount = list(filter(lambda customer : customer["age"] <= 40 and customer["age"] >= 18 , customers))

customersUpdatedPurchase = list(map(lambda customer : {
    "name" : customer["name"],
    "age" : customer["age"],
    "total_purchase" : customer["total_purchase"] *(0.9 if customer["age"] >= 18 and customer["age"] <= 25 else 0.95 )
},customersForDiscount))

print(customersUpdatedPurchase)