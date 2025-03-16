import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

INP_PATH = f'./plot_parser/temp/1a_Iout_temp-stab.csv'

def piecewiselin_approximation(x, y, x_thresholds):
    functions = []  
    masks = []
    
    for i in range(len(x_thresholds) - 1):
        x_t1, x_t2 = x_thresholds[i], x_thresholds[i + 1]
        
        # Find the corresponding y-values
        idx1 = np.searchsorted(x, x_t1)
        idx2 = np.searchsorted(x, x_t2)

        if idx1 >= len(x) or idx2 >= len(x):
            continue  # Skip if thresholds are out of range

        y_t1, y_t2 = y[idx1], y[idx2]
        
        # Compute slope
        slope = (y_t2 - y_t1) / (x_t2 - x_t1)
        
        # Define the piecewise function using default arguments to capture values
        functions.append(lambda x, s=slope, xt1=x_t1, yt1=y_t1: s * (x - xt1) + yt1)

        # Create corresponding mask
        masks.append(np.logical_and(x >= x_t1, x < x_t2))

    # Ensure last mask includes last point
    masks.append(x >= x_thresholds[-1])
    functions.append(lambda x: y[-1])  # Assume constant at the last point

    # Apply piecewise function
    y_approx = np.piecewise(x, masks, functions)
    
    return y_approx



def main():
    # read the csv
    data = pd.read_csv(INP_PATH)
    x = data[data.columns[0]].values
    ys = {}  # dictionary for all y values
    for col in data.columns[1:]:
        ys[col] = data[col].values
    print("Pandas has read the following columns: ", data.columns)

    y = ys['I(Rload)']
    # comment if not interactive
    # y = ys[input("Choose the column to approximate: ")]

    # piecewise linear approximation
    x_thresholds = [-20, 25, 40, 55, 125, 150]
    linear_spline = piecewiselin_approximation(x, y, x_thresholds)
    print(linear_spline)
    plt.plot(x, linear_spline, label='Approximation')
    plt.savefig('./fig1.png')
    plt.plot(x, y, label='Original')
    plt.savefig('./fig2.png')

if __name__ == '__main__':
    main()
