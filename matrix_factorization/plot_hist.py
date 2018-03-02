import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show(dataframe, size = 20):
    fig, axs = plt.subplots(4, 4, sharey=True, tight_layout=True, squeeze=False)
    fig.set_size_inches(size,size)
    cnt = 0
    for col in dataframe:
        n_bins = len(set(dataframe[col]))
        arr = axs[cnt/4, cnt%4].hist(np.array(dataframe[col]), bins = n_bins)
        for i in range(n_bins):
            axs[cnt/4, cnt%4].text(arr[1][i],arr[0][i],str(int(arr[0][i])))
        axs[cnt/4, cnt%4].set_xlabel('%s' % col)
        cnt = cnt+1
    plt.show()
    plt.clf()