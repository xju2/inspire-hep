from __future__ import annotations

import dataclasses
import json
import re
from pathlib import Path

import tqdm

from arxiv import get_arxiv_data
from cds import get_cds_data
from inspirehep import get_inspire_data
from paper import PaperData


def generate_pub_data(paper_info: PaperData) -> str:
    title = paper_info.title
    title = title.replace("\\", "\\\\")  # escape backslash

    link = paper_info.url
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
    return out


class PublicationWriter:
    def __init__(self, outdir: str | Path, mode="u"):
        self.outdir = Path(outdir)
        self.mode = mode

        self.local_data_name = ".localdatabase.json"
        self.local_data = {}
        if Path(self.local_data_name).exists():
            with open(self.local_data_name) as f:
                self.local_data = json.load(f)

        # save output filename for each record_id.
        self.local_metadata_name = ".metadata.json"
        self.local_metadata = {}
        if Path(self.local_metadata_name).exists():
            with open(self.local_metadata_name) as f:
                self.local_metadata = json.load(f)
        else:
            self.local_metadata["TotalRecords"] = 0

        # save bibtex data
        self.bib_data = []
        # save publication data for personal website
        self.pub_data = []

    def add(self, record_id: str):
        paper_info: PaperData | None = None
        record_id = record_id.strip().lower()
        if record_id in self.local_data:
            paper_data = self.local_data.get(record_id)
            paper_info = PaperData(**paper_data)
        else:
            if "cds" in record_id:
                paper_info = get_cds_data(record_id)
            elif "arxiv" in record_id:
                paper_info = get_arxiv_data(record_id)
            else:
                paper_info = get_inspire_data(record_id)

            self.local_data[record_id] = dataclasses.asdict(paper_info)

        # save the output filename for each record_id
        date = paper_info.preprint_date
        # if date is not in the format of YYYY-MM-DD, add '-01' to the end
        if not re.match(r"\d{4}-\d{2}-\d{2}", date):
            date += "-01"

        if record_id not in self.local_metadata:
            self.local_metadata["TotalRecords"] += 1
            self.local_metadata[record_id] = f"{date}-p{self.local_metadata['TotalRecords']}.md"

        bib_entry = paper_info.bibtex
        self.bib_data.append(bib_entry)
        self.pub_data.append(paper_info)

    def add_all(self, record_ids: list[str]):
        for recid in tqdm.tqdm(reversed(record_ids), total=len(record_ids), desc="Adding records"):
            self.add(recid)

    def write(self):
        mode = "a" if self.mode == "a" else "w"
        # write bib file
        with open(self.outdir / "mypub.bib", mode) as f:
            f.write("\n".join(self.bib_data))

        # write pub file
        for pub in self.pub_data:
            if pub.record_id not in self.local_metadata:
                print(f"Warning: {pub.record_id} not found in local metadata. Skipping.")
                continue
            filename = self.local_metadata[pub.record_id]
            with open(self.outdir / filename, mode) as f:
                f.write(generate_pub_data(pub))

    def save(self):
        with open(self.local_data_name, "w") as f:
            json.dump(self.local_data, f)

        with open(self.local_metadata_name, "w") as f:
            json.dump(self.local_metadata, f)
