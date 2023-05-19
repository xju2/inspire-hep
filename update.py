import os
import time
import glob
import re
from citations import citations
from mypub import inspire_ids
import bibtexparser
import datetime


def get_link(bib_str):
    bib_entry = bibtexparser.loads(bib_str)
    bib_entry = bib_entry.entries[0]

    if 'doi' in bib_entry:
        return f"https://doi.org/{bib_entry['doi']}"
    elif 'arxiv_eprint' in bib_entry:
        return f"https://arxiv.org/abs/{bib_entry['arxiv_eprint']}"
    elif 'eprint' in bib_entry:
        return f"https://arxiv.org/abs/{bib_entry['eprint']}"
    else:
        return None


def get_citation_info(bib_str):
    bib_entry = bibtexparser.loads(bib_str)
    bib_entry = bib_entry.entries[0]
    if "journal" in bib_entry:
        j_data = [bib_entry['journal'], bib_entry['volume'],
                  f"({bib_entry['year']})"]
        if "numbers" in bib_entry:
            j_data.append(f"no.{bib_entry['numbers']}")
        if "pages" in bib_entry:
            j_data.append(f"{bib_entry['pages']}")
        journal = " ".join(j_data)
    elif "eprint" in bib_entry:
        journal = f"arxiv:{bib_entry['eprint']}"
    else:
        journal = None
    return journal

def fix_title(title):
    title = title.replace("\\", "\\\\")
    return title

def fix_date(date_text):
    new_date = date_text
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        # <TODO> more date formats
        new_date = date_text + "-01"
    return new_date


def get_pub_info(paper_info):
    title = fix_title(paper_info['title'])
    link = get_link(paper_info['bibtex'])
    date = fix_date(paper_info['preprint_date'])
    venue = get_citation_info(paper_info['bibtex'])
    inspire_id = paper_info['inspire_id']

    out = '\n'.join([
        '---',
        f'title: "{title}"',
        f"date: {date}",
        f"venue: {venue}",
        f"link: {link}",
        f'inspire_id: {inspire_id}',
        '---'
    ])
    return [date, out]

class csv_handler(object):
    def __init__(self, outdir, mode='u'):
        self.outdir = outdir
        self.mode = mode
        self.columns = [
            "texkeys", 'arxiv_eprints', 'preprint_date',
            'citation_count', "citation_count_without_self_citations",
            'doi', 'title']
        # save all publication info into csv
        self.csv_data = []

        # save bibtex data
        self.bib_data = []
        # save publication data for personal website
        self.pub_data = []

    def add(self, paper_info):
        info = [str(paper_info[x]) for x in self.columns]
        info[-1] = '"{}"'.format(info[-1])
        self.csv_data.append(info)
        bib_entry = paper_info['bibtex']
        self.bib_data.append(bib_entry)
        self.pub_data.append(get_pub_info(paper_info))

    def write(self):
        # write csv file
        mode = 'a' if self.mode == 'a' else 'w'
        with open(os.path.join(self.outdir, 'mypub.csv'), mode) as f:
            if self.mode != 'a':
                f.write(','.join(self.columns) + "\n")
            f.write('\n'.join(','.join(x) for x in self.csv_data))

        # write bib file
        with open(os.path.join(self.outdir, 'mypub.bib'), mode) as f:
            f.write('\n'.join(self.bib_data))

        # write pub file
        pattern = re.compile(r'.*p([0-9]*).md')
        pub_md_idx = max([int(pattern.search(os.path.basename(x)).groups()[0])
                          for x in glob.glob(self.outdir + "/*.md")]) if self.mode == 'a' else 0

        for idx, pub in enumerate(reversed(self.pub_data)):
            index = pub_md_idx + idx + 1
            with open(os.path.join(self.outdir, f"{pub[0]}-p{index}.md"), 'w') as f:
                f.write(pub[1])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="update my publication")
    add_arg = parser.add_argument
    add_arg("-o", '--outdir', help="output directory", default='publications')
    add_arg("-m", '--mode', help="update mode", default='a', choices=['a', 'u'])
    args = parser.parse_args()

    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    time_stamp = time.strftime('%Y%m%d-%H%M%S', time.localtime())

    writer = csv_handler(outdir=outdir, mode=args.mode)

    for inspire_id in inspire_ids:
        print("procesing {}".format(inspire_id))
        try:
            res = citations('literature', inspire_id)
        except Exception as inst:
            print(type(inst), inst.args)
            print("Skipping {}".format(inspire_id))
            continue

        writer.add(res)

    writer.write()
