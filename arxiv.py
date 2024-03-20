"""arXiv related helper functions."""

import asyncio
import re
from datetime import datetime
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession

from inspirehep import get_inspire_data
from paper import PaperData


def find_index(in_str: str):
    pattern = r"[0-9]*\.[0-9]*"
    index = None

    if "arxiv.org" in in_str:
        index = url_to_index(in_str)
    elif re.match(pattern, in_str):
        index = in_str
    elif ":" in in_str:
        # deal with format:  arXiv:1909.03460
        index = in_str.split(":")[-1]
    else:
        return None

    return remove_version(index)


def url_to_index(url: str):
    o = urlparse(url)
    if o.netloc != "arxiv.org":
        print(f"invalid arxiv url: {url}")
        return None

    paths = o.path.split("/")
    index = paths[2] if paths[1] == "abs" else paths[2][:-4]

    return remove_version(index)


def remove_version(index):
    if index is None:
        return index
    pp = "v[0-9]*"
    if re.search(pp, index) is not None:
        idx = index.find("v")
        index = index[:idx]
    return index


async def get_inspire_id(url: str):
    asession = AsyncHTMLSession()
    new_url = await asession.get(url)
    return new_url.url.split("/")[-1]


def get_arxiv_data(index: str) -> PaperData:
    """Get the metadata for a given arXiv index."""
    arxiv_index = find_index(index)
    if arxiv_index is None:
        return None

    arxiv_url = f"https://arxiv.org/abs/{arxiv_index}"

    # try inspire hep first
    inspire_url = f"https://inspirehep.net/arxiv/{arxiv_index}"
    inspire_id = asyncio.run(get_inspire_id(inspire_url))

    if inspire_id is not None and inspire_id != "None":
        inspire_id = int(inspire_id)
        return get_inspire_data(inspire_id)

    # get the arXiv webpage data
    data = requests.get(arxiv_url, timeout=20).text
    # then parse the html data to get the metadata
    soup = BeautifulSoup(data, "html.parser")

    title = soup.find_all("h1", "title mathjax")[0].contents[1]
    authors = [x.text for x in soup.find_all("div", "authors")[0].find_all("a")]

    # arxiv_doi = soup.find_all("td", "tablecell arxivdoi")[0].find_all("a")[0].get("href")
    journal_ref = "N/A"
    paper_doi = "N/A"
    for label in soup.find_all("td", "tablecell label"):
        label_text = label.get_text()
        if "Journal" in label_text:
            journal_ref = label.next_sibling.next_sibling.get_text()
        if "DOI" in label_text:
            paper_doi = label.next_sibling.next_sibling.find_all("a")[0].get("href")

    category = soup.find_all("span", "primary-subject")[0].text
    category = re.search(r"\((.*)\)", category).group(1)
    preprint_date = re.search(
        r"(\d+ \w+ \d+)", soup.find_all("div", "submission-history")[0].text
    ).group(1)
    preprint_date = datetime.strptime(preprint_date, "%d %b %Y").date().strftime("%Y-%m-%d")

    # get cite count from google scholar
    cite_url = f"https://scholar.google.com/scholar?q=arXiv:{arxiv_index}"
    cite_data = requests.get(cite_url, timeout=20).text
    cite_soup = BeautifulSoup(cite_data, "html.parser")
    cite_count = cite_soup.find_all("div", "gs_ab_mdw")[0].text
    cite_count = [x.text.split()[-1] for x in cite_soup.find_all("a") if "Cited by" in x.text]
    cite_count = int(cite_count[0]) if len(cite_count) > 0 else 0

    # try to get as much information as possible for the PaperData
    paper_data = {
        "texkeys": "",
        "citation_count": cite_count,
        "citation_count_without_self_citations": -1,
        "doi": paper_doi,
        "arxiv_eprints": arxiv_index,
        "arxiv_category": category,
        "preprint_date": preprint_date,
        "title": title,
        "bibtex": "N/A",
        "inspire_id": "N/A",
        "authors": authors,
        "cite_info": f"arXiv:{arxiv_index}" if journal_ref == "N/A" else journal_ref,
    }

    return PaperData(**paper_data)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="")
    add_arg = parser.add_argument
    # add_arg('', help='')

    args = parser.parse_args()

    url = "https://arxiv.org/abs/1909.03460v1"
    print(url_to_index(url))
    url = "https://arxiv.org/pdf/1909.03460.pdf"
    print(url_to_index(url))

    print(find_index("arxiv:1909.03460"))
    print(find_index("1909.03460v2"))
    print(find_index("1909.03460"))
    print(find_index("190x9.03460"))

    print(get_arxiv_data("1909.03460"))
