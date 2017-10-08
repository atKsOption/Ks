import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 0.1, 0.01)
print x
plt.plot(x, np.sin(x))
plt.show()
