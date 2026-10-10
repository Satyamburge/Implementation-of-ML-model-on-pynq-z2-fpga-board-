# Convert to NumPy arrays

X= np.array(time_data)

Y= np.array(temperature_data)

# Linear regression

m, c = np.polyfit(X, Y, 1)

# Expected / predicted temperature

Y_pred m * X + c

print("Slope (m)", m)

print("Intercept (c) :", c)

print("\nLinear Regression Equation:")

print("Temperature = {:.6f} x Time + {:.6f}".format(m, c))

