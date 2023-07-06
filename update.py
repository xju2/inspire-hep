import os
import time
import glob
import re
from typing import List, Any

from inspirehep import InspireHepLiterature
from writer import PublicationWriter

from mypub import inspire_ids


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="update my publication")
    add_arg = parser.add_argument
    add_arg("-o", '--outdir', help="output directory", default='publications')
    add_arg("-m", '--mode', help="update mode", default='u', choices=['a', 'u'])
    add_arg("-w", '--workers', help="number of workers", default=1, type=int)
    args = parser.parse_args()

    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    time_stamp = time.strftime('%Y%m%d-%H%M%S', time.localtime())

    inspire_hep = InspireHepLiterature(args.workers)
    writer = PublicationWriter(inspire_hep, outdir=outdir, mode=args.mode)
    writer.add_all(inspire_ids)
    writer.write()
