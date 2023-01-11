---
title: "Some Useful Settings of Python Plotting"
date: 2020-09-18T14:52:10+08:00
tags: ["python", "virtualization"]
categories: ["virsualization"]
---

## __1 Pseudo-color map with polar projection__
We uasually need to plot pseudo-color maps in polar projection besides
except of thoese in Cartesian projection. Setting the `projection` as
`polar` in method `subplot`. Here , we give an example of python code.
```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 121)
r = np.linspace(0, 10, 51)

T, R = np.meshgrid(theta, r)
v = np.sin(T*R) * np.exp(-(T**2+R**2)/10)

plt.figure(figsize=(8, 5.5))
plt.subplot(111, projection='polar')
plt.pcolormesh(theta, r, v, cmap='CMRmap')
plt.colorbar()
plt.show()
```
