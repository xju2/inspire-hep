import os
import bibtexparser
from bibtexparser.bwriter import BibTexWriter

def correct_lhc_authors(bib_tex):
    bib_data = bibtexparser.loads(bib_tex)
    entry = bib_data.entries[0]
    if "collaboration" in entry:
        # remove author and keep collaboration
        entry['author'] = ""

        # entry['author'] = entry['collaboration'] + " Collaboration"
        # print(entry['collaboration'])
        # del entry['collaboration']
    bib_data.entries = [entry]

    writer = BibTexWriter()
    return writer.write(bib_data)

def get_author_list(bib_str):
    bib_entry = bibtexparser.loads(bib_str)
    bib_entry = bib_entry.entries[0]

    if "author" in bib_entry and bib_entry["author"] != "":
        authors = bib_entry["author"].split("and")
        authors = [a.strip() for a in authors]
        new_authors = []
        for author in authors:
            if "," in author:
                author = author.split(",")
                author = f"{author[1].strip()} {author[0].strip()}"
            new_authors.append(author)
        return new_authors

    elif "collaboration" in bib_entry:
        return [bib_entry["collaboration"] + " Collaboration"]
    else:
        return None

def reformat(bib_file):
    if not os.path.exists(bib_file):
        print(f"{bib_file} does not exist.")

    with open(bib_file) as f:
        bib_data = bibtexparser.load(f)

    # change author to Collaborations
    # for entry in bib_data.entries:
    #     entry['author'] = entry['collaboration'] + " Collaboration"

    # write the updated bib into file
    writer = BibTexWriter()
    with open(bib_file, 'w') as f:
        f.write(writer.write(bib_data))

def get_paper_url(bib_str):
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


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Test')
    add_arg = parser.add_argument

    args = parser.parse_args()

    bib_tex = """@article{CMS:2019ybf,
    author = "Sirunyan, Albert M and others",
    collaboration = "CMS",
    title = "{Searches for physics beyond the standard model with the $M_\mathrm{T2}$ variable in hadronic final states with and without disappearing tracks in proton-proton collisions at $\sqrt{s}=$ 13 TeV}",
    eprint = "1909.03460",
    archivePrefix = "arXiv",
    primaryClass = "hep-ex",
    reportNumber = "CMS-SUS-19-005, CERN-EP-2019-180",
    doi = "10.1140/epjc/s10052-019-7493-x",
    journal = "Eur. Phys. J. C",
    volume = "80",
    number = "1",
    pages = "3",
    year = "2020"}
    """
    print(correct_lhc_authors(bib_tex=bib_tex))
