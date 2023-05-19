#!/usr/bin/env python
"""Summarize your publications
"""

if __name__ == '__main__':
    import os
    import pandas as pd
    import argparse
    parser = argparse.ArgumentParser(description='Summarize your publications')
    add_arg = parser.add_argument
    add_arg('-i', '--input', help='input file', default='publications/mypub.csv')

    args = parser.parse_args()

    if os.path.exists(args.input):
        df = pd.read_csv(args.input)
    else:
        exit(1)

    tot_pub = df.shape[0]
    tot_citation = df['citation_count'].sum()
    print("Total {:,} publications with {:,} of citations".format(
        tot_pub, tot_citation))
