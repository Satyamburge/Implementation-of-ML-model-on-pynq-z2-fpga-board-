import matplotlib.pyplot as plt

plt.figure(figsize-(12, 6))

# Actual values:
#red dotted points only 
plt.plot( X, Y, ) markersize-10, label='Actual Temperature'

#Expected/Predicted values:
#blue dotted points + blue connecting Line 

plt.plot( x, Y pred, 'b.-', linewidth=2, markersize-8, label-Expected Temperature'

plt.xlabel("Time (seconds)")

plt.ylabel("Temperature (°C)")

plt.title("Actual vs Expected Temperature")

plt.legend()

plt.grid(True, linestyle, alpha-8.5)

plt.tight layout() plt.show
