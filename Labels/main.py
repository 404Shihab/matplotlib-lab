import matplotlib.pyplot as plt
import numpy as np

x = np.array([2000, 2001, 2002, 2003, 2004])
y1 = np.array([20, 13, 18, 34, 9])
y2 = np.array([30, 22, 9, 3, 28])
y3 = np.array([10, 3, 20, 19, 23])


plt.title("Class Size", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="blue")


plt.xlabel("Year", fontsize=20,
           family="Arial",
           fontweight="bold",
           color="darkblue")


plt.ylabel("Students", fontsize=20,
           family="Arial",
           fontweight="bold",
           color="darkblue")


plt.tick_params(axis="both",
                color="darkblue")



plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)


plt.xticks(x)

plt.show() 