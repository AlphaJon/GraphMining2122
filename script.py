import numpy as np
import scipy
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#DateTime	Actor	Recipient	Behavior	Category	Duration	Point
obs_df = pd.read_csv("OBS_data.txt", sep='\t')
obs_df.dropna(subset=['Actor', 'Recipient'], inplace=True)