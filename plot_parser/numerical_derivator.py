import pandas as pd
import numpy as np

data = pd.read_csv('temp/1a_experiment.csv')

dx = np.gradient(data['temperature'])
dy = np.gradient(data['I(Rload)'])
derivative = dy / dx

# pridani derivace
data['dI_dT'] = derivative

# smazani sloupce
data = data.drop(columns=['I(Rload)'])

data.to_csv('temp/output.csv', index=False)
