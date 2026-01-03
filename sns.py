import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
plt.style.use("seaborn-v0_8")
d=sn.load_dataset("penguins")
print(d.head())
sn.catplot(x="species", y="body_mass_g", kind="strip", data=d)
sn.catplot(x="species", y="body_mass_g", kind="strip", jitter=0.4, data=d)
sn.catplot(x="species", y="body_mass_g", kind="strip", jitter=True, data=d)
sn.catplot(x="species", y="body_mass_g", kind="swarm", data=d)
sn.catplot(x="species", y="body_mass_g", kind="swarm",hue="sex" ,data=d)
plt.show()