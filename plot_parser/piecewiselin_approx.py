import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

INP_PATH = f'./plot_parser/temp/1a_Iout_temp-stab.csv'

def piecewiselin_approximation(x, y, x_thresholds):
    
    # parse the therhold values
    functions = []  
    for x_threshold in x_thresholds[:-1]:
        y_threshold = y[np.where(x == x_threshold)[0][0]]
        slope = (y[np.where(x == x_threshold)[0][0] + 1] - y_threshold) / (x[np.where(x == x_threshold)[0][0] + 1] - x_threshold)
        functions.append(lambda x: slope * (x - x_threshold) + y_threshold)
        if x_threshold == x_thresholds[-2]:
            functions.append(lambda x: slope * (x - x_threshold) + y_threshold)
    
    # create a boolean mask for each function
    masks = []
    for x_threshold in x_thresholds[:-1]:
        masks.append(x > x_threshold)
        if x_threshold == x_thresholds[-2]:
            masks.append(x_thresholds[-1] > x > x_threshold)

    # apply the masks
    y_approx = np.piecewise(x, masks, functions)
    return y_approx      



def main():
    # read the csv
    data = pd.read_csv(INP_PATH)
    x = data[data.columns[0]].values
    ys = {}  # dictionary for all y values
    for col in data.columns[1:]:
        ys[col] = data[col].values

    # piecewise linear approximation
    x_thresholds = [-20, 25, 40, 55, 125, 150]
    linear_spline = piecewiselin_approximation(x, ys[1], x_thresholds)
    print(linear_spline)

