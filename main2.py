import numpy as np
from scipy import stats

if __name__ == '__main__':
    data = np.random.randn(5, 4)
    mean_value = np.mean(data)
    print("Media: " + str(mean_value))