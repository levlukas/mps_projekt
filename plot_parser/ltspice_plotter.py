from matplotlib import pyplot as plt
import pandas as pd
import os

INP_PATHS = ['../2_experiment/data/irload.csv','../2_experiment/data/sqrt_s_ntot.csv']
SERIES_NAMES = ['$I_{load}$', '$I_{ef}$']  # Names for each series
SERIES_COLORS = ['blue', 'green']  # Colors for each series
SECONDARY_AXIS_SERIES = [False, True]  # Specify True for series to be plotted on the secondary y-axis
LTSPICE_FILE_NAME = "2_experiment_irload_ief"
X_AXIS_TITLE = r"$f$"
Y_AXIS_TITLE = "$I_{load}$, proud zátěží"
Y_AXIS_SECONDARY_TITLE = "$I_{ef}$, šumový proud"
X_AXIS_UNIT = "Hz"  # Unit for the x-axis (optional)
Y_AXIS_UNIT = r"A"  # Unit for the primary y-axis (optional)
Y_AXIS_SECONDARY_UNIT = r"A"  # Unit for the secondary y-axis (optional)
LOG_X_AXIS = False  # Set to True to use a logarithmic scale for the x-axis
LOG_Y_AXIS = False  # Set to True to use a logarithmic scale for the primary y-axis
LOG_Y_AXIS_SECONDARY = False  # Set to True to use a logarithmic scale for the secondary y-axis
ENABLE_PRIMARY_GRID = True  # Set to True to enable primary grid
ENABLE_SECONDARY_GRID = True  # Set to True to enable secondary grid
ENGINEERING_NOTATION_X = True  # Enable engineering notation for the x-axis
ENGINEERING_NOTATION_Y = True  # Enable engineering notation for the primary y-axis
ENGINEERING_NOTATION_Y_SECONDARY = True  # Enable engineering notation for the secondary y-axis
ENABLE_LEGEND = True  # Set to True to enable legend

SI_PREFIXES = {
    -18: 'a', -15: 'f', -12: 'p', -9: 'n', -6: 'u', -3: 'm', 0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T'
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

def plot_csv(ax, ax_secondary, inp_path, series_name, color, secondary_axis):
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
        if secondary_axis and ENGINEERING_NOTATION_Y_SECONDARY:
            y_values, y_prefix = convert_to_engineering_notation(y_values)
        elif not secondary_axis and ENGINEERING_NOTATION_Y:
            y_values, y_prefix = convert_to_engineering_notation(y_values)
        else:
            y_prefix = ''

        # Plot the data on the appropriate axis
        if secondary_axis:
            ax_secondary.plot(x_values, y_values, label=f'{series_name}: {col}', color=color)
        else:
            ax.plot(x_values, y_values, label=f'{series_name}: {col}', color=color)

    return x_prefix, y_prefix  # Return prefixes for axis titles

def main():
    # Check if all input files exist
    if len(INP_PATHS) != len(SERIES_NAMES) or len(INP_PATHS) != len(SERIES_COLORS) or len(INP_PATHS) != len(SECONDARY_AXIS_SERIES):
        raise ValueError("The number of input paths, series names, series colors, and secondary axis flags must match.")

    for inp_path in INP_PATHS:
        if not os.path.exists(inp_path):
            raise FileNotFoundError(f'File {inp_path} does not exist')

    # Check if any series is assigned to the secondary axis
    use_secondary_axis = any(SECONDARY_AXIS_SERIES)

    # Create the plot
    fig, ax = plt.subplots()
    ax_secondary = ax.twinx() if use_secondary_axis else None  # Create a secondary y-axis only if needed
    x_prefix, y_prefix, y_secondary_prefix = '', '', ''  # Initialize prefixes

    for inp_path, series_name, color, secondary_axis in zip(INP_PATHS, SERIES_NAMES, SERIES_COLORS, SECONDARY_AXIS_SERIES):
        if secondary_axis and use_secondary_axis:
            x_prefix, y_secondary_prefix = plot_csv(ax, ax_secondary, inp_path, series_name, color, secondary_axis=True)
        else:
            x_prefix, y_prefix = plot_csv(ax, ax_secondary, inp_path, series_name, color, secondary_axis=False)

    # Update axis titles with units and prefixes (only once)
    global X_AXIS_TITLE, Y_AXIS_TITLE, Y_AXIS_SECONDARY_TITLE
    if X_AXIS_UNIT:
        X_AXIS_TITLE = f"{X_AXIS_TITLE} [{x_prefix}{X_AXIS_UNIT}]"
    if Y_AXIS_UNIT:
        Y_AXIS_TITLE = f"{Y_AXIS_TITLE} [{y_prefix}{Y_AXIS_UNIT}]"
    if use_secondary_axis and Y_AXIS_SECONDARY_UNIT:
        Y_AXIS_SECONDARY_TITLE = f"{Y_AXIS_SECONDARY_TITLE} [{y_secondary_prefix}{Y_AXIS_SECONDARY_UNIT}]"

    # Customize the plot
    ax.set_xlabel(X_AXIS_TITLE)
    ax.set_ylabel(Y_AXIS_TITLE)
    if use_secondary_axis:
        ax_secondary.set_ylabel(Y_AXIS_SECONDARY_TITLE)
    if LOG_X_AXIS:
        ax.set_xscale('log')
        if use_secondary_axis:
            ax_secondary.set_xscale('log')
    if LOG_Y_AXIS:
        ax.set_yscale('log')
    if use_secondary_axis and LOG_Y_AXIS_SECONDARY:
        ax_secondary.set_yscale('log')

    # Add grids
    if ENABLE_PRIMARY_GRID:
        ax.grid(which='major', linestyle='-', linewidth=0.75, alpha=0.7)
    if ENABLE_SECONDARY_GRID:
        ax.minorticks_on()
        ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

    # Combine legends from both axes
    if ENABLE_LEGEND:
        handles_primary, labels_primary = ax.get_legend_handles_labels()
        if use_secondary_axis:
            handles_secondary, labels_secondary = ax_secondary.get_legend_handles_labels()
            handles = handles_primary + handles_secondary
            labels = labels_primary + labels_secondary
        else:
            handles, labels = handles_primary, labels_primary
        fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2)  # Common legend

    plt.tight_layout()

    # Save the plot
    if not os.path.exists('temp'):
        os.mkdir('temp')
    plt.savefig(f'temp/{LTSPICE_FILE_NAME}.png', dpi=300, bbox_inches='tight')
    print(f'Plot saved as temp/{LTSPICE_FILE_NAME}.png')

if __name__ == '__main__':
    main()
