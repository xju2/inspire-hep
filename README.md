# inspire-hep
Fetch citations and self-excluded citations for each article listed in `mypub.py`, create bibtex file `mypub.bib`, and create a csv files with columns of `texkeys, arxiv_eprints, preprint_date, citation_count, citation_count_without_self_citations, doi, title`.

## Instructions:
* write down the HEP Inspire-ID in `mypub.py`
* run `python update.py -w 4 --mode u `
It will produce two files `mypub.bib` and `mypub.csv`.

## Get bib
```bash
python get_bib.py test_bib.txt
```

## Get total citation count
```bash
python get_citation_count.py publications/mypub.csv
```

## Example of json file from Inspire-API
[example.json](https://github.com/xju2/inspire-hep/blob/main/example.json)