# Convert to NumPy arrays np.array(time data)

np.array(temperature_data)

#Logarithmic regression: #Ya*ln(X) + b

a, b = np.polyfit(np.log(X), Y, 1)

#Expected temperature

Y_pred =a * np.log(X) b

print("Coefficient a", a)

print("Intercept b", b)

print("\nLogarithmic Regression Equation:")

print("Temperature = {:.6f} x In (Time)+ {:.6f}".format(a, b))
