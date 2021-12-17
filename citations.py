#!/usr/bin/env python 

import urllib.request, json

def citations(id_type, id_value, debug=False):
    inspire_api = f'https://inspirehep.net/api/{id_type}/{id_value}'
    if debug: print(f"launching API: {inspire_api}")
    data = json.loads(urllib.request.urlopen(inspire_api).read())
    if debug:
        print(data)
    meta = data['metadata']
    bibtex_url = data['links']['bibtex']
    bibtex = urllib.request.urlopen(bibtex_url).read()
    if type(bibtex) is bytes:
        bibtex = bibtex.decode("utf-8")
    
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
        arxiv_eprint = arxiv_category = prepring_date = "N/A"

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
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fetch citations for HEP articles")
    add_arg = parser.add_argument
    add_arg("--id-type", help="identification type",
        choices=['literature', 'doi', 'arxiv'], default='literature')
    add_arg("--id-value", help='identfication value', required=True)
    
    args = parser.parse_args()
    res = citations(args.id_type, args.id_value)
    print(res)