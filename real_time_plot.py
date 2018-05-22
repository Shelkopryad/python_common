import matplotlib.pyplot as plt
import numpy as np

plt.axis([0, 100, 0, 100])

for i in range(100):
    y = np.random.randint(20)
    plt.scatter(i, y)
    plt.pause(0.5)
    
plt.show()