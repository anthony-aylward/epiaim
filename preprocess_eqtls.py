import funcgenom
import os
import sys
import pickle

sys.path.append('/home/data/kglab-python3-modules')
import colocalize

from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser(description='preprocess islet eQTL data')
    parser.add_argument(
        'gene_ids',
        metavar='gene_ids.txt',
        help='gene ids'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    genome = funcgenom.Genome()
    with open(args.gene_ids, 'r') as f:
        gene_ids = f.read().splitlines()
    colocalize.load_islet_eqtl_data(genome, *gene_ids, processes=23, graceful=True)
    with open('test.p', 'wb') as f:
        pickle.dump(genome, f)


if __name__ == '__main__':
    main()
