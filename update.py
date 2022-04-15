import os
import time
from citations import citations
from mypub import inspire_ids

def backup(filename, timeinfo):
    os.makedirs('backup')
    if os.path.exists(filename):
        os.rename(filename, os.path.join('backup', filename+".{}".format(timeinfo)))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="update my publication")
    add_arg = parser.add_argument
    add_arg("outdir", help="output directory")
    add_arg("-b", "--backup", help="backup existing files")
    args = parser.parse_args()

    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    time_stamp = time.strftime('%Y%m%d-%H%M%S', time.localtime())

    out_bib = ""
    columns = ["texkeys", 'arxiv_eprints', 'preprint_date', 'citation_count', "citation_count_without_self_citations", 'doi', 'title']
    data = []

    for inspire_id in inspire_ids:
        print("procesing {}".format(inspire_id))
        try:
            res = citations('literature', inspire_id)
        except Exception as inst:
            print(type(inst), inst.args)
            print("Skipping {}".format(inspire_id))
            continue

        info = [str(res[x]) for x in columns]
        info[-1] = '"{}"'.format(info[-1])
        data.append(info)
        out_bib += res['bibtex'] + "\n"

    bib_outname = os.path.join(outdir, 'mypub.bib')
    if args.backup:
        backup(bib_outname, time_stamp)
    with open(bib_outname, 'w') as f:
        f.write(out_bib)

    pub_outname = os.path.join(outdir, "mypub.csv")
    if args.backup:
        backup(pub_outname, time_stamp)

    # print(data)
    out = ",".join(columns) + "\n"
    out += '\n'.join([", ".join(x) for x in data])
    with open(pub_outname, 'w') as f:
        f.write(out)