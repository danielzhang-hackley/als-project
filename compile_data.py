import numpy as np
import pandas as pd


def convert_scheme(data, from_key, to_key):
    output = np.empty(data.shape[0])
    for i, name in enumerate(data):
        idx = np.where(from_key == name)[0]
        output[i] = to_key[idx]

    return output


def format_go():
    go = pd.read_csv('data/goa_human.gaf', sep='\t', skiprows=41)


def format_ppi():
    ppi = pd.read_csv('data/9606.protein.links.full.v10.5.txt', sep=' ')
    # keys = pd.read_csv('data/meta/human.name_2_string.tsv', sep='\t', skiprows=1)

    ppi = ppi.iloc[:, 0:2]
    print(ppi.shape)
    print(ppi)


def format_pathdip():
    pass


def main():
    format_ppi()


if __name__ == '__main__':
    print('\033c')
    main()
