import os
import time
from citations import citations
from mypub import inspire_ids
import bibtexparser

def backup(filename, timeinfo):
    os.makedirs('backup')
    if os.path.exists(filename):
        os.rename(filename, os.path.join('backup', filename+".{}".format(timeinfo)))

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
            j_data.append(f"pp.{bib_entry['pages']}")
        journal = " ".join(j_data)
    elif "eprint" in bib_entry:
        journal = f"arxiv:{bib_entry['eprint']}"
    else:
        journal = None
    return journal

def get_pub_info(paper_info):
    title = paper_info['title']
    link = get_link(paper_info['bibtex'])
    date = paper_info['preprint_date']
    venue = get_citation_info(paper_info['bibtex'])

    out = '\n'.join([
        '---',
        f"title: {title}",
        f"date: {date}",
        f"venue: {venue}",
        f"link: {link}",
        '---'
        ])
    return [date, out]
   
class csv_handler(object):
    def __init__(self, outdir):
        self.outdir = outdir
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
        with open(os.path.join(self.outdir, 'mypub.csv'), 'w') as f:
            f.write('\n'.join(','.join(x) for x in self.csv_data))

        # write bib file
        with open(os.path.join(self.outdir, 'mypub.bib'), 'w') as f:
            f.write('\n'.join(self.bib_data))

        # write pub file
        for idx,pub in enumerate(reversed(self.pub_data)):
            index = idx + 1
            with open(os.path.join(self.outdir, f"{pub[0]}-p{index}.md"), 'w') as f:
                f.write(pub[1])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="update my publication")
    add_arg = parser.add_argument
    add_arg("-o", '--outdir', help="output directory", default='data')
    add_arg("-b", "--backup", help="backup existing files")
    args = parser.parse_args()

    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    time_stamp = time.strftime('%Y%m%d-%H%M%S', time.localtime())

    writer = csv_handler(outdir=outdir)

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