def updatePurchase(customer):
    if customer["age"] > 18 and customer["age"] <= 25 :
        customer["total_purchase"] *= 0.9 
    elif customer["age"] > 25 and customer["age"] <= 40 :
        customer["total_purchase"] *= 0.95 
    return customer

customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

customersForDiscount = list(filter(lambda customer : customer["age"] <= 40 , customers))

customersUpdatedPurchase = list(map(lambda customer : updatePurchase(customer),customersForDiscount))

print(customersUpdatedPurchase)