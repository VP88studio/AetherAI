testing = True
input = 5
weight = 0
bias = 0
target = 10
error = 1
prediction = 0
while testing:
    if error == 0:
        prediction = (input * weight) + bias
        error = target - prediction
        print(f"Weight: {weight}")
        print(f"Prediction: {prediction}")
        print(f"Target: {target}")
        print(f"Error: {error}")
        print("! Achived Total !")
        testing = False
    prediction = (input * weight) + bias
    error = target - prediction
    if error > 0:
        weight += 1
    if error < 0:
        weight -+ 1
    print(f"Weight: {weight}")
    print(f"Prediction: {prediction}")
    print(f"Target: {target}")
    print(f"Error: {error}")