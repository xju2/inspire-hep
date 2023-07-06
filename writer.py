import os
import re
import glob
from typing import List
from inspirehep import InspireHepLiterature
from paper import PaperData

class PublicationWriter:
    def __init__(self, inpire_hep: InspireHepLiterature, outdir: str, mode='u'):
        self.inpire_hep = inpire_hep
        self.outdir = outdir
        self.mode = mode

        # save bibtex data
        self.bib_data = []
        # save publication data for personal website
        self.pub_data = []

    def add(self, record_id: int):
        paper_info = self.inpire_hep.get(record_id)
        bib_entry = paper_info.bibtex
        self.bib_data.append(bib_entry)

        self.pub_data.append(self.generate_pub_data(paper_info))

    def generate_pub_data(self, paper_info: PaperData):
        title = paper_info.title
        title = title.replace("\\", "\\\\")  # escape backslash

        # use the doi url as the link if possible
        if paper_info.doi != "N/A":
            link = f"https://doi.org/{paper_info.doi}"
        else:
            link = f"https://inspirehep.net/literature/{paper_info.inspire_id}"

        date = paper_info.preprint_date
        # if date is not in the format of YYYY-MM-DD, add '-01' to the end
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            date += "-01"

        venue = paper_info.cite_info
        inspire_id = paper_info.inspire_id

        authors = paper_info.authors
        if len(authors) > 3:
            authors = authors[:3] + [" et al."]
        authors = ', '.join(authors)

        out = '\n'.join([
            '---',
            f'title: "{title}"',
            f"date: {date}",
            f"venue: {venue}",
            f"link: {link}",
            f'inspire_id: {inspire_id}',
            f"authors: {authors}",
            f"bibtex: {repr(paper_info.bibtex)}",
            '---'
        ])
        return [date, out]

    def add_all(self, record_ids: List[int]):
        for recid in record_ids:
            self.add(recid)

    def write(self):
        mode = 'a' if self.mode == 'a' else 'w'
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
