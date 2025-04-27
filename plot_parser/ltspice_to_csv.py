"""
Reads ltspice planetext file and outputs it as csv to temp folder in plot_parser dir.
"""
import os
import pandas as pd

INP_PATH = f'../1_experiment/1a/ltspice/1a_experiment_Vref.txt'
LTSPICE_FILE_NAME = INP_PATH.split('/')[-1].split('.')[0]

def ltspice_to_csv(inp_path):
    with open(inp_path, 'r') as f:
        lines = f.readlines()

    # replace \t with commas
    lines = [line.replace('\t', ',') for line in lines]

    return lines

def secondary_parser(inp_path:str):
    """
    in order to parse the output of ltspice_to_csv()
    - helpful when more than one param was .stepped
    """ 
    no_step_lines = []       
    header = ''

    with open(inp_path, 'r') as f:
        lines = f.readlines()
        header = lines[0]
        for i, line in enumerate(lines):
            if "Step Information:" in line:
                no_step_lines.append(i)
    
    no_step_lines.append(len(lines))  # add last line
    if no_step_lines:
        for i in range(len(no_step_lines)-1):
            with open(inp_path[:-4]+f'_{i}.csv', 'w') as f:
                f.write(header)
                f.writelines(lines[no_step_lines[i]:no_step_lines[i+1]])



def main():
    if not os.path.exists(INP_PATH):
        NameError(f'File {INP_PATH} does not exist')    
    # print(ltspice_to_csv(INP_PATH))  # debug

    # save to csv
    if not os.path.exists('temp'):
        os.mkdir('temp')
    with open(f'temp/{LTSPICE_FILE_NAME}.csv','w') as f:
        f.writelines(ltspice_to_csv(INP_PATH))

    # parse secondary
    secondary_parser(f'temp/{LTSPICE_FILE_NAME}.csv')
    print(f'File saved as {LTSPICE_FILE_NAME}.csv')   

if __name__ == '__main__':
    main()
