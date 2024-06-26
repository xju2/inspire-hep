from dataclasses import dataclass


@dataclass
class PaperData:
    record_id: str
    texkeys: str
    citation_count: int
    citation_count_without_self_citations: int
    doi: str
    arxiv_eprints: str
    arxiv_category: str
    preprint_date: str
    title: str
    bibtex: str
    inspire_id: str
    authors: str
    cite_info: str
    url: str

    def __post_init__(self):
        assert self.record_id, "Record ID cannot be empty."
        assert self.title, "Title cannot be empty."
        assert self.authors, "Authors cannot be empty."
        assert self.url, "URL cannot be empty."
        assert self.bibtex, "Bibtex cannot be empty."
