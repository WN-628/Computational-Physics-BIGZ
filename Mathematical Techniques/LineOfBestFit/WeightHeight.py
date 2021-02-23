#%%
import LineOfBestFit
import numpy as np

W_list = [70, 75, 77, 80, 82, 84, 87, 90]
A_list = [2.1, 2.12, 2.15, 2.20, 2.22, 2.23, 2.26, 2.30]
Wlog_list = list(map(lambda w: np.log(w), W_list))
Alog_list = list(map(lambda a: np.log(a), A_list))

LineOfBestFit.getBestFit(Wlog_list, Alog_list)

# %%
