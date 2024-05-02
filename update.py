import time
from pathlib import Path

from mypub import inspire_ids
from writer import PublicationWriter

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="update my publication")
    add_arg = parser.add_argument
    add_arg("-o", "--outdir", help="output directory", default="publications")
    add_arg("-m", "--mode", help="update mode", default="u", choices=["a", "u"])
    add_arg("-w", "--workers", help="number of workers", default=1, type=int)
    args = parser.parse_args()

    outdir = args.outdir
    Path(outdir).mkdir(exist_ok=True)

    time_stamp = time.strftime("%Y%m%d-%H%M%S", time.localtime())

    writer = PublicationWriter(outdir=outdir, mode=args.mode)
    record_ids = [str(i) for i in inspire_ids]
    writer.add_all(record_ids)
    writer.write()
    writer.save()
