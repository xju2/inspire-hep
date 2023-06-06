#!/usr/bin/env python

import urllib.request
import json
import bib as bibHelper
import pprint

pp = pprint.PrettyPrinter(indent=2)

def citations(id_type, id_value, debug=False):
    inspire_api = f'https://inspirehep.net/api/{id_type}/{id_value}'
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
    authors = [author["full_name"] for author in meta['authors']]
    authors = ", ".join(authors)

    # maybe the paper is not submitted to a journal yet
    try:
        doi = meta['dois'][0]['value']
    except KeyError:
        doi = "N/A"

    # maybe the paper is not availble on arxiv
    try:
        arxiv_eprint = meta['arxiv_eprints'][0]['value']
        arxiv_category = meta['arxiv_eprints'][0]['categories'][0]
        prepring_date = meta['preprint_date']
    except KeyError:
        print("No arxiv info found for INSPIRE ID: ", id_value)
        arxiv_eprint = arxiv_category = prepring_date = "N/A"

    # replace preprint date with the publication date
    try:
        prepring_date = meta['imprint'][0]['date']
    except KeyError:
        pass

    return {
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
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fetch citations for HEP articles")
    add_arg = parser.add_argument
    add_arg("--id-type", help="identification type",
            choices=['literature', 'doi', 'arxiv'], default='literature')
    add_arg("--id-value", help='identfication value', default=1851403)
    add_arg('-d', '--debug', help='debug mode', action='store_true')

    args = parser.parse_args()
    res = citations(args.id_type, args.id_value, args.debug)
    print("\n")
    pp.pprint(res)
