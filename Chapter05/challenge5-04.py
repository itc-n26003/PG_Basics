characteristic = {"height": "178", "weight": "65", "blood": "O"}

answer = input("height, weight, or blood")
if answer in characteristic:
    result = characteristic[answer]
    print(result)
