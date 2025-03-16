"""
Reads ltspice planetext file and outputs it as csv to temp folder in plot_parser dir.
"""
import os
import pandas as pd

INP_PATH = f'/home/llev/OneDrive/4_letni/MPS/mps_projekt/1_experiment/1a/1a_Iout_temp-stab.txt'
LTSPICE_FILE_NAME = INP_PATH.split('/')[-1].split('.')[0]

def ltspice_to_csv(inp_path):
    with open(inp_path, 'r') as f:
        lines = f.readlines()

    # replace \t with commas
    lines = [line.replace('\t', ',') for line in lines]

    return lines
        

def main():
    if not os.path.exists(INP_PATH):
        NameError(f'File {INP_PATH} does not exist')    
    # print(ltspice_to_csv(INP_PATH))  # debug

    # save to csv
    if not os.path.exists('./plot_parser/temp'):
        os.mkdir('./plot_parser/temp')
    with open(f'./plot_parser/temp/{LTSPICE_FILE_NAME}.csv','w') as f:
        f.writelines(ltspice_to_csv(INP_PATH))

    

if __name__ == '__main__':
    main()
