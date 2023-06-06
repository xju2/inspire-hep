"""InspireHep class for the inspirehep API.
"""
from typing import List
import urllib.request
import json
import bib as bibHelper
import pprint
import time

from multiprocessing import Pool
from paper import PaperData

pp = pprint.PrettyPrinter(indent=2)

allowed_id_types = ["literature", 'authors', 'institutions',
                    "conferences", "seminars", "journals",
                    "jobs", "experiments", "data"]
allowed_rate = 15  # 15 requests per 5 seconds
sleep_time = 5 / allowed_rate   # sleep time between requests in seconds
class InspireHepLiterature:
    def __init__(self, num_workers: int = 1):
        self.num_workers = num_workers

    def get(self, recid: int, debug=False) -> PaperData:
        """Get the metadata for a given recid."""
        inspire_api = f'https://inspirehep.net/api/literature/{recid}'
        if debug:
            print(f"launching API: {inspire_api}")
        data = json.loads(urllib.request.urlopen(inspire_api).read())
        if debug:
            pp.pprint(data)

        meta = data['metadata']
        bibtex_url = data['links']['bibtex']
        bibtex = urllib.request.urlopen(bibtex_url).read()
        if type(bibtex) is bytes:
            bibtex = bibtex.decode("utf-8")

        bibtex = bibHelper.correct_lhc_authors(bibtex)

        # authors
        authors = bibHelper.correct_lhc_authors(bibtex)

        # maybe the paper is not submitted to a journal yet
        doi = meta['dois'][0]['value'] if "dois" in meta else "N/A"

        # maybe the paper is not availble on arxiv
        try:
            arxiv_info = meta['arxiv_eprints'][0]
            arxiv_eprint = arxiv_info['value']
            arxiv_category = arxiv_info['categories'][0]
            prepring_date = meta['preprint_date']
        except KeyError:
            print("No arxiv info found for INSPIRE ID: ", recid)
            arxiv_eprint = arxiv_category = prepring_date = "N/A"

        # replace preprint date with the publication date
        if "imprint" in meta:
            prepring_date = meta['imprint'][0]['date']

        # get the journal information from bibtex
        cite_info = bibHelper.get_citation_info(bibtex)

        out_data = {
            "texkeys": meta['texkeys'][0],
            "citation_count": meta['citation_count'],
            "citation_count_without_self_citations": meta['citation_count_without_self_citations'],
            "doi": doi,
            "arxiv_eprints": arxiv_eprint,
            "arxiv_category": arxiv_category,
            'preprint_date': prepring_date,
            "title": meta['titles'][0]['title'],
            "bibtex": bibtex,
            "inspire_id": data['id'],
            "authors": authors,
            "cite_info": cite_info
        }

        # add a sleep time so that we don't exceed the rate limit
        time.sleep(sleep_time)

        return PaperData(**out_data)

    def get_multiple(self, recids: List[int], debug=False) -> List[PaperData]:
        """Get the metadata for a list of recids."""
        with Pool(self.num_workers) as p:
            res = p.map(self.get, recids)
        return res

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fetch citations for HEP articles")
    add_arg = parser.add_argument
    add_arg("--id-value", help='identfication value', default=1851403)
    add_arg('-d', '--debug', help='debug mode', action='store_true')

    args = parser.parse_args()
    res = InspireHepLiterature().get(args.id_value, debug=args.debug)
    print("\n")
    pp.pprint(res)
