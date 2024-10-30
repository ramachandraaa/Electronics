import numpy as np
import matplotlib.pyplot as plt
N=21;
n=np.arange(-10,11)
delta=np.zeros(N)
delta[N//2]=1
plt.stem(n,delta)
plt.xlabel('n')
plt.ylabel('Delta')
plt.title('Unit impulse signal')
plt.show()
