#!/usr/bin/python
import arxiv
from citations import citations
from multiprocessing import Pool
from functools import partial

def process(inspire_id, info_type, debug=False):
    if debug:
        print(f"procesing {info_type} with id {inspire_id}")
    try:
        if info_type == "arxiv":
            res = citations('arxiv', inspire_id, debug=debug)
        else:
            res = citations('literature', inspire_id)
    except Exception as inst:
        print(type(inst), inst.args)
        print("Skipping {}".format(inspire_id))

    return res['bibtex']


if __name__ == "__main__":
    import os
    import time
    import argparse

    parser = argparse.ArgumentParser(description="get bib for a list of articles")
    add_arg = parser.add_argument
    add_arg("filename", help='input file containing arxiv ids')
    add_arg("-t", "--type", help='entry information', default='arxiv', choices=['inspire', 'arxiv'])
    add_arg("-d", "--debug", action='store_true', help="in a debug mode")
    add_arg('-o', '--outname', help='output filename', default=None)
    add_arg('-w', '--workers', default=1, type=int, help="number of processes")
    args = parser.parse_args()

    filename = args.filename
    debug = args.debug
    info_type = args.type
    outname = args.outname
    workers = args.workers

    if not os.path.exists(filename):
        print(f"{filename} does not exit.")
        exit(0)

    print(f"Input information type: {info_type}")
    with open(filename, 'r') as f:
        if info_type == 'arxiv':
            inspire_ids = [
                arxiv.find_index(line[:-1] if '\n' in line else line)
                for line in f if line[0] != '#']
        else:
            inspire_ids = [line[:-1] if '\n' in line else line for line in f if line[0] != '#']
    

    time_stamp = time.strftime('%Y%m%d-%H%M%S', time.localtime())

    if workers < 2:
        out_bib = [process(idx, info_type, debug) for idx in inspire_ids]
    else:
        # multiprocessing
        with Pool(workers) as p:
            out_bib = p.map(partial(process, info_type=info_type, debug=debug), inspire_ids)


    if outname is None:
        print('\n'.join(out_bib))
    else:
        with open(outname, 'w') as f:
            f.write('\n'.join(out_bib))