"""InspireHep class for the inspirehep API."""


import time
from multiprocessing import Pool

import requests

import bib as bibHelper
from paper import PaperData

allowed_rate = 15  # 15 requests per 5 seconds
sleep_time = 5 / allowed_rate  # sleep time between requests in seconds


def get_inspire_data(recid: str) -> PaperData:
    """Get the metadata for a given recid."""
    inspire_api = f"https://inspirehep.net/api/literature/{recid}"

    data = requests.get(inspire_api, timeout=20).json()

    meta = data["metadata"]
    bibtex_url = data["links"]["bibtex"]
    bibtex = requests.get(bibtex_url, timeout=20).content
    if type(bibtex) is bytes:
        bibtex = bibtex.decode("utf-8")

    bibtex = bibHelper.correct_lhc_authors(bibtex)

    # authors
    authors = bibHelper.get_author_list(bibtex)

    # maybe the paper is not submitted to a journal yet
    doi = meta["dois"][0]["value"] if "dois" in meta else "N/A"

    # maybe the paper is not availble on arxiv
    if "arxiv_eprints" in meta:
        arxiv_info = meta["arxiv_eprints"][0]
        arxiv_eprint = arxiv_info["value"]
        arxiv_category = arxiv_info["categories"][0]
        prepring_date = meta["preprint_date"]
    else:
        arxiv_eprint = arxiv_category = prepring_date = "N/A"

    # replace preprint date with the publication date
    if "imprint" in meta:
        prepring_date = meta["imprint"][0]["date"]

    # get the journal information from bibtex
    cite_info = bibHelper.get_citation_info(bibtex)

    out_data = {
        "record_id": recid,
        "texkeys": meta["texkeys"][0],
        "citation_count": meta["citation_count"],
        "citation_count_without_self_citations": meta["citation_count_without_self_citations"],
        "doi": doi,
        "arxiv_eprints": arxiv_eprint,
        "arxiv_category": arxiv_category,
        "preprint_date": prepring_date,
        "title": meta["titles"][0]["title"],
        "bibtex": bibtex,
        "inspire_id": data["id"],
        "authors": authors,
        "cite_info": cite_info,
        "url": f"https://inspirehep.net/literature/{recid}" if arxiv_eprint == "N/A" else f"https://arxiv.org/abs/{arxiv_eprint}",
    }

    # add a sleep time so that we don't exceed the rate limit
    time.sleep(sleep_time)

    return PaperData(**out_data)


class InspireHepLiterature:
    def __init__(self, num_workers: int = 1):
        self.num_workers = num_workers

    def get_multiple(self, recids: list[int]) -> list[PaperData]:
        """Get the metadata for a list of recids."""
        with Pool(self.num_workers) as p:
            res = p.map(get_inspire_data, recids)
        return res


if __name__ == "__main__":
    import argparse
    import pprint

    parser = argparse.ArgumentParser(description="Fetch citations for HEP articles")
    add_arg = parser.add_argument
    add_arg("--id-value", help="identfication value", default=1851403)

    args = parser.parse_args()
    res = get_inspire_data(args.id_value)
    print("\n")
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(res)
