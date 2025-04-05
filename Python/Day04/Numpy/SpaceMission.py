import numpy as np
resources = np.array([
    [15, 40, 32],
    [20, 42, 35],
    [25, 38, 30],
    [18, 50, 40],
    [22, 37, 36],
    [28, 45, 33]
])

print("Resource Consumption Matrix:")
print(resources)

[oxygen,water,food] = np.sum(resources,axis=0)
print(f'Total resources needed (tons): Oxygen: {oxygen}, Water: {water}, Food: {food}')

max_consumption_month = np.argmax(np.max(resources, axis=1))
max_consumption_resource = np.argmax(resources[max_consumption_month])
max_consumption_value = resources[max_consumption_month,max_consumption_resource]
print(f"Highest consumption in a month : {['Oxygen','Water','Food'][max_consumption_resource]} {max_consumption_value} tons in month {max_consumption_month+1}")

[oxygen,water,food] = np.std(resources,axis=0)
print(f"Standard deviation of consumption: Oxygen: {oxygen}, Water: {water}, Food: {food}")

resources_T = np.transpose(resources)

print('Transpose : ',resources_T)