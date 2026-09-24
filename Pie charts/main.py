import matplotlib.pyplot as plt 
import numpy as np

# Bar chart1= Circular chart divided into slices to show 
#             percentages of the total. Good for visualizing 
#             distribution among categories.

categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([300,250,275,225])
colors = ["red","green","yellow","blue"]

plt.pie(values, labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0,0,0,0.1],
        shadow=True,
        startangle=180)

plt.title("South point college")

plt.show()