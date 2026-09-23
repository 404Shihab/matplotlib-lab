import matplotlib.pyplot as plt
import numpy as np


x = np.array([2000, 2001, 2002, 2003, 2004])

y1 = np.array([20, 12, 18, 9, 22])
y2 = np.array([28, 17, 8, 39, 2])
y3 = np.array([9, 30, 28, 5, 32])


# Common styling options for all three lines
line_style = dict(
    marker=".",
    markersize=20,              # Also can use: ms
    markerfacecolor="red",      #Also can use: mfc
    markeredgecolor="red",      # Also can use: mec
    linestyle="dashdot",        # "none" removes the connecting line
    linewidth=3                 # Also can use: lw
)


#plot each dataset with a different line color
plt.plot(x, y1, color="red", **line_style)
plt.plot(x, y2, color="blue", **line_style)
plt.plot(x, y3, color="yellow", **line_style)


plt.show()  #Display the plot