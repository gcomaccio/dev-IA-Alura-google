from random import randint
from random import seed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n_voluntarios = 300
idade_voluntarios = np.random.randint(60,100, size=n_voluntarios)
print(idade_voluntarios) 
