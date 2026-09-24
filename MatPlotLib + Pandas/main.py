import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("MatPlotLib + Pandas/data.csv")

position_count = df["Position"].value_counts()

plt.bar(position_count.index, position_count.values)

plt.show()

