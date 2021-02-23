#%%
import LineOfBestFit
import numpy as np
import matplotlib.pyplot as plt

Mass_list = [400, 70, 45, 2, 0.3, 0.16]
M_list = [270, 82, 50, 4.8, 1.45, 0.97]

Masslog_list = list(map(lambda a: np.log(a), Mass_list))
Mlog_list = list(map(lambda m: np.log(m), M_list))

plt.plot(Mass_list, M_list, ".")
plt.subplots(1)
plt.plot(Masslog_list, Mlog_list, '.')

LineOfBestFit.getBestFit(Mass_list, M_list)
LineOfBestFit.getBestFit(Masslog_list, Mlog_list)
# %%
