import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,24,0.01)
y = (4 ** (-1 * x)) * 100
plt.ylim([0, 100])
plt.xlim([0, 24])
plt.xlabel('時間',fontname="MS Gothic")
plt.ylabel('やる気', fontname="MS Gothic")
plt.plot(x, y)
plt.show()