"""Dealing with the CDS data."""

from datetime import datetime

import bibtexparser
import requests
from bibtexparser.bwriter import BibTexWriter
from bs4 import BeautifulSoup

from paper import PaperData


def get_cds_bibtext(cds_id: int):
    """Get the BibTeX entry from CDS."""
    url = f"https://cds.cern.ch/record/{cds_id}/export/hx"
    data = requests.get(url, timeout=20).text
    soup = BeautifulSoup(data, "html.parser")
    bib_text = soup.find("pre").get_text()
    return bib_text


def remove_instiution_name(authors: str):
    """Remove the institution name in parenthesis from the authors' names."""
    authors = authors.split(";")
    authors = [author.split("(")[0].strip() for author in authors]
    return authors


def get_cds_info(cds_id: int):
    """Get the metadata from CDS."""
    url = f"https://cds.cern.ch/record/{cds_id}"
    data = requests.get(url, timeout=20).text
    soup = BeautifulSoup(data, "html.parser")
    table = soup.find_all("table")[1]
    table_content = {}
    if table:
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) < 2:
                continue
            key = cells[0].get_text().strip()
            value = cells[1].get_text()
            if value:
                table_content[key] = value.strip()
            else:
                table_content[key] = "N/A"
    return table_content


def get_cds_data(index: str) -> dict:
    """Get the CDS data for a given index."""
    if not index:
        return None

    if index[:4] == "cds:":
        cds_id = index[4:]
    else:
        print(f"ERROR: invalid CDS index: {index}")

    cds_info = get_cds_info(cds_id)
    title = cds_info.get("Title")
    authors = remove_instiution_name(cds_info.get("Author(s)"))
    journal_ref = cds_info.get("Report number")
    paper_doi = "N/A"
    category = "hep-ex"
    preprint_date = cds_info.get("Imprint").split(".")[0]
    preprint_date = datetime.strptime(preprint_date, "%d %b %Y").date().strftime("%Y-%m-%d")

    bib_text = get_cds_bibtext(cds_id)
    bib_writer = BibTexWriter()
    bib_text = bib_writer.write(bibtexparser.loads(bib_text))

    texkeys = bib_text.split(",")[0].split("{")[-1]

    paper_data = {
        "record_id": index,
        "texkeys": texkeys,
        "citation_count": -1,
        "citation_count_without_self_citations": -1,
        "doi": paper_doi,
        "arxiv_eprints": "N/A",
        "arxiv_category": category,
        "preprint_date": preprint_date,
        "title": title,
        "bibtex": bib_text,
        "inspire_id": "N/A",
        "authors": authors,
        "cite_info": journal_ref,
        "url": f"https://cds.cern.ch/record/{cds_id}",
    }
    return PaperData(**paper_data)
