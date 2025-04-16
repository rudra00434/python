import matplotlib.pyplot as plt
import numpy as np
fig, axs=plt.subplots(ncols=3,nrows=3,figsize=(4.5,3.5),layout="constrained")
for row in range(3):
    for col in range(3):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                            transform=axs[row, col].transAxes,
                            ha='center', va='center', fontsize=18,
                            color='darkgrey')
fig.suptitle('plt.subplots()')
plt.show()
