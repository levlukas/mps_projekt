from matplotlib import pyplot as plt
import pandas as pd
import os

INP_PATHS = ['temp/0_experiment_0.csv', 'temp/0_experiment_1.csv']
SERIES_NAMES = ['Experiment 0', 'Experiment 1']  # Names for each series
LTSPICE_FILE_NAME = "combined_plot"
X_AXIS_TITLE = "X-Axis"
Y_AXIS_TITLE = "Y-Axis"
LOG_X_AXIS = False  # Set to True to use a logarithmic scale for the x-axis
LOG_Y_AXIS = False  # Set to True to use a logarithmic scale for the y-axis

def plot_csv(inp_path, series_name):
    # Read the CSV file, skipping the second line (additional data)
    data = pd.read_csv(inp_path, skiprows=[1])
    print(f'Processing file: {inp_path}')
    print(f'Pandas has read the following columns: {data.columns}')

    x_axis = data.columns[0]
    for col in data.columns[1:]:
        plt.plot(data[x_axis], data[col], label=f'{series_name}: {col}')

def main():
    # Check if all input files exist
    if len(INP_PATHS) != len(SERIES_NAMES):
        raise ValueError("The number of input paths must match the number of series names.")

    for inp_path in INP_PATHS:
        if not os.path.exists(inp_path):
            raise FileNotFoundError(f'File {inp_path} does not exist')

    # Create the plot
    plt.figure()
    for inp_path, series_name in zip(INP_PATHS, SERIES_NAMES):
        plot_csv(inp_path, series_name)

    # Customize the plot
    plt.xlabel(X_AXIS_TITLE)
    plt.ylabel(Y_AXIS_TITLE)
    if LOG_X_AXIS:
        plt.xscale('log')
    if LOG_Y_AXIS:
        plt.yscale('log')
    plt.legend()
    plt.tight_layout()

    # Save the plot
    if not os.path.exists('temp'):
        os.mkdir('temp')
    plt.savefig(f'temp/{LTSPICE_FILE_NAME}.png')
    print(f'Plot saved as temp/{LTSPICE_FILE_NAME}.png')

if __name__ == '__main__':
    main()
