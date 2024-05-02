from __future__ import annotations

import dataclasses
import json
import re
from pathlib import Path

from arxiv import get_arxiv_data
from cds import get_cds_data
from inspirehep import get_inspire_data
from paper import PaperData


class PublicationWriter:
    def __init__(self, outdir: str | Path, mode="u"):
        self.outdir = Path(outdir)
        self.mode = mode

        self.local_data_name = ".localdatabase.json"
        self.local_data = {}
        if Path(self.local_data_name).exists():
            with open(self.local_data_name) as f:
                self.local_data = json.load(f)

        # save bibtex data
        self.bib_data = []
        # save publication data for personal website
        self.pub_data = []

    def add(self, record_id: str | int):
        paper_info: PaperData = None
        if str(record_id) in self.local_data:
            paper_data = self.local_data.get(str(record_id))
            paper_info = PaperData(**paper_data)
        else:
            if record_id[:3] == "cds":
                paper_info = get_cds_data(record_id)
            else:
                paper_info = get_arxiv_data(str(record_id))
                if paper_info is None:
                    # try inspire hep
                    paper_info = get_inspire_data(record_id)
            self.local_data[record_id] = dataclasses.asdict(paper_info)

        bib_entry = paper_info.bibtex
        self.bib_data.append(bib_entry)
        self.pub_data.append(self.generate_pub_data(paper_info))

    def generate_pub_data(self, paper_info: PaperData):
        title = paper_info.title
        title = title.replace("\\", "\\\\")  # escape backslash

        # use the doi url as the link if possible
        if paper_info.doi != "N/A":
            link = f"https://doi.org/{paper_info.doi}"
        elif paper_info.inspire_id != "N/A":
            link = f"https://inspirehep.net/literature/{paper_info.inspire_id}"
        else:
            link = f"https://arxiv.org/abs/{paper_info.arxiv_eprints}"

        date = paper_info.preprint_date
        # if date is not in the format of YYYY-MM-DD, add '-01' to the end
        if not re.match(r"\d{4}-\d{2}-\d{2}", date):
            date += "-01"

        venue = paper_info.cite_info.replace("arxiv", "arXiv")
        inspire_id = paper_info.inspire_id

        authors = paper_info.authors
        if len(authors) > 3:
            authors = authors[:3] + [" et al."]
        authors = ", ".join(authors)

        out = "\n".join([
            "---",
            f'title: "{title}"',
            f"date: {date}",
            f"venue: {venue}",
            f"link: {link}",
            f"inspire_id: {inspire_id}",
            f"authors: {authors}",
            f"bibtex: {paper_info.bibtex!r}",
            "---",
        ])
        return [date, out]

    def add_all(self, record_ids: list[int]):
        for recid in record_ids:
            self.add(recid)

    def write(self):
        mode = "a" if self.mode == "a" else "w"
        # write bib file
        with open(self.outdir / "mypub.bib", mode) as f:
            f.write("\n".join(self.bib_data))

        # write pub file
        pattern = re.compile(r".*p([0-9]*).md")
        pub_md_idx = (
            max([
                int(pattern.search(Path(x).name).groups()[0])
                for x in self.outdir.glob("*.md")
            ])
            if self.mode == "a"
            else 0
        )

        for idx, pub in enumerate(reversed(self.pub_data)):
            index = pub_md_idx + idx + 1
            with open(self.outdir / f"{pub[0]}-p{index}.md", "w") as f:
                f.write(pub[1])

    def save(self):
        with open(self.local_data_name, "w") as f:
            json.dump(self.local_data, f)
