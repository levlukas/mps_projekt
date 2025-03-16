from matplotlib import pyplot as plt
import pandas as pd
import os

INP_PATH = f'./plot_parser/temp/1b_experiment.csv'
LTSPICE_FILE_NAME = INP_PATH.split('/')[-1].split('.')[0]

def plot_csv(inp_path):
    data = pd.read_csv(inp_path)
    print(f'Pandas has read the following columns: {data.columns}')

    # plot
    plt.figure()
    x_axis = data.columns[0]
    for col in data.columns[1:]:
        plt.plot(data[x_axis], data[col], label=col)

    plt.legend()
    plt.title(f'LTspice simulation: {LTSPICE_FILE_NAME}')

    # save plot
    if not os.path.exists('./plot_parser/temp'):
        os.mkdir('./plot_parser/temp')
    plt.savefig(f'./plot_parser/temp/{LTSPICE_FILE_NAME}.png')

def main():
    if not os.path.exists(INP_PATH):
        NameError(f'File {INP_PATH} does not exist')    
    plot_csv(INP_PATH)
    print(f'Plot saved as {LTSPICE_FILE_NAME}.png')

if __name__ == '__main__':
    main()
