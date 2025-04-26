from matplotlib import pyplot as plt
import pandas as pd
import os

INP_PATHS = ['temp/0_experiment_0.csv', 'temp/0_experiment_1.csv', 'temp/0_experiment_2.csv']
SERIES_NAMES = ['Vcc = 5 V', 'Vcc = 15 V', 'Vcc = 36 V']  # Names for each series
SERIES_COLORS = ['blue', 'green', 'red']  # Colors for each series
LTSPICE_FILE_NAME = "experiment_1b"
X_AXIS_TITLE = "$R_{load}$"
Y_AXIS_TITLE = "$I_{load}$"
X_AXIS_UNIT = "$\Omega$"  # Unit for the x-axis (optional)
Y_AXIS_UNIT = "A"  # Unit for the y-axis (optional)
LOG_X_AXIS = True  # Set to True to use a logarithmic scale for the x-axis
LOG_Y_AXIS = False  # Set to True to use a logarithmic scale for the y-axis
ENABLE_PRIMARY_GRID = True  # Set to True to enable primary grid
ENABLE_SECONDARY_GRID = True  # Set to True to enable secondary grid
ENGINEERING_NOTATION_X = False  # Enable engineering notation for the x-axis
ENGINEERING_NOTATION_Y = True  # Enable engineering notation for the y-axis

SI_PREFIXES = {
    -15: 'f', -12: 'p', -9: 'n', -6: 'u', -3: 'm', 0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T'
}

def convert_to_engineering_notation(values):
    """Convert values to engineering notation."""
    factor = 0
    while values.max() < 1 and factor > -15:
        values *= 1000
        factor -= 3
    while values.max() >= 1000 and factor < 12:
        values /= 1000
        factor += 3
    return values, SI_PREFIXES.get(factor, '')

def plot_csv(inp_path, series_name, color):
    # Read the CSV file, skipping the second line (additional data)
    data = pd.read_csv(inp_path, skiprows=[1])
    print(f'Processing file: {inp_path}')
    print(f'Pandas has read the following columns: {data.columns}')

    x_axis = data.columns[0]
    for col in data.columns[1:]:
        x_values = data[x_axis]
        y_values = data[col]

        # Apply engineering notation if enabled for each axis
        if ENGINEERING_NOTATION_X:
            x_values, x_prefix = convert_to_engineering_notation(x_values)
        else:
            x_prefix = ''
        if ENGINEERING_NOTATION_Y:
            y_values, y_prefix = convert_to_engineering_notation(y_values)
        else:
            y_prefix = ''

        # Plot the data
        plt.plot(x_values, y_values, label=f'{series_name}: {col}', color=color)

    return x_prefix, y_prefix  # Return prefixes for axis titles

def main():
    # Check if all input files exist
    if len(INP_PATHS) != len(SERIES_NAMES) or len(INP_PATHS) != len(SERIES_COLORS):
        raise ValueError("The number of input paths, series names, and series colors must match.")

    for inp_path in INP_PATHS:
        if not os.path.exists(inp_path):
            raise FileNotFoundError(f'File {inp_path} does not exist')

    # Create the plot
    plt.figure()
    x_prefix, y_prefix = '', ''  # Initialize prefixes
    for inp_path, series_name, color in zip(INP_PATHS, SERIES_NAMES, SERIES_COLORS):
        x_prefix, y_prefix = plot_csv(inp_path, series_name, color)

    # Update axis titles with units and prefixes (only once)
    global X_AXIS_TITLE, Y_AXIS_TITLE
    if X_AXIS_UNIT:
        X_AXIS_TITLE = f"{X_AXIS_TITLE} [{x_prefix}{X_AXIS_UNIT}]"
    if Y_AXIS_UNIT:
        Y_AXIS_TITLE = f"{Y_AXIS_TITLE} [{y_prefix}{Y_AXIS_UNIT}]"

    # Customize the plot
    plt.xlabel(X_AXIS_TITLE)
    plt.ylabel(Y_AXIS_TITLE)
    if LOG_X_AXIS:
        plt.xscale('log')
    if LOG_Y_AXIS:
        plt.yscale('log')

    # Add grids
    if ENABLE_PRIMARY_GRID:
        plt.grid(which='major', linestyle='-', linewidth=0.75, alpha=0.7)
    if ENABLE_SECONDARY_GRID:
        plt.minorticks_on()
        plt.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

    plt.legend()
    plt.tight_layout()

    # Save the plot
    if not os.path.exists('temp'):
        os.mkdir('temp')
    plt.savefig(f'temp/{LTSPICE_FILE_NAME}.png', dpi=300, bbox_inches='tight')
    print(f'Plot saved as temp/{LTSPICE_FILE_NAME}.png')

if __name__ == '__main__':
    main()
