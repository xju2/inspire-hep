# inspire-hep
Fetch citations and self-excluded citations for each article listed in `mypub.py`, create bibtex file `mypub.bib`, and create a csv files with columns of `texkeys, arxiv_eprints, preprint_date, citation_count, citation_count_without_self_citations, doi, title`.

## Instructions: 
* write down the HEP Inspire-ID in `mypub.py`
* run `python update.py`
It will produce two files `mypub.bib` and `mypub.csv`.

## Get bib
```bash
python get_bib.py test_bib.txt
```
