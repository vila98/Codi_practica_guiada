import numpy as np
import matplotlib.pyplot as plt
def style():
  plt.axvspan(0,0.365,facecolor='red',alpha=0.4)
  plt.axvspan(0.365,0.625,facecolor='green',alpha=0.4)
  plt.axvspan(0.625,1,facecolor='red',alpha=0.4)
  plt.axhspan(-10,0.020021,facecolor='white')
  plt.xlabel(r'$z/d$')
  plt.ylabel(r'$(T-T_0)\frac{2k}{V^2\sigma}$')
  plt.ylim(0,0.030)
  plt.xlim(0,1)
  plt.xticks(np.linspace(0,1,11))
  plt.legend()
def erstyle():
  plt.xlabel(r'$z/d$')
  plt.ylabel(r'$(T-T_{analítica})\frac{2k}{V^2\sigma}$')
  plt.xlim(0,1)
  plt.xticks(np.linspace(0,1,11))
  plt.legend()
