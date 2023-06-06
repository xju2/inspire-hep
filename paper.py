from collections import namedtuple

PaperData = namedtuple(
    "PaperData",
    ["texkeys", "citation_count", "citation_count_without_self_citations",
     "doi", "arxiv_eprints", "arxiv_category", "preprint_date", "title",
     "bibtex", "inspire_id", "authors", "cite_info"
     ]
)
