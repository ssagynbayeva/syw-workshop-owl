import numpy as np
import matplotlib.pyplot as plt
import paths

x = np.linspace(0,50)
y = np.linspace(0,50)

plt.plot(x, y)
plt.savefig(paths.figures / "plot1.pdf", bbox_inches="tight", dpi=300)